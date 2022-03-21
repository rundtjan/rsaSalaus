def gcd(a,b):
    while(b != 0):
        t = b
        b = a % b
        a = t
    return a

print(euclidean(110,1000))