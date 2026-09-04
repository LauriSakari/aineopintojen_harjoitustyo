Opiskelen tietojenkäsittelytiedettä suomeksi. Myös projektin kieli on suomi.
Tehtävän ohjelmoinnissa käytetään Python kieltä.
Voin myös arvioida C, C++ ja Javascript kielillä tehtyjä töitä.

Toteutan työssäni Connect 4 pelin joka käyttää minimax algoritmiä, jota optimoidaan siirtojen järjestämisellä, iteratiivisella syvenemisellä ja pelitilanteen syvyyttä arvioivalla huristiikkafunktiolla.

Käytän työssä myös harjoitustyön tekoälyalustaa graafisena käyttöliittymänä.

Lähteenä tulen käyttämään internetiä ja youtubea. Algoritmien ja käsitteiden opiskeluun tulen varmasi käyttämään apuna myös tekoälyä. 

Aheen ydin on tekoäly joka osaa pelata Connect 4 peliä. Ydin rakennetaan minimax algoritmilla joka käyttää syvyyshakua parhaan madollisen siirron löytämiseen kyseisessä pelitilanteessa, mikäli molemmat pelaajat pelaavat optimaalisesti. Siirtoja on liikaa että kaikki vaihtoehdot voitaisiin käydä läpi tehokkaasti joten algoritmia tehostetaan Alpha-Beta karsinnalla.
Minimax algoritmilla pystytään laskemaan kaikki siirrot ja vaihtoehdot rajatummassa ympäristössä, mutta connect 4 laajuudessa se on liian hidasta. Ongelma jota yritän ratkaista on, miten saan luotua tekoälyn joka osaa pelata järkevästi ja nopeasti, kun kaikkia vaihtoehtoja ei käydä loppuun asti.  

Aikakompleksisuudessa tavoite on päästä mahdollisimman lähelle Alpha-Beta karsinnan teoreettista ${O}(b^{m/2})$ nopeutta, kun minimax algoritmin aikakompleksisuus sellaisenaan on ${O}(b^{m})$.
Teoreettinen nopeus vaatii että siirrot käydään juuri oikeassa järjestyksessä läpi, ja sitä pyritään maksimoimaan muilla optimointimenetelmillä.