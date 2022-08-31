# Määrittelydokumentti 

Aion vertailla eri algoritmeja lyhimpien reittien löytämiseen kahden pisteen välillä painotetussa verkossa aika- sekä tilavaativuuden kannalta. Teen projektin Pythonilla, mutta pystynen vertaisarviointeja varten ymmärtämään myös Javaa, ja pahimmassa tapauksessa JavaScriptiä. Aion tutkia lyhimpiä reittejä verkoissa, todennäköisesti vertailemalla ainakin IDA*- ja Dijkstran algoritmeja keskenään. Ohjelma saa syötteinä verkkoja, joita läpikäymällä se suorittaa vertailut. Tavoitteena olisi ainakin käyttää Moving AI Lab:in 2d-karttoja.

Aikavaativuuksina Dijkstralla olisi hyvä saada O(n+m log m), jos ja kun oletuksena on ettei ole kahta kaarta samalla lähtö- ja loppusolmua. IDA*:lla voisi olettaa aikavaativuuden olevan pienempi kuin Dijkstra, vaikka se onkin (todella) vähän A*-algoritmia (O(n+m)), eli ehkä lähintä sukulaistaan hitaampi. Koska Dijkstra on epäspesifimpi (Ei heurestiikkaa), sen tilavaativuus sekä aikavaativuus ovat luonnollisesti x -> y polunetsinnässä tehottomammat.

Kurssi tehdään osana Tietojenkäsittelytieteen kandidaatin tutkintoa, dokumentaatio suomeksi.

Lähteet:

[Tietorakenteet ja algoritmit, Antti Laaksonen](https://www.cs.helsinki.fi/u/ahslaaks/tirakirja/)

Wikipedia: [Dijkstran algoritmi](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm) sekä [IDA*](https://en.wikipedia.org/wiki/Iterative_deepening_A*), myös [täältä](https://www.algorithms-and-technologies.com/iterative_deepening_a_star/python) haettu tietoa.
