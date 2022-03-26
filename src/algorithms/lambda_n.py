def gcd(a,b):
    """Funktio, joka löytää kahden luvun suurin yhteinen tekijä.

    Parametrit:
        Kaksi kokonaislukua, joiden syt halutaan löytää.

    Palautusarvo:
        Kokonaisluku, eli suurin yhteinen tekijä.
    """

    while b != 0:
        t = b
        b = a % b
        a = t
    return a

def lcm(a,b):
    """Funktio, joka löytää kahden luvun pienin yhteinen jaettava.

    Parametrit:
        Kaksi kokonaislukua.

    Palautusarvo:
        Kokonaisluku, joka on kahden luvun pienin yhteinen jaettava.
    """

    return a*b/gcd(a,b)

def lambda_n(p,q):
    """Funktio, joka löytää λ(n) - luku, jota tarvitaan rsa-algoritmissa.

    Parametrit:
        RSA-algoritmin alkuluvut p ja q.

    Palautusarvo:
        Kokonaisluku, eli λ(n).
    """

    return lcm(p-1,q-1)
