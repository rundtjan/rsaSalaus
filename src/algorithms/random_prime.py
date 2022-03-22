import random
from .miller_rabin import miller_rabin

def random_prime(min_max):
    """Funktio, joka tuottaa satunnaisen (todennäköisen) alkuluvun, tiettyjen rajojen sisällä.
    
    Parametrit:
        Monikko, jossa kokonaisluvut (minimiraja, maksimiraja).

    Palautusarvo:
        Kokonaisluku, min/max-rajojen sisällä, joka on todennäköisesti alkuluku.
    """

    (min, max) = min_max
    while(True):
        n = random.randrange(min,max)
        if miller_rabin(n,40): break
    return n

def min_max(length,first_number):
    """Funktio, joka luo minimi- ja maksimirajan tietyn bittipitoisuuden ja mahd. toisen luvun perusteella.
    
    Parametrit:
        Kokonaisluku length - bittipituus.
        Kokonaisluku first_number - voi myös olla None. Jos käytetty, määrittää sopivat rajat, 
            jotta uuden ja tämän luvun tulo olisi sopivaa bittipituutta.

    Palautusarvo:
        Monikko, jossa kokonaisluvut (minimi-, maksimiraja).
    """

    min = pow(2, length)
    max = pow(2, length+1)-1
    if first_number:
        min //= first_number
        min += pow(10, 10)
        max //= first_number
    return (min,max)

def get_prime_numbers(length_of_product):
    """Funktio, joka luo kahta sopivankokoista alkulukua.
    
    Parametrit:
        Kokonaisluku length_of_product - bittipituus, jota toivotaan olevan näiden kahden lukujen tulon pituus.

    Palautusarvo:
        Monikko, jossa kokonaisluvut (p,q), jonka tulon bittipituus on length_of_product:in määrittämä.
    """
    
    half_plus_length = length_of_product//2 + length_of_product//20
    p = random_prime(min_max(half_plus_length,None))
    q = random_prime(min_max(length_of_product,p))
    return (p,q)
