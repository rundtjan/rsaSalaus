import random

def test_for_prime(n, d, r):
    """Funktio, joka kokeilee eri arvoja 'a' vastaan, että onko luku alkuluku.
    
    Parametrit:
        Kokonaisluku n - luku jota testataan.
        Kokonaisluku d - saadaan Miller-Rabin:in alkupuolesta. Yhtälöstä n-1 = 2^r * d
        Kokonaisluku r - saadaan samasta yhtälöstä kuin d (yllä). Määrittelee, montako kierrosta testataan lukua.

    Palautusarvo:
        Boolean - True jos luku näytti alkuluvulta, kun testataan lukua 'a' vastaan. False jos selvästi ei ole alkuluku.     
    """

    a = random.randrange(2, n-2)
    x = pow(a, d, n)
    if x == 1 or x == n-1:
        return True
    for _ in range(r-1):
        x = pow(x, 2, n)
        if x == n - 1:
            return True
    return False


def miller_rabin(n, k):
    """Funktio, joka toteuttaa Miller-Rabin:in algoritmi. Eli testaa, onko luku todennäköisesti alkuluku.
    
    Parametrit:
        Kokonaisluku n - luku jota testataan.
        Kokonaisluku k - positiivinen luku, joka säätää algoritmin tarkkuutta. Esim. 40 on sopivan suuri luku. Virhetodennäköisyys 1/(4^k).

    Palautusarvo:
        Boolean: True jos luku on todennäköisesti alkuluku. False jos luku varmasti ei ole alkuluku.
    """

    if n>0 and n <=3:return True
    if n % 2 == 0: return False 

    nMin1 = n - 1
    r = 0 
    d = nMin1
    result = True

    while d % 2 == 0:
        r += 1
        d //= 2

    for _ in range(k):
        result = test_for_prime(n, d, r)
        if result is False:
            break

    return result
