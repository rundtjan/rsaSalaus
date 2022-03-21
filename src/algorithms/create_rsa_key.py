from random_prime import get_prime_numbers
from lambda_n import lambda_n
from find_e import find_e

def create_rsa_key(length):
    (p,q) = get_prime_numbers(length)
    n = p*q
    l_n = lambda_n(p,q)
    e = find_e(l_n)
    print(n)
    print(e)

create_rsa_key(1024)
