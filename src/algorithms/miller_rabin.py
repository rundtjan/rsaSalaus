def miller_rabin(n, k):
    #do miller rabin test here, e.g. https://www.youtube.com/watch?v=8i0UnX7Snkc
    
    #https://docs.python.org/2/library/functions.html#pow modular exponentation
    #time complexity O(k log3n) - wikipedia https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
    #write n as 2r·d + 1 with d odd (by factoring out powers of 2 from n − 1)
    #https://www.baeldung.com/cs/miller-rabin-method
    #For a number of b bits, the MILLER-RABIN function requires \mathcal {O} (sb) arithmetic operations and \mathcal {O} (sb ^ {3}) bit operations.
    #https://en.wikipedia.org/wiki/F%C3%BCrer%27s_algorithm#Improved_algorithms
    #https://stackoverflow.com/questions/17063753/can-someone-explain-this-miller-rabin-primality-test-pseudo-code-in-simple-terms
    #https://programmingpraxis.files.wordpress.com/2012/09/primenumbers.pdf

    #Step 1: find n - 1 = 2^k x m
    nMin1 = n - 1
    exp = 0
    temp = 0

    exp, temp = 0, nMin1

    while temp % 2 == 0:
        exp += 1
        temp //= 2

    print(exp, temp)
    print(pow(2,exp) * temp)

    f = 0

    while(True):
        break

miller_rabin(20000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001,3)