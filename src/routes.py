import random
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
    file = random.randrange(100000,1000000)
    html = f'<h1>Rsa-Service</h1><p>Please visit <a href="/genKeys">this page</a> to generate Rsa-keys.</p>'
    html += f'<p>Encrypt a message <a href="/encrypt">here</a></p>'
    html += f'<p>Decrypt a message <a href="/decrypt">here</a></p>'
    return html

@app.route('/genKeys')
def gen_keys():
    (n,e,d) = rsa_key_gen.create()
    html = '<h1>Your RSA-keys</h1><p>Please copy and store in a safe place</p>'
    html += '<p>Return to <a href="/">the mainpage</a></p>'
    html += '<h3>Public key</h3>'
    html += f'<p style="overflow-wrap: break-word;">{n}#{e}</p>'
    html += '<h3>Private key</h3>'
    html += f'<p style="overflow-wrap: break-word;">{n}#{d}</p>'
    return html

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