from .lambda_n import gcd

def find_e(l_n):
    """Funktio, joka löytää rsa-avaimen ns. e-arvo.

    Parametrit:
        Kokonaisluku, joka tulee olemaan e-arvon kanssa keskenään jaoton.

    Palautusarvo:
        Kokonaisluku, eli e-arvo.
    """

    if l_n > pow(2,19):
        e = pow(2,16) + 1
    else:
        e = 3
    while True:
        if gcd(l_n,e) == 1:
            break
        e += 1
    return e
