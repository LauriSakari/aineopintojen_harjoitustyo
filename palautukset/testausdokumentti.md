Testit voidaan ajaa Pytestiä käyttämällä Poetry virtuaaliympäristössä. Ohjeet:

Käynnistä virtuaaliympäristö ohjelman juurihakemistossa komennolla:
´eval $(poetry env activate)´

Pelkät testit voi suorittaa komennolla:
´pytest´

Kattavuusraportit saa ajamalla testit komennolla:
´coverage run --branch -m pytest src´

Kattavuusraportin näkee komennolla:
´coverage report -m´


Testit:

Nämä testit testaavat että 
Niiden tarkoitus on varmistaa että minimax algoritmi tunnistaa tilanteen jossa peli on päättynyt. 
Tarkistukset tehdään vain niillä linjoilla joita viimeisin lisäys koskee.

Testataan että ohjelma tunnistaa voiton vertikaalisessa rivissä, johon pelinappula on laitettu:
test_check_vertical_recognizes_win(self)
Testataan että ohjelma tunnistaa voiton horisontaalisessa rivissä, johon pelinappula on laitettu:
test_check_horizontal_recognizes_win(self)
Testataan että ohjelma tunnistaa voiton ylä-vasemmalta ala-oikelle diagonaalisessa rivissä, johon pelinappula on laitettu:
test_check_diagonal_recognizes_win(self)
Testataan että ohjelma tunnistaa voiton ala-vasemmalta ylä-oikelle diagonaalisessa rivissä, johon pelinappula on laitettu:
test_check_other_diagonal_recognizes_win(self)

Testataan että is_terminal funktio, joka käyttää em. funktioita voitontarkistukseen, tunnistaa voiton:
test_is_terminalFunction(self):

Testataan että tekoäly osaa blokata vain toisesta päästä avoimen kolmen suoran:
test_ai_can_block(self):

Testataan että tekoälyn valitsee voiton eikä blokkaa jos mahdollista:
test_ai_chooses_to_win_not_block(self):
test_ai_chooses_to_win_not_block_2(self):

Testataan että tekoäly aloittaa keskeltä:
test_ai_chooses_to_open_in_the_middle(self):

Testataan että tekoäly osaa blokata voittosuoran joka keskeltä vajaa:
test_ai_blocks_when_slot_in_the_middle(self):

Testataan että tekoäly blokkaa avoimen kahden suoran:
test_ai_blocks_open_two(self):

Testataan että algoritmi osaa käsitellä täyden pelilaudan:
test_algorithm_handles_full_board(self):

Testataan että täysi sarake sivuutetaan agoritmissä:
test_full_col_is_recognized_in_minimax(self):

Testataan että timeout error nostetaan kun aika on loppunut:
test_timeout_error_is_raised(self)
