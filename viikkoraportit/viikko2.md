# Viikko 2

Tällä viikolla sain suuren osan RSA:n perusalgoritmeista toteutettua ja vieläkin testattua. 

Miller-Rabin:iin toteuttamiseen meni jonkin verran aikaa, kun siitä löytyi hieman eri selityksiä netistä, joista osa vaikutti eroavan aika paljon wikipedian versiosta. Wikipedian pseudokoodissa oli se ongelma, etten täysin ymmärtänyt, miten "continue" algoritmin silmukassa oikein toimii ja tuottaa järkevän tuloksen. Kuitenkin, vertaamalla muihin lähteisiin, tajusin sitten, miten pseudokoodi toimi, ja sain sen käännettyä pythoniksi.

Otin käyttöön sekä pytest:in että pylint:in, mutta pylintin tulos on vielä suht kehno.

Aloitin myös koodin dokumentaation, docstringien muodossa.

Jotta näkyisi hieman edistystä myös päällepäin, laitoin käyttöliittymän juurisivun näyttämään niitä RSA-avaimen komponentteja, mitkä olen tähän asti saanut aikaiseksi.

Tunteja käytetty: n. 8
