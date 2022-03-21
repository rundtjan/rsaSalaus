def gcd(a,b):
    while(b != 0):
        t = b
        b = a % b
        a = t
    return a

def lcm(a,b):
    return a*b/gcd(a,b)

def lambda_n(p,q):
    return lcm(p-1,q-1)