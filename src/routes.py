from app import app
from flask import (
    render_template,
    redirect
#    request,
#    flash
)
from flask_login import login_required, current_user
from rsa_service.encrypt import rsa_encrypt, rsa_decrypt
from rsa_service.RsaKeyGenerator import RsaKeyGenerator

rsa_key_gen = RsaKeyGenerator(1024)

@app.route('/')
def base():
    (n,e,d) = rsa_key_gen.create()
    message = 'This is a very, very secret message, I can ensure you.'
    encrypted = rsa_encrypt(message, n, e)
    decrypted = rsa_decrypt(encrypted, n, d)
    html = f'<!DOCTYPE html><html><body><h1>Sinun julkinen RSA-avain:</h1><p>{str(n)[:150]}<br />{str(n)[151:]} --- {e}</p>'
    html += f'<h1>Sinun yksityinen avain:</h1><p>{str(d)[:150]}<br />{str(d)[151:]}</p>'
    html += f'<h1>Viesti ennen kryptausta:</h1><p>{message}<p><h1>Kryptattu viesti:</h1>'
    html += f'<p>{str(encrypted)[:150]}<br />{str(encrypted)[151:300]}<br />{str(encrypted)[301:450]}<br />{str(encrypted)[451:600]}<br />'
    html += f'{str(encrypted)[651:800]}<br />{str(encrypted)[801:950]}<br />{str(encrypted)[951:]}</p></body></html>'
    html += f'<h1>Viesti dekryptattu</h1><p>{decrypted}</p>'
    return html

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/test')
def test():
    if current_user.is_authenticated:
        return redirect("/lukuvinkkiview")
    return redirect("/login")
