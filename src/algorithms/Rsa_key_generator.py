from .Random_prime_generator import Random_prime_generator
from .Lambda_n_generator import Lambda_n_generator

class Rsa_key_generator:

    def __init__(self, length) -> None:
        self._length = length
        self._prime_gen = Random_prime_generator(length)
        self._lambda_n_gen = Lambda_n_generator()

    def create(self):
        """Funktio, joka tuottaa rsa-avaimen.

        Parametrit:
            Self.

        Palautusarvo:
            Monikko, jossa avaimeen kuuluvat osiot n, e ja d.
        """
        (n,p,q) = self._prime_gen.create()
        l_n = self._lambda_n_gen.create(p,q)
        e = self._find_e(l_n)
        d = self._ext_euclidean(l_n, e)
        return (n,e,d)

    def _find_e(self,l_n):
        """Funktio, joka löytää rsa-avaimen ns. e-arvo.

        Parametrit:
            Kokonaisluku, lambda(n).

        Palautusarvo:
            Kokonaisluku, e-arvom lambda(n):n kanssa keskenään jaoton.
        """

        if l_n > pow(2,19):
            e = pow(2,16) + 1
        else:
            e = 3
        while True:
            if self._lambda_n_gen.gcd(l_n,e) == 1:
              break
            e += 1
        return e

    def _ext_euclidean(self, lambda_n, e):
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

        if old_t < 0:
            old_t += lambda_n

        if old_t > lambda_n:
            old_t -= lambda_n

        return old_t
