Ohjelma koostuu kurssilla suositellun graafisen pelipohjan tarjoamasta main.py tiedostosta ja varsinaisen minimax algoritmin sisältävästä minimax.py tiedostosta.
Main.py:ssä annetaan algoritmin käyttämät syvyydet ja aikarajat.
Siellä pidetään kirjaa pelitilanteesta ja kumpi pelaaja on vuorossa ja varsinainen siirto tapahtuu myös siellä. Graafinen käyttöliittymä antaa PLAY tai MOVE viestejä ohjelmalle. PLAY käynnistää tekoälyn tekemän siirron ja MOVE tekee siirron suoraan kyseiseen sarakkeeseen.

PLAY viesti aiheuttaa minimax.py:ssä olevan calculate_next_move() funktion kutsun, ja käynnistää minimax algoritmin.

Calculate_next_move käynnistää ajanoton ja iteratiivisen syvenemisen, jota suoritetaan kunnes aikaraja tai toivottu syvyys on saavutettu. Jokaisen syvyyden jälkeen saavutettu paras siirto tallennetaan, jolloin seuraava syvyys voidaan aloittaa suoraan parhaalla siirrolla. Tämä tehostaa alpha beta karsinnan vaikutusta seuraavassa syvyydessä.

Itse minimax funktio tarkistaa onko aikaraja ylitetty, tarkistaa onko tila pelin päättävä ja ollaanko saavutettu maksimisyvyys.
Mikäli ei ole niin aloitetaan siirtojen läpikäynti prioriteettijärjestyksessä.
Kun ollaan maksimisyvyydessa niin suoritetaan heuristinen arvio sen hetkisestä pelitilanteesta ja palautetaan se.

Saavutettu aikavaatimus lähestyy tavoitetta $ O = \sqrt{b^d} $ joka olisi optimaalinen tilanne.
Algoritmissa on käytösssä apha beta karsinta ja sitä tehostetaan edelleen siirtojen järjestämisellä ja iteratiivisella syvenemisellä.

Parannusehdotuksia olisi koodin refaktorointi ja ysinkertaistaminen. Joitain tarkistuksia tehdään ehkä useampaan kertaan yms. Siirtojen optimointi on tällä hetkellä melko yksinkertainen. Heuristiikkaa voisi optimoida varmasti paljonkin. Testejä voisi varmasti myös olla enemmän.
Myös graafisen pohjan käyttöönotto oli mielesni melko hankalaa ja vei alussa pajon aikaa. Jos tekisin alusta, tekisin varmaan vaan oman yksinkertaisen terminaalissa pelattavan pohjan.

Pääasiallisina lähteinä on käytetty wikipedian artikkeleita:
https://en.wikipedia.org/wiki/Minimax
https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning

Tekoälyä on käytetty lähinnä joidenkin bugien selvittelyissä ja esim funktioiden kommentoinnissa ja käsitteiden opiskelussa.
