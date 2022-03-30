from hashlib import sha512

def to_len(h, len):
    return h #joka jollain tavalla säädetään pituuteen len

def hash(str, len):
    h = sha512(str).digest() 
    to_len(h, len)
    return h


def byte_to_bin_string(bytes):
    '''Funktio, joka muuntaa byte-jonon binäärimerkkijonoksi
    
    Parametrit:
        bytes - b''
    
    Palautusarvo - merkkijono, jossa bytes binäärisessä esitysmuodossa.

    '''
    b_m = ''
    for byte in list(bytes):
        b = format(byte, 'b')
        ex = 8 - len(b)
        if ex > 0:
            z = '0'*ex
            b = z + b
        b_m += b
    return b_m    

def string_to_bin(m):
    '''Funktio, joka muuntaa merkkijonon binääriseksi.
    
    Parametrit:
        m - merkkijono.

    Palautusarvo:
        Merkkijono, vastaa sisällöltään parametrin merkkijono, mutta
        jokainen merkki käännetty 8-merkkiseksi binääriseksi luvuksi.
    '''
    m = m.encode('utf8')
    return byte_to_bin_string(m)

def mgf1(db, length):
    '''Funktio, suoraan OAEP:n määrittelystä.
    
    Parametrit:
        db - datablokki binäärisessä esitysmuodossa, merkkijono
        length - palautusarvon toivottu pituus - pitää tarkistaa

    Palautusarvo:
        Merkkijono, hash-funktion tulos, binäärisessä esitysmuodossa.

    '''
    counter = 0
    oct_str = str(db).encode('utf-8')
    output = b''
    while len(output) < length // 8:
        c_b = str(counter).encode('utf-8')
        output += sha512(oct_str+c_b).digest()
        print(counter, len(output))
        counter += 1
    return byte_to_bin_string(output[:length//8])

def xor(a,b):
    '''Funktio, joka tuottaa xor-tuloksen kahdesta parametrista.
    
    Parametrit:
        a - merkkijono, sisältönä binäärinen luku.
        b - merkkijono, sisältönä binäärinen luku.

    Palautusarvo:
        c - merkkijono, sisältönä xor-binäärinen tulos a ja b:sta.

    '''
    c = a+b #xor tapahtuisi jollain tavalla täällä
    return c

def oaep(m0, rand, db_len):
    '''Funktio, joka hoitaa oaep-padding:

    Parametrit:
        m0 - alkuperäinen viesti merkkijonona, binääristä dataa.
        rand - satunnainen viestiosuus, "padding", merkkijono, binääristä dataa.
        db_len - algoritmin datablokin pituus

    Palautusarvo:
        oaep_m - viestiosuuden ja satunnaisen viestiosuuden yhdistelmä, merkkijono, binääristä dataa.

    '''
    m1 = m0 + [0] * (db_len - len(m0))
    m1 = xor(m1, mgf1(rand, db_len))
    rand = xor(rand, mgf1(m1, len(rand)))
    return m1 + rand

def rsa(padded, e, n):
    '''Funktio, joka tekee itse rsa-laskelman.
    
    Parametrit:
        padded - salattava viesti oaep-käsittelyn jälkeen.
        e - julkisen avaimen e-osuus
        n - julkisen avaimen n-osuus
    
    '''
    return pow(padded, e, n)

def rsa_encrypt(m0, n, e, rand, db_len):
    '''Funktio, joka tuottaa rsa-salauksen oaep-padding-tekniikan avulla.
    
    Parametrit:
        m0 - alkuperäinen viesti merkkijonona.
        n - julkisen avaimen n-osuus
        e - julkisen avaimen e-osuus
        rand - viestin satunnainen osuus samassa esitysmuodossa kuin m0.
        db_len - salattavan datablokin lopullinen pituus, m0 + '0'*(db_len - len(m0))

    Palautusarvo:
        Salattu viesti, merkkijonona, binääristä dataa.
    '''
    padded = oaep(m0, rand, db_len)
    rsa_m = rsa(padded, e, n)
    return rsa_m
