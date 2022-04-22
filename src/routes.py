import timeit
from statistics import mean, median, stdev
from flask import (
    render_template,
    redirect,
    request,
    flash
)
from app import app
from rsa_service.RsaKeyGenerator import RsaKeyGenerator
from rsa_service.RsaService import RsaService

rsa_key_gen = RsaKeyGenerator(1024)
rsa_service = RsaService()

@app.route('/')
def base():
    '''Funktio, joka hoitaa GET-kutsut /-polkuun.

    Palautusarvo:
        Edelleensiirto polkuun /genKeys
    '''
    return redirect('/genKeys')

@app.route('/genKeys')
def gen_keys():
    '''Funktio, joka hoitaa GET-kutsut /genKeys-polkuun.

    Palautusarvo:
        Avaa sivun keys.html ja näyttää luodut rsa-avaimet.
    '''
    (n,e,d) = rsa_key_gen.create()
    return render_template('keys.html', n=n, e=e, d=d)

@app.route('/encrypt')
def encrypt():
    '''Funktio, joka hoitaa GET-kutsut /encrypt-polkuun.

    Palautusarvo:
        Avaa sivun encrypt.html.
    '''
    return render_template('encrypt.html')

@app.route("/encrypt", methods=["POST"])
def handle_encrypt():
    '''Funktio, joka hoitaa POST-kutsut /encrypt-polkuun.

    Palautusarvo:
        Palauttaa virheitä, jos viesti tai julkinen avain puuttuu tai on virheellinen.
        Muuten palauttaa encrypt-sivun jossa salattu viesti. 
    '''
    if "encrypt_button" in request.form:
        message = request.form.get('message')
        if len(message) == 0:
            flash('Please enter a message')
            return redirect("/encrypt")
        try:
            key = request.form.get('publickey').split('#')
            encrypted = rsa_service.encrypt(message, int(key[0]), int(key[1]))
            return render_template('encrypt.html', encrypted=encrypted)
        except:
            flash("Please enter a valid public key.")
            return redirect("/encrypt")

@app.route('/decrypt')
def decrypt():
    '''Funktio, joka hoitaa GET-kutsut /decrypt-polkuun.

    Palautusarvo:
        Avaa sivun decrypt.html.
    '''
    return render_template('decrypt.html')

@app.route("/decrypt", methods=["POST"])
def handle_decrypt():
    '''Funktio, joka hoitaa POST-kutsut /decrypt-polkuun.

    Palautusarvo:
        Palauttaa virheitä, jos viesti tai yksityinen avain puuttuu tai on virheellinen.
        Muuten palauttaa decrypt-sivun jossa viesti jonka salaus on purettu. 
    '''
    if "decrypt_button" in request.form:
        message = request.form.get('message')
        if len(message) == 0:
            flash('Please enter a message')
            return redirect('/decrypt')
        if not rsa_service.check_valid_decrypt_message(message):
            flash('Please enter a valid encrypted message in binary format')
            return redirect('/decrypt')
        key = request.form.get('privatekey')
        if len(key) == 0:
            flash('Please enter a private key')
            return redirect('/decrypt')
        key = key.split('#')
        if len(key) != 2:
            flash('Please enter a valid private key')
            return redirect('/decrypt')
        try:
            decrypted = rsa_service.decrypt(message, int(key[0]), int(key[1]))
            return render_template('decrypt.html', decrypted=decrypted)
        except:
            flash('Please enter a valid encrypted message and a valid private key.')
            return redirect('/decrypt')

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

@app.route("/timecheck_decrypt")
def time_check_decrypt():
    (n,e,d) = rsa_key_gen.create()
    message = "It's like a jungle sometimes, it makes me wonder how I keep from going under (ha ha ha ha ha)."
    c = rsa_service.encrypt(message, n, e)
    times = 100
    t = timeit.repeat(lambda: rsa_service.decrypt(c, n, d), number=1, repeat=times)
    m = round(mean(t), 6)
    me = round(median(t),6)
    std = round(stdev(t),6)
    mx = round(max(t), 6)
    mn = round(min(t), 6)
    return f'Mean: {str(m)} seconds median: {str(me)} seconds, standard deviation: {str(std)} seconds <br/>Max: {mx} seconds, min: {mn} seconds.'
