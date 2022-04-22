from hashlib import sha512
import random

class RsaService:
    '''Luokka, jossa tarvittavat funktiot, jotka toteuttavat rsa-salauksen ja dekryptauksen.'''

    @classmethod
    def _byte_to_bin_string(cls, bytestring):
        '''Funktio, joka muuntaa byte-jonon binäärimerkkijonoksi

        Parametrit:
            bytes - b''

        Palautusarvo - merkkijono, jossa bytes binäärisessä esitysmuodossa.

        '''
        b_m = ''
        for byte in list(bytestring):
            b = format(byte, 'b')
            ex = 8 - len(b)
            if ex > 0:
                z = '0'*ex
                b = z + b
            b_m += b
        return b_m

    def _string_to_bin(self, m):
        '''Funktio, joka muuntaa merkkijonon binääriseksi.

        Parametrit:
            m - merkkijono.

        Palautusarvo:
            Merkkijono, vastaa sisällöltään parametrin merkkijono, mutta
            jokainen merkki käännetty 8-merkkiseksi binääriseksi luvuksi.
        '''
        m = m.encode('utf8')
        return self._byte_to_bin_string(m)

    def _mgf1(self, db, length):
        '''Funktio, suoraan OAEP:n määrittelystä.

        Parametrit:
            db - datablokki binäärisessä esitysmuodossa, merkkijono
            length - palautusarvon toivottu pituus

        Palautusarvo:
            Merkkijono, hash-funktion tulos, binäärisessä esitysmuodossa.
        '''
        counter = 0
        oct_str = str(db).encode('utf-8')
        output = b''
        while len(output) < length // 8:
            c_b = str(counter).encode('utf-8')
            output += sha512(oct_str+c_b).digest()
            counter += 1
        return self._byte_to_bin_string(output[:length//8])

    @classmethod
    def _xor(cls, a, b):
        '''Funktio, joka tuottaa xor-tuloksen kahdesta parametrista.

        Parametrit:
            a - merkkijono, sisältönä binäärinen luku.
            b - merkkijono, sisältönä binäärinen luku.

        Palautusarvo:
            c - merkkijono, sisältönä xor-binäärinen tulos a ja b:sta.
        '''
        c = ''
        assert len(a) == len(b), "a and b should be of same length"
        for i in range(0,len(a)):
            if a[i] == b[i]:
                c += '0'
            else:
                c += '1'
        return c

    def _oaep(self, message, seed, db_len):
        '''Funktio, joka hoitaa oaep-padding:

        Parametrit:
            message - alkuperäinen viesti merkkijonona, binääristä dataa.
            seed - satunnainen viestiosuus, "padding", merkkijono, binääristä dataa.
            db_len - algoritmin datablokin pituus

        Palautusarvo:
            oaep_m - viestiosuuden ja satunnaisen viestiosuuden yhdistelmä, merkkijono,
            binääristä dataa.
        '''
        db = message + '0' * (db_len - len(message))
        db_mask = self._mgf1(seed, db_len)
        db = self._xor(db, db_mask)
        seed_mask = self._mgf1(db, len(seed))
        seed = self._xor(seed, seed_mask)
        return db + seed

    @classmethod
    def _rsa(cls, padded, e, n):
        '''Funktio, joka tekee itse rsa-laskelman.

        Parametrit:
            padded - salattava viesti oaep-käsittelyn jälkeen.
            e - julkisen avaimen e-osuus
            n - julkisen avaimen n-osuus
        '''
        return pow(padded, e, n)

    @classmethod
    def _bit_length_of(cls,i):
        '''Funktio, joka tarkistaa kokonaisluvun bittipituus.

        Parametrit:
            i - kokonaisluku.

        Palautusarvo:
            kokonaisluku, i:n bittipituus.
        '''
        return len(bin(i)[2:])

    @classmethod
    def _create_random_seed(cls,length):
        '''Funktio, joka tuottaa satunnaisen viestin osuus, oaep:n tarvitsema seed.

        Parametrit:
            length - kokonaisluku, seedin pituus.

        Palautusarvo:
            seed - merkkijono, binääristä dataa.
        '''
        seed = ''
        for _ in range(length):
            seed += str(random.randint(0,1))
        return seed

    @classmethod
    def _bin_string_to_int(cls,b_s):
        '''Funktio, joka muuntaa binäärinen merkkijono kokonaisluvuksi.

        Parametrit:
            b_s - merkkijono, binääristä dataa.

        Palauttaa:
            kokonaisluvun.
        '''
        return int(b_s, 2)

    def encrypt(self, message, n, e):
        '''Funktio, joka tuottaa rsa-salatun viestin.

        Parametrit:
            message - alkuperäinen viesti, merkkijono.
            n - kokonaisluku, julkisen avaimen n-osuus.
            e - kokonaisluku, julkisen avaimen e-osuus.

        Palautusarvo:
            Merkkijono, binääristä dataa, salattu viesti.

        '''
        block_array = self._split_into_blocks(message, n)
        encrypted = ''
        for i in range(0, len(block_array)):
            encrypted += f'{self._rsa_encrypt_block(block_array[i], n, e)}#'
        return encrypted

    def decrypt(self, message, n, d):
        '''Funktio, joka poistaa salauksen viestistä.

        Parametrit:
            message - salattu viesti, merkkijono, binääristä dataa.
            n - kokonaisluku, julkisen avaimen n-osuus.
            d - kokonaisluku, yksityisen avaimen d-osuus.

        Palautusarvo:
            merkkijono, alkuperäinen viesti ilman salausta.
        '''
        block_array = message.split('#')
        decrypted = ''
        if len(block_array) == 1:
            try:
                return self._rsa_decrypt_block(block_array[0], n, d)
            except:
                raise ValueError
        for i in range(0, len(block_array)-1):
            decrypted += f'{self._rsa_decrypt_block(block_array[i], n, d)}'
        return decrypted

    @classmethod
    def check_valid_decrypt_message(cls,message):
        sum = message.count('0') + message.count('1') + message.count('#')
        if sum == len(message):
            return True
        return False

    def _split_into_blocks(self, message, n):
        '''Funktio, joka jakaa viestin sopivankokoisiin osiin.

        Parametrit:
            message - merkkijono, alkuperäinen viesti.
            n - kokonaisluku, julkisen avaimen n-osuus.

        Palautusarvo:
            Lista - sisältää merkkijonoja binääristä dataa,
                    viesti muunneltu sopivankokoisiin osiin.
        '''
        result = []
        blocksize = self._bit_length_of(n) - 16 - self._bit_length_of(n) // 4
        assert blocksize % 8 == 0, "n should be divisible by 8"
        message = self._string_to_bin(message)
        if len(message) < blocksize:
            return [message]
        for i in range(0, len(message), blocksize):
            block = message[i: i+blocksize]
            result.append(block)
        return result

    def _rsa_encrypt_block(self, message, n, e):
        '''Funktio, joka tuottaa rsa-salauksen oaep-padding-tekniikan avulla.

        Parametrit:
            message - alkuperäinen viestin sopivan kokoinen osa merkkijonona, binääristä dataa.
            n - julkisen avaimen n-osuus
            e - julkisen avaimen e-osuus

        Palautusarvo:
            Merkkijonona, binääristä dataa, salatun viestin osa.
        '''
        n_len = self._bit_length_of(n)
        seed = self._create_random_seed(n_len // 4)
        assert len(seed) % 8 == 0, "seed should be divisible by 8"
        db_len = n_len -8 - len(seed)
        assert len(message) < (n_len - 8 - len(seed)), "the message is too long"
        padded = self._oaep(message, seed, db_len)
        pad_m_int = self._bin_string_to_int(padded)
        rsa_m = self._rsa(pad_m_int, e, n)
        rsa_m = bin(rsa_m)[2:]
        return rsa_m

    @classmethod
    def _rsa_reverse(cls, message, n, d):
        return pow(message, d, n)

    def _reverse_oaep(self, db, seed):
        '''Funktio, joka käyttää oaep-padding-toimintoa toisinpäin.

        Parametrit:
            db - merkkijono, oaep-käsitelty viestiosuus, binääristä dataa
            seed - merkkijono, oaep-käsitelty satunnainen osuus, binääristä dataa

        Palautusarvo:
            db - merkkijono, viestiosuus ilman oaep-käsittelyä, binääristä dataa
        '''
        seed_mask = self._mgf1(db, len(seed))
        seed = self._xor(seed, seed_mask)
        db_mask = self._mgf1(seed, len(db))
        db = self._xor(db, db_mask)
        return db

    def _correct_length(self, message, n):
        '''Funktio, joka lisää kryptattuun viestiin tarvittaessa etunollia.

        Parametrit:
            message - merkkijono, binääristä dataa
            n - kokonaisluku, jonka bittipituus määrittelee viestin pituutta.

        Palautusarvo:
            message - merkkijono, oikean pituinen.
        '''
        correct_len = self._bit_length_of(n) - 8
        if correct_len - len(message) > 0:
            message = ('0'*(correct_len-len(message))) + message
        return message

    def _split_into_db_and_seed(self, message, n):
        '''Funktio, joka löytää kryptatusta viestistä datablokin ja seed:in.

        Parametrit:
            message - merkkijono.
            n - kokonaisluku.

        Palautusarvo:
            (db, seed) - tuple, datablokki ja seed.
        '''
        n_len = self._bit_length_of(n)
        seed_len = n_len // 4
        seed = message[n_len-8-seed_len:]
        db = message[:n_len-8-seed_len]
        return (db, seed)

    @classmethod
    def _from_bin_to_text_string(cls, db):
        '''Funktio, joka muuntaa merkkijonon binääristä dataa tekstimuotoon.

        Parametrit:
            db - merkkijono, binääristä dataa.

        Palautusarvot:
            message - merkkijono, tekstisisältöä.
        '''
        byte_db = bytes(int(db[i: i+8], 2) for i in range(0, len(db), 8))
        message = byte_db.decode('utf-8')
        return message.rstrip('\x00')

    def _rsa_decrypt_block(self, message, n, d):
        '''Funktio, joka poistaa salauksen viestistä.

        Parametrit:
            message - merkkijono, binääristä dataa, kryptattu viesti.
            n - kokonaisluku, osa julkista ja yksityistä avainta.
            d - kokonaisluku, osa yksityistä avainta.

        Palautusarvo:
            message - merkkijono, alkuperäinen/dekryptattu viesti.
        '''
        message = self._bin_string_to_int(message)
        message = self._rsa_reverse(message, n , d)
        message = bin(message)[2:]
        message = self._correct_length(message, n)
        (db, seed) = self._split_into_db_and_seed(message, n)
        db = self._reverse_oaep(db, seed)
        message = self._from_bin_to_text_string(db)
        return message
