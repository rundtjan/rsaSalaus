import random

def test_for_prime(n, d, r):
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

miller_rabin(82589931,3)