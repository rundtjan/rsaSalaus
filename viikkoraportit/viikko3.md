# Viikko 3

Tällä viikolla tajusin, että RSA-avaimen lisäksi, RSA-salauksessa on erittäin tärkeää, millä tavalla käsittelee viestiä, ennen RSA-laskentaa.
Tuli tutuksi käsite "padding". En tiedä mikä on oikea suomenkielinen termi. Padding tarkoittaa, että lisätään alkuperäiseen viestiin satunnaista ainestoa, joka tekee viestin osittaista dekryptausta ilman avainta melko mahdottomaksi.

RSA-salauksen kanssa käytetään OEAP-nimistä tekniikkaa, joka on todettu hyvin luotettavaksi. Minulla meni suhteettoman paljon aikaa vain eri OEAP-kuvausten tuijottamiseen, ennen kuin alkoi jollain tavalla hahmottua, miten algoritmi toimii, ja mistä voisin lähteä liikkeelle.

Sain tällä viikolla sekä enkryptaus- että enkryptaus-vaiheen valmiiksi. Tämän jälkeen pitäisi katsoa itse sovelluksen käyttöliittymää, refaktorointia yms.

Tunteja käytetty: n. 15
