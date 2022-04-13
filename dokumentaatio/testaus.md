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

Avaimen luonnin kesto testattu. Testaus-endpoint löytyy verkkosovellukselta polusta /timecheck.  

Tulokset (100 kpl avaimen luontia testattua):
| Mitattu | Sekunnit |
| ------ | ------- |
| Keskiarvo | 0,448 |  
| Mediaani | 0,384 |  
| Keskihajonta | 0,302 |  
| Maksimiarvo | 1,723 |  
| Minimiarvo | 0,091 |
