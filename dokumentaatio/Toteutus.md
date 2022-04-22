# Toteutuskuvaus

## Ohjelman yleisrakenne

Sovellus on perus-Flask-sovelluksen muodossa. Suoraan /src-kansiosta löytyy index, app ja routes joissa verkkosovelluksen perusominaisuudet.
Sivujen html-pohjat löytyvät kansiosta /templates.
RSA-salaukseen liittyvät luokat löytyvät kansiosta /rsa_service. Koodi on eritelty sopiviin luokkiin/kokonaisuuksiin.
Testit löytyvät kansiosta /tests.

## Aika- ja tilavaativuudet  

RSA-avainten luonti suurin aikavaativuus on algoritmilla Miller-Rabin, jonka aikavaativuus O(k log^3 n) (tarkempi analyysi tulossa).
RSA-salauksen aikavaativuus xx
RSA-dekryptauksen aikavaativuus xx

Tilavaativuudet: tulossa.

## Työn mahdolliset puutteet ja parannusehdotukset

Tällä hetkellä avaimen pituus kovakoodattu, voisi olla käyttäjän valinta (tai ainakin voisi löytyä eri vaihtoehtoja).

## Lähteet
  
[Wikipedia: RSA, fi](https://fi.wikipedia.org/wiki/RSA)  
[Wikipedia: RSA, eng](https://en.wikipedia.org/wiki/RSA_(cryptosystem))  
[Suurimman yhteisen tekijän löytäminen](https://brilliant.org/wiki/extended-euclidean-algorithm/)  
[Eukleideen algoritmista](https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/the-euclidean-algorithm)  
[Laajennettu Eukleideen algoritmi](https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm)  
[Wikipedia: Miller-Rabin](https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test)  
[Aiheesta montako iteraatiota kannattaa Miller-Rabinissa tehdä](https://stackoverflow.com/questions/6325576/how-many-iterations-of-rabin-miller-should-i-use-for-cryptographic-safe-primes#:~:text=Each%20iteration%20of%20Rabin%2DMiller,that%20the%20number%20is%20composite)  
[OAEP](https://en.wikipedia.org/wiki/Optimal_asymmetric_encryption_padding)  
[Myös OAEP](https://datatracker.ietf.org/doc/html/rfc2437#section-9.1.1.2)  
[Vielä OAEP](https://www.inf.pucrs.br/~calazans/graduate/TPVLSI_I/RSA-oaep_spec.pdf)  
[OAEP:n Mask Function](https://en.wikipedia.org/wiki/Mask_generation_function)
