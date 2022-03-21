import random
import time
from miller_rabin import miller_rabin

def random_prime(min_max):
#number of iterations from https://stackoverflow.com/questions/6325576/how-many-iterations-of-rabin-miller-should-i-use-for-cryptographic-safe-primes#:~:text=Each%20iteration%20of%20Rabin%2DMiller,that%20the%20number%20is%20composite.
    (min, max) = min_max
    while(True):
        n = random.randrange(min,max)
        if miller_rabin(n,40): break
    return n

def min_max(length,first_number):
    min = pow(2, length)
    max = pow(2, length+1)-1
    if first_number:
        min //= first_number
        min += pow(10, 10)
        max //= first_number
    return (min,max)

def get_prime_numbers(length_of_product):
    half_plus_length = length_of_product//2 + length_of_product//20
    p = random_prime(min_max(half_plus_length,None))
    q = random_prime(min_max(length_of_product,p))
    return (p,q)
