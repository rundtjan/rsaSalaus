# Määrittely

## Ohjelmointikielet  

Tulen käyttämään Pythonia tässä projektissa. Olen tottunut käyttämään Pythonia, Javaa ja Nodejs. C++ pystyn kyllä käyttämään, mutten välttämättä lähtisi sitä mielelläni vertaisarvioimaan.

## Algoritmit ja tietorakenteet

Algoritmit ainakin: Miller-Rabin (aikavaaatimus wikipedian mukaan O(k log^3 n), jolla voi testata, että onko satunnaisesti luotu luku alkuluku. Täytyy myös kehittää tehokkaan algoritmin, joka löytää kahden luvun syt:tä - tähän soveltuu hyvin Eukleideen algoritmi. Täytyy myös löytää modulaariaritmetiikan käänteisluku, josta muodostuu yksityinen avain - ja siihen auttaa laajennettu Eukleideen algoritmi.

RSA:ssa käytetään ilmeisesti enkryptaus ja dekryptaus-vaiheissa hieman monimutkaista algoritmia tai tekniikkaa, nimeltään OAEP. Kokeilen, saanko sen toteutettua.

## Ongelmanratkaisu

Tulen tässä projektissa toteuttamaan omaa RSA-salausta. Käyttäjän tulisi pystyä lataamaan omat julkiset ja yksityiset avaimet, ja lähettämään järjestelmässä viestin toiselle käyttäjälle, käyttäen tämän julkista avainta. Käyttäjän pitäisi myös pystyä lukemaan itselleen lähettämiä 
salattuja viestejä.

## Aika- ja tilavaativuudet

Algoritmeista ainakin Miller-Rabin:in aikavaatimus wikipedian mukaan O(k log^3 n) (tai O(k log n log log n) jos käyttää supertehokasta kertolaskun algoritmia, mihin tuskin pystyn). Euclidean algoritmi on aikavaatimukseltaan O(log(min(a, b)), joko on pienempi kuin Miller-Rabin, joten Miller-Rabin määrittelee (tällä hetkellä) sovelluksen aikavaatimusta.

## Lähteet

Ainakin:  
[Wikipedia: RSA, fi](https://fi.wikipedia.org/wiki/RSA)
[Wikipedia: RSA, eng](https://en.wikipedia.org/wiki/RSA_(cryptosystem))
[Suurimman yhteisen tekijän löytäminen](https://brilliant.org/wiki/extended-euclidean-algorithm/)
[Eukleideen algoritmista](https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/the-euclidean-algorithm)
[Laajennettu Eukleideen algoritmi](https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm)
[Wikipedia: Miller-Rabin](https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test)
[Aiheesta montako iteraatiota kannattaa Miller-Rabinissa tehdä](https://stackoverflow.com/questions/6325576/how-many-iterations-of-rabin-miller-should-i-use-for-cryptographic-safe-primes#:~:text=Each%20iteration%20of%20Rabin%2DMiller,that%20the%20number%20is%20composite)
[OAEP](https://en.wikipedia.org/wiki/Optimal_asymmetric_encryption_padding)
[Myös OAEP](https://datatracker.ietf.org/doc/html/rfc2437#section-9.1.1.2)


## Opinto-ohjelma

TKT

## Dokumentaatiossa ja määrittelyssä käytetty kieli  

Suomi
