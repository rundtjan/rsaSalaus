def ext_euclidean(lambda_n, e):
    """Funktio, joka tuottaa modulaariaritmetiikan käänteisluvun.
    
    Parametrit:
        lambda_n - kokonaisluku.
        e - kokonaisluku
        
    Palautusarvo:
        old_t - positiivinen kokonaisuluku, joka vastaa y:tä, yhtälössä:
        x * lambda_n + y * e = gcd(lambda_n, e) = 1
    """
    (old_r, r) = (lambda_n, e)
    (old_s, s) = (1, 0)
    (old_t, t) = (0, 1)

    while r != 0:
        quo = old_r // r
        (old_r, r) = (r, old_r - quo * r)
        (old_s, s) = (s, old_s - quo * s)
        (old_t, t) = (t, old_t - quo * t)

    print(old_s, old_t)

    if old_t < 0:
        old_t += lambda_n

    if old_t > lambda_n:
        old_t -= lambda_n
    
    print(old_t)

    return old_t
