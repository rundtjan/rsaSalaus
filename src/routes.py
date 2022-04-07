import os
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
    html = f'<h1>Rsa-Service</h1><p>Please visit <a href="/createkeys/{file}">this page</a> to download your Rsa-keys.</p>'
    html += f'<p>Encrypt a message <a href="/encrypt">here</a></p>'
    html += f'<p>Decrypt a message <a href="/decrypt">here</a></p>'
    return html

@app.route('/createkeys/<file>')
def keys(file):
    (n,e,d) = rsa_key_gen.create()
    f = open(os.path.join(app.root_path, f'temp/{file}.txt'), "w")
    f.write(f'PUBLIC KEY:\n{n}#{e}\n\nPRIVATE KEY:\n{n}#{d}')
    f.close()
    html = f'<h1>Key generation</h1><p><b>Please download</b> your <a href="/download/{file}">keys</a></p>'
    html += f'<p><b>After downloading</b>, please delete the keys from the server and <a href="/delete/{file}">return to the mainpage</a></p>'
    return html

@app.route('/delete/<file>')
def delete(file):
    if os.path.exists(os.path.join(app.root_path, f'temp/{file}.txt')):
        os.remove(os.path.join(app.root_path, f'temp/{file}.txt'))
    return redirect('/')  

@app.route('/download/<file>')
def download(file):
    return send_from_directory(os.path.join(app.root_path, 'temp'), f'{file}.txt', as_attachment=True)

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