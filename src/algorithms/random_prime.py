import random
from miller_rabin import miller_rabin

def dec_from_bin(bin, length):
    dec = 0
    for i in range(length):
        dec += bin[i] * pow(2, i)
    print(dec)
    return dec

def random_prime(length):   
    
    for _ in range(4):
        to_test = [0] * length
        to_test[0] = 1
        to_test[length-1] = 1
        for i in range(1, length-1):
            to_test[i] = random.randint(0,1)
        print(to_test)
        to_test = dec_from_bin(to_test, length)
        #print(miller_rabin(to_test, 20))
    

random_prime(1026)