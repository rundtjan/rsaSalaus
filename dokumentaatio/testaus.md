# Testaus

## Testauskattavuus

Testikattavuus on tällä hetkellä 88%. Raportti löytyy [täältä](https://app.codecov.io/gh/rundtjan/rsaSalaus).

## Miten on testattu

Yksikkötestit on tässä hyvin ratkaisevassa asemassa, kun sovelluksen logiikka on hyvin suoraviivainen: sen pitää tuottaa oikeanmuotoisia avaimia, ja näillä avaimilla sen pitää sekä salata että purkaa salauksen viesteistä.

Yksikkötestien lisäksi, on tehty paljon manuaalisia end2end-testejä, tarkistaakseen, että sovellus tuottaa halutun tuloksen eri syötteillä.

Syötteenä on käytetty eripituisia merkkijonoja. On myös testattu, että sovellus pystyy käsittelemään erikoismerkkejä.

## Testien toistettavuus

Testit voidaan ajaa omalla koneella. Esim. sovelluksen juuressa:
```bash
poetry run pytest src
```

## Suorituskyvyn testaaminen

### Avaimen luonnin kesto 
Testaus-endpoint löytyy verkkosovellukselta polusta /timecheck.  

Tulokset (100 kpl avaimen luontia testattu):
| Mitattu | Sekuntia |
| ------ | ------- |
| Keskiarvo | 0,448 |  
| Mediaani | 0,384 |  
| Keskihajonta | 0,302 |  
| Maksimiarvo | 1,723 |  
| Minimiarvo | 0,091 |

### Viestin salauksen kesto 
Testaus-endpoint löytyy verkkosovellukselta polusta /timecheck_encrypt.  
Viestinä käytetty Grandmaster Flashin riimi: "It's like a jungle sometimes, it makes me wonder how I keep from going under (ha ha ha ha ha)".

Tulokset (100 kpl viestin salausta testattu):
| Mitattu | Sekuntia |
| ------ | ------- |
| Keskiarvo | 0,000887 |  
| Mediaani | 0,000782 |  
| Keskihajonta | 0,000216 |  
| Maksimiarvo | 0,002004 |  
| Minimiarvo | 0,000748 |

### Viestin salauksen purun kesto 
Testaus-endpoint löytyy verkkosovellukselta polusta /timecheck_decrypt.  
Viestinä käytetty Grandmaster Flashin riimi: "It's like a jungle sometimes, it makes me wonder how I keep from going under (ha ha ha ha ha)".

Tulokset (100 kpl viestin salauksen purkua testattu):
| Mitattu | Sekuntia |
| ------ | ------- |
| Keskiarvo | 0,005588 |  
| Mediaani | 0,005467 |  
| Keskihajonta | 0,000368 |  
| Maksimiarvo | 0,006873 |  
| Minimiarvo | 0,005127 |
