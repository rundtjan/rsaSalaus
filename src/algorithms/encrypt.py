from hashlib import sha512
import random

def byte_to_bin_string(bytestring):
    '''Funktio, joka muuntaa byte-jonon binäärimerkkijonoksi

    Parametrit:
        bytes - b''

    Palautusarvo - merkkijono, jossa bytes binäärisessä esitysmuodossa.

    '''
    b_m = ''
    for byte in list(bytestring):
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
        length - palautusarvon toivottu pituus

    Palautusarvo:
        Merkkijono, hash-funktion tulos, binäärisessä esitysmuodossa.

    '''
    counter = 0
    oct_str = str(db).encode('utf-8')
    output = b''
    while len(output) < length // 8:
        c_b = str(counter).encode('utf-8')
        output += sha512(oct_str+c_b).digest()
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
    c = ''
    assert len(a) == len(b), "a and b should be of same length"
    for i in range(0,len(a)):
        if a[i] == b[i]:
            c += '0'
        else:
            c += '1'
    return c

def oaep(message, seed, db_len):
    '''Funktio, joka hoitaa oaep-padding:

    Parametrit:
        message - alkuperäinen viesti merkkijonona, binääristä dataa.
        seed - satunnainen viestiosuus, "padding", merkkijono, binääristä dataa.
        db_len - algoritmin datablokin pituus

    Palautusarvo:
        oaep_m - viestiosuuden ja satunnaisen viestiosuuden yhdistelmä, merkkijono,
        binääristä dataa.

    '''
    db = message + '0' * (db_len - len(message))
    db_mask = mgf1(seed, db_len)
    db = xor(db, db_mask)
    seed_mask = mgf1(db, len(seed))
    seed = xor(seed, seed_mask)
    return db + seed

def rsa(padded, e, n):
    '''Funktio, joka tekee itse rsa-laskelman.

    Parametrit:
        padded - salattava viesti oaep-käsittelyn jälkeen.
        e - julkisen avaimen e-osuus
        n - julkisen avaimen n-osuus

    '''
    return pow(padded, e, n)

def bit_length_of(i):
    '''Funktio, joka tarkistaa kokonaisluvun bittipituus.

    Parametrit:
        i - kokonaisluku.

    Palautusarvo:
        kokonaisluku, i:n bittipituus.
    '''
    return len(bin(i)[2:])

def create_random_seed(length):
    '''Funktio, joka tuottaa satunnaisen viestin osuus, oaep:n tarvitsema seed.

    Parametrit:
        length - kokonaisluku, seedin pituus.

    Palautusarvo:
        seed - merkkijono, binääristä dataa.
    '''
    seed = ''
    for _ in range(length):
        seed += str(random.randint(0,1))
    return seed

def bin_string_to_int(b_s):
    '''Funktio, joka muuntaa binäärinen merkkijono kokonaisluvuksi.
    
    Parametrit:
        b_s - merkkijono, binääristä dataa.

    Palauttaa:
        kokonaisluvun.
    
    '''
    return int(b_s, 2)


def rsa_encrypt(message, n, e):
    '''Funktio, joka tuottaa rsa-salauksen oaep-padding-tekniikan avulla.

    Parametrit:
        message - alkuperäinen viestin sopivan kokoinen osa merkkijonona, binääristä dataa.
        n - julkisen avaimen n-osuus
        e - julkisen avaimen e-osuus
        db_len - salattavan datablokin lopullinen pituus, m0 + '0'*(db_len - len(message))
            -- esim db_len, jos salattava viesti oltava < len(bits(n)),
            -- jolloin db_len = 1024 - 1 kpl. byte (8) - len(seed) (bytes, eli x*8)
            -- esim jos len(seed) = 24 * 8 = 192, db_len = 1024-8-192 = 824
            -- len(message) < db_len

    Palautusarvo:
        Salattu viesti, merkkijonona, binääristä dataa.
    '''
    n_len = bit_length_of(n)
    seed = create_random_seed(n_len // 4)
    assert len(seed) % 8 == 0, "seed should be divisible by 8"
    db_len = n_len -8 - len(seed)
    message = string_to_bin(message)
    assert len(message) < (n_len - len(seed)), "the message is too long"
    padded = oaep(message, seed, db_len)
    pad_m_int = bin_string_to_int(padded)
    rsa_m = rsa(pad_m_int, e, n)
    rsa_m = bin(rsa_m)[2:]
    return rsa_m

def rsa_reverse(message, n, d):
    return pow(message, d, n)

def reverse_oaep(db, seed):
    '''Funktio, joka käyttää oaep-padding-toimintoa toisinpäin.

    Parametrit:
        db - merkkijono, oaep-käsitelty viestiosuus, binääristä dataa
        seed - merkkijono, oaep-käsitelty satunnainen osuus, binääristä dataa

    Palautusarvo:
        db - merkkijono, viestiosuus ilman oaep-käsittelyä, binääristä dataa
    '''
    seed_mask = mgf1(db, len(seed))
    seed = xor(seed, seed_mask)
    db_mask = mgf1(seed, len(db))
    db = xor(db, db_mask)
    return db

def correct_length(message, n):
    '''Funktio, joka lisää kryptattuun viestiin tarvittaessa etunollia.

    Parametrit:
        message - merkkijono, binääristä dataa
        n - kokonaisluku, jonka bittipituus määrittelee viestin pituutta.

    Palautusarvo:
        message - merkkijono, oikean pituinen.
    '''
    correct_len = bit_length_of(n) - 8
    if correct_len - len(message) > 0:
        message = ('0'*(correct_len-len(message))) + message
    return message

def split_into_db_and_seed(message, n):
    '''Funktio, joka löytää kryptatusta viestistä datablokin ja seed:in.

    Parametrit:
        message - merkkijono.
        n - kokonaisluku.

    Palautusarvo:
        (db, seed) - tuple, datablokki ja seed.

    '''
    n_len = bit_length_of(n)
    seed_len = n_len // 4
    seed = message[n_len-8-seed_len:]
    db = message[:n_len-8-seed_len]
    return (db, seed)

def from_bin_to_text_string(db):
    '''Funktio, joka muuntaa merkkijonon binääristä dataa tekstimuotoon.

    Parametrit:
        db - merkkijono, binääristä dataa.

    Palautusarvot:
        message - merkkijono, tekstisisältöä.
    '''
    byte_db = bytes(int(db[i: i+8], 2) for i in range(0, len(db), 8))
    message = byte_db.decode('utf-8')
    return message

def rsa_decrypt(message, n, d):
    '''Funktio, joka poistaa salauksen viestistä.

    Parametrit:
        message - merkkijono, binääristä dataa, kryptattu viesti.
        n - kokonaisluku, osa julkista ja yksityistä avainta.
        d - kokonaisluku, osa yksityistä avainta.

    Palautusarvo:
        message - merkkijono, alkuperäinen/dekryptattu viesti.
    '''
    message = bin_string_to_int(message)
    message = rsa_reverse(message, n , d)
    message = bin(message)[2:]
    message = correct_length(message, n)
    (db, seed) = split_into_db_and_seed(message, n)
    db = reverse_oaep(db, seed)
    message = from_bin_to_text_string(db)
    return message
