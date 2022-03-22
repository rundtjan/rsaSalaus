def gcd(a,b):
    """Funktio joka löytää kahden luvun suurin yhteinen tekijä.
    
    Argumentit:
        Kaksi lukua.
    
    Palauttaa:
        Yksi luku: suurin yhteinen tekijä.
    """

    while(b != 0):
        t = b
        b = a % b
        a = t
    return a
