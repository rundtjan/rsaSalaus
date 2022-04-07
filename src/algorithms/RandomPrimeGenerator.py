import random

class RandomPrimeGenerator:
    """Luokka, jossa tarvittavat funktiot, jotka tuottavat satunnaisia alkulukuja."""

    def __init__(self, length_of_product) -> None:
        self._length_of_p = length_of_product

    def create(self):
        """Funktio, joka luo kahta sopivankokoista alkulukua.

        Parametrit:
            Kokonaisluku length_of_product - bittipituus, jota toivotaan olevan
            näiden kahden lukujen tulon pituus.

        Palautusarvo:
            Monikko, jossa kokonaisluvut (p,q), jonka tulon bittipituus on
            length_of_product:in määrittämä.
        """
        half_plus_length = self._length_of_p//2 + self._length_of_p//20
        p = self._random_prime(self._min_max(half_plus_length,None))
        q = self._random_prime(self._min_max(self._length_of_p,p))
        n = p * q
        return (n,p,q)

    def _random_prime(self, min_max):
        """Funktio, joka tuottaa satunnaisen (todennäköisen) alkuluvun, tiettyjen rajojen sisällä.

        Parametrit:
            Monikko, jossa kokonaisluvut (minimiraja, maksimiraja).

        Palautusarvo:
            Kokonaisluku, min/max-rajojen sisällä, joka on todennäköisesti alkuluku.
        """

        (min_n, max_n) = min_max
        while True:
            n = random.randrange(min_n,max_n)
            if self._miller_rabin(n,40):
                break
        return n

    @classmethod
    def _min_max(cls, length,first_number):
        """Funktio, joka luo minimi- ja maksimirajan tietyn bittipitoisuuden
            ja mahd. toisen luvun perusteella.

        Parametrit:
            Kokonaisluku length - bittipituus.
            Kokonaisluku first_number - voi myös olla None. Jos käytetty, määrittää sopivat rajat,
            jotta uuden ja tämän luvun tulo olisi sopivaa bittipituutta.

        Palautusarvo:
            Monikko, jossa kokonaisluvut (minimi-, maksimiraja).
        """

        min_n = pow(2, length-1)
        max_n = pow(2, length-1+1)-1
        if first_number:
            min_n //= first_number
            min_n += pow(10, 10)
            max_n //= first_number
        return (min_n,max_n)

    @classmethod
    def _test_for_prime(cls, n, d, r):
        """Funktio, joka kokeilee eri arvoja 'a' vastaan, että onko luku alkuluku.

        Parametrit:
            Kokonaisluku n - luku jota testataan.
            Kokonaisluku d - saadaan Miller-Rabin:in alkupuolesta. Yhtälöstä n-1 = 2^r * d
            Kokonaisluku r - saadaan samasta yhtälöstä kuin d (yllä). Määrittelee,
            montako kierrosta testataan lukua.

        Palautusarvo:
            Boolean - True jos luku näytti alkuluvulta, kun testataan lukua 'a' vastaan.
            False jos selvästi ei ole alkuluku.
        """

        a = random.randrange(2, n-2)
        x = pow(a, d, n)
        if x in(1, n - 1):
            return True
        for _ in range(r-1):
            x = pow(x, 2, n)
            if x == n - 1:
                return True
        return False


    def _miller_rabin(self, n, k):
        """Funktio, joka toteuttaa Miller-Rabin:in algoritmi. Eli testaa,
            onko luku todennäköisesti alkuluku.

        Parametrit:
            Kokonaisluku n - luku jota testataan.
            Kokonaisluku k - positiivinen luku, joka säätää algoritmin tarkkuutta.
            Esim. 40 on sopivan suuri luku. Virhetodennäköisyys 1/(4^k).

        Palautusarvo:
            Boolean: True jos luku on todennäköisesti alkuluku.
            False jos luku varmasti ei ole alkuluku.
        """

        if 0< n <=3:
            return True
        if n % 2 == 0:
            return False

        n_min_1 = n - 1
        r = 0
        d = n_min_1
        result = True

        while d % 2 == 0:
            r += 1
            d //= 2

        for _ in range(k):
            result = self._test_for_prime(n, d, r)
            if result is False:
                break

        return result
