#from flask import (
#    render_template,
#    request,
#    redirect,
#    flash
#)
from algorithms.create_rsa_key import create_rsa_key

from app import app

@app.route('/')
def base():
    (n,e) = create_rsa_key(1024)
    html = f'<!DOCTYPE html><html><body><h1>RSA-avain</h1><p>{n} --- {e}</p></body></html>'
    return html
