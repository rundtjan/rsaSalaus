#from flask import (
#    render_template,
#    request,
#    redirect,
#    flash
#)
from algorithms.create_rsa_key import create_rsa_key
from algorithms.encrypt import rsa_encrypt

from app import app

@app.route('/')
def base():
    (n,e,d) = create_rsa_key(1024)
    message = 'This is a very, very secret message, I can ensure you.'
    encrypted = rsa_encrypt(message, n, e)
    html = f'<!DOCTYPE html><html><body><h1>Sinun julkinen RSA-avain:</h1><p>{n[:150]}</p><p>{n[151:]} --- {e}</p><h1>Sinun yksityinen avain:</h1><p>{d}</p>'
    html += f'<h1>Viesti ennen kryptausta:</h1><p>{message}<p><h1>Kryptattu viesti:</h1><p>{encrypted[:150]}</p><p>{encrypted[151:]}</p></body></html>'
    return html
