from lambda_n import gcd

def find_e(l_n):
    if l_n > pow(2,19):
        e = pow(2,16) + 1
    else:
        e = 3
    while(True):
        if gcd(l_n,e) == 1:
            break
        e += 1
    return e
