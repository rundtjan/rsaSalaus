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

Ei ole vielä mitattu, paljonko sovelluksen eri toiminnot vievät aikaa.
