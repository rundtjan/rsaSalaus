from hashlib import sha512

def to_len(h, len):
    return h #joka jollain tavalla säädetään pituuteen len

def hash(str, len):
    h = sha512(str).digest() 
    to_len(h, len)
    return h

def xor(a,b):
    '''Funktio, joka tuottaa xor-tuloksen kahdesta parametrista.
    
    Parametrit:
        a - octet string?
        b - octet string?

    Palautusarvo:
        c - octet string, joka on a:n ja b:n xor-tulos?

    '''
    c = a+b #xor tapahtuisi jollain tavalla täällä
    return c

def oaep(m0, rand, m1_len, rand_len):
    '''Funktio, joka hoitaa oaep-padding:

    Parametrit:
        m0 - alkuperäinen viesti octet stringinä.
        rand - satunnainen viestiosuus, "padding"
        m1_len - algoritmin viestiosuuden pituus
        rand_len - satunnaisen viestiosuuden pituus

    Palautusarvo:
        oaep_m - viestiosuuden ja satunnaisen viestiosuuden yhdistelmä, octet stringinä.

    '''
    m1 = m0 + [0] * (m1_len - len(m0))
    m1 = xor(m1, hash(rand, m1_len))
    rand = xor(rand, hash(m1, rand_len))
    return concat(m1, rand) #miten konkatenoida nämä?

def rsa(padded, e, n):
    '''Funktio, joka tekee itse rsa-laskelman.
    
    Parametrit:
        padded - salattava viesti oaep-käsittelyn jälkeen.
        e - julkisen avaimen e-osuus
        n - julkisen avaimen n-osuus
    
    '''
    return pow(padded, e, n)

def rsa_encrypt(m0, n, e, rand, m1_len, rand_len):
    '''Funktio, joka tuottaa rsa-salauksen oaep-padding-tekniikan avulla.
    
    Parametrit:
        m0 - alkuperäinen viesti jossain esitysmuodossa. (octet string?)
        n - julkisen avaimen n-osuus
        e - julkisen avaimen e-osuus
        rand - viestin satunnainen osuus samassa esitysmuodossa kuin m0.
        m1_len - salattavan viestin ei-satunnainen osuus, m0 + '0'*(m1_len - len(m0))
        rand_len - satunnaisen osuuden pituus. (m1_len + rand_len pitää olla sopiva verrattuna n:ään)

    Palautusarvo:
        Salattu viesti, jossain esitysmuodossa (octet string?).
    '''
    padded = oaep(m0, rand, m1_len, rand_len)
    rsa_m = rsa(padded, e, n)
    return rsa_m

def first_encrypt(m, n, e):
    #m = int.from_bytes(m.encode('utf-8'), byteorder='big')
    #print(m)
    m = m.encode('utf8')
    print(m)
    print(list(m))
    len_m = len(m)*8
    len_n = 1024
    print(len_n - len_m)
    c = 0
    # c = m^e mod n
    # c = pow(m,e,n)
    return c

first_encrypt('hello world, how wonderful it is to be alive, is it not?', 123412341234123412341241241234123412, e = pow(2,16) + 1)