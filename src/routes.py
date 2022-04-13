import timeit
from statistics import mean, median, stdev
from flask import (
    render_template,
    redirect,
    send_from_directory,
    current_app,
    request
#    flash
)
from flask_login import login_required, current_user
from app import app
from rsa_service.RsaKeyGenerator import RsaKeyGenerator
from rsa_service.RsaService import RsaService

rsa_key_gen = RsaKeyGenerator(1024)
rsa_service = RsaService()

@app.route('/')
def base():
    return render_template('index.html')

@app.route('/genKeys')
def gen_keys():
    (n,e,d) = rsa_key_gen.create()
    return render_template('keys.html', n=n, e=e, d=d)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/encrypt')
def encrypt():
    return render_template('encrypt.html')

@app.route("/encrypt", methods=["POST"])
def handle_encrypt():
    if "encrypt_button" in request.form:
        message = request.form.get('message')
        key = request.form.get('publickey').split('#')
        encrypted = rsa_service.encrypt(message, int(key[0]), int(key[1]))
        return render_template('encrypt.html', encrypted=encrypted)

@app.route('/decrypt')
def decrypt():
    return render_template('decrypt.html')

@app.route("/decrypt", methods=["POST"])
def handle_decrypt():
    if "decrypt_button" in request.form:
        message = request.form.get('message')
        key = request.form.get('privatekey').split('#')
        decrypted = rsa_service.decrypt(message, int(key[0]), int(key[1]))
        return render_template('decrypt.html', decrypted=decrypted)

@app.route("/timecheck")
def time_check():
    times = 100
    t = timeit.repeat(lambda: rsa_key_gen.create(), number=1, repeat=times)
    m = round(mean(t), 3)
    me = round(median(t),3)
    std = round(stdev(t),3)
    mx = round(max(t), 3)
    mn = round(min(t), 3)
    return f'Mean: {str(m)} seconds median: {str(me)} seconds, standard deviation: {str(std)} seconds <br/>Max: {mx} seconds, min: {mn} seconds.'

@app.route("/timecheck_encrypt")
def time_check_encrypt():
    (n,e,d) = rsa_key_gen.create()
    message = "It's like a jungle sometimes, it makes me wonder how I keep from going under (ha ha ha ha ha)."
    times = 100
    t = timeit.repeat(lambda: rsa_service.encrypt(message, n, e), number=1, repeat=times)
    m = round(mean(t), 6)
    me = round(median(t),6)
    std = round(stdev(t),6)
    mx = round(max(t), 6)
    mn = round(min(t), 6)
    return f'Mean: {str(m)} seconds median: {str(me)} seconds, standard deviation: {str(std)} seconds <br/>Max: {mx} seconds, min: {mn} seconds.'
