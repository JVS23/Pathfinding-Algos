# Testausdokumentti

## Testaus

Unittestit voi käydä läpi "src"-directoryssä komennolla "python -m unittest".
Unittesteillä on testattu algoritmien toiminta vertaamalla generoitujen verkkojen läpikäynnin tuloksia
itserakennetulla algoritmilla vs NetworkX:n tarjoamalla algoritmillä. Testit tarkastavat, saavatko algoritmit samat tulokset samassa verkossa. Näin ollen oman algoritmin täytyy toimia oikein, sillä suurissa verkoissa oikeaa tulosta ei saa sattumanvaraisesti.

## Test-coverage

Coverage report:

![Covreport](covreport.jpg)
