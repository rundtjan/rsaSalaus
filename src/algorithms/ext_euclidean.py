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

ext_euclidean(81,57)
ext_euclidean(46,240)
ext_euclidean(61142807745645472107166599236498665523095742862759734512743290005394961942862310160864170140184161856100082346225825540866500367436669761385246038695881247776671814474742882946314936863860935651037249742036466937206505539297480207250386210036736123192885143784058218340707408139396601094952305007978709891160, 65537)
ext_euclidean(780, 17)