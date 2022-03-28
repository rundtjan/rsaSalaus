def encrypt(m, n, e):
    #m = int.from_bytes(m.encode('utf-8'), byteorder='big')
    #print(m)
    m = m.encode('utf8')
    print(m)
    print(list(m))
    len_m = len(m)*8
    len_n = 1024
    print(len_n - len_m)
    c = 0
    # c = m^e mod n
    # c = pow(m,e,n)
    return c

encrypt('hello world, how wonderful it is to be alive, is it not?', 123412341234123412341241241234123412, e = pow(2,16) + 1)