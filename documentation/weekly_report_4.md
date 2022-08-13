# Viikon 4 raportti

Sain kuin sainkin visualisoinnin hoidettua suht järkevästi NetworkX-libraryllä, vaikka sen implementointi onkin vielä hieman vaiheessa, joten voin jatkaa projektia kuten oli tarkoituskin. Visualisoinnin ideana on pyöräyttää sama verkko nx:n kautta vain visualisoinnin vuoksi, ja riittävällä testauksella varmistaa että tulos on kuitenkin sama kuin omissa algoritmeissäni. Projektin ydintoiminta alkaa pikkuhiljaa olemaan kasassa, ja vihdoin kunnollisen testauksenkin voi näin ollen aloittaa, vaikka se näin hieman myöhässä tuleekin. En jostain syystä keksinyt millään ratkaisua miten saada Dijkstra päivittämään polkua, ja sen ongelman kanssa tulikin suurin osa ajasta taisteltua. Syynä luultavasti aika heikosti rakennettu pohja graph-classille sekä itse algoritmille, pitää katsoa ensiviikolla. Koodi tällä hetkellä aikamoista spagettia kiireiden takia, joten yiritin vain saada tähän palautukseen edes jotain toimintakykyistä. Olettaisin että saan kuitenkin kirittyä kahden viikon aikana projektin edes palautuskelpoiseksi, sillä ydintoiminta ei kaipaa enää (kovin) paljoa viilausta, ja testit, tilastointi yms siistiminen sujunee ongelmitta.
Ohjaajan kanssa jutustelu voisi olla kuitenkin kohtuullisen hyvä idea, joten olen varmaankin ensiviikolla yhteyksissä.





| Pvm | Tunnit | Aihe |
| ---         |     ---      |  --- |
| 10.8   | 5     | NetworkX:n implementointi, verkkojen visualisointi |
| 12.8   | 6    | IDA*:n alku, Dijkstran parantelu |
| 13.8   | 3   | IDA* lähes valmis |
| Yht.    | 14     |    |
