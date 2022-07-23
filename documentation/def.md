# Määrittelydokumentti 

Aion vertailla eri algoritmeja lyhimpien reittien löytämiseen kahden pisteen välillä painotetussa verkossa aika- sekä tilavaativuuden kannalta. Teen projektin Pythonilla, mutta pystynen vertaisarviointeja varten ymmärtämään myös Javaa, ja pahimmassa tapauksessa JavaScriptiä. Aion tutkia lyhimpiä reittejä verkoissa, todennäköisesti vertailemalla ainakin IDA*- ja Dijkstran algoritmeja keskenään. Ohjelma saa syötteinä kartat (ainakin Moving AI Lab:in artkistoista). 

Aikavaativuuksina Dijkstralla olisi hyvä saada O(n+m log m), jos ja kun oletuksena on ettei ole kahta kaarta samalla lähtö- ja loppusolmua. IDA*:lla voisi ainakin olettaa aikavaativuuden olevan pienempi kuin Dijkstra, vaikka se onkin (todella) vähän A*-algoritmia (O(n+m)), eli ehkä lähintä sukulaistaan hitaampi. 

Kurssi tehdään osana Tietojenkäsittelytieteen kandidaatin tutkintoa, dokumentaatio suomeksi.