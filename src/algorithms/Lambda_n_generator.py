class Lambda_n_generator:

    def create(self,p,q):
        """Funktio, joka löytää λ(n) - luku, jota tarvitaan rsa-algoritmissa.

        Parametrit:
            RSA-algoritmin alkuluvut p ja q.

        Palautusarvo:
            Kokonaisluku, eli λ(n).
        """

        return self._lcm(p-1,q-1)

    def _lcm(self,a,b):
        """Funktio, joka löytää kahden luvun pienin yhteinen jaettava.

        Parametrit:
            Kaksi kokonaislukua.

        Palautusarvo:
            Kokonaisluku, joka on kahden luvun pienin yhteinen jaettava.
        """
        return a*b//self.gcd(a,b)

    def gcd(self,a,b):
        """Funktio, joka löytää kahden luvun suurin yhteinen tekijä.

        Parametrit:
            Kaksi kokonaislukua, joiden syt halutaan löytää.

        Palautusarvo:
            Kokonaisluku, eli suurin yhteinen tekijä.
        """

        while b != 0:
            t = b
            b = a % b
            a = t
        return a