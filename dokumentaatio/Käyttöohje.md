# Käyttöohje

Kloonaa repo. Siirry juurikansioon, ja ajaa:  
```bash
poetry install
```
Siirry poetry shelliin:  
```bash
poetry shell
```
ja käynnistä sovellus:
```bash
python3 src/index.py
```
Windows-koneella:
```bash
python src/index.py
```
Avaa selain osoitteella:  
```bash
http://localhost:5000
```
Ensiksi avautuu RSA-avain-näkymä. Voit kopioida avaimet esim. txt-tiedostoon.
'Encrypt message'-näkymässä voit kirjoittaa viestin message-kenttään ja kopioida julkisen avaimen public-key kenttään ja painaa 'encrypt'.  
'Decrypt message'-näkymässä voit kirjoittaa salatun viestin message-kenttään ja kopioida yksityisen avaimen private-key kenttään ja painaa 'decrypt'.  
Huom! Jos käytät viallista tai väärää avainta, järjestelmä herjaa virhettä.
