# Hrali jste nekdy mini-hru hackovani ve Fallout 3?  Toto je moje levna kopie^^
# Jestlize ne, tak pravidla jsou jednoducha
# Konzole vypise nekolik slov a nahodne znaky.
# Vasim ukolem je zjistit, ktere z techto slov je tajne heslo. Mate 4 pokusy
# Program vam bude napovidat, zda jste vyplnili spravne znaky

import random
import time

class Generator:


    slova_01 = ["RAGS", "VAST", "BODY", "LAYS", "SOUL", "FEED", "TALE",
                "MAIN", "TAKE", "SIGN", "LATE", "FEAR", "NOTE", "FALL"]

    slova_02 = ["RAIDER", "SWORDS", "ALLOWS", "TAVERN", "SHOVEL", "HOVELS",
                "REMIND", "COVERS", "RACREE", "SUPPLY", "ALMOST", "SCORCH"]

    slova_03 = ["BREAKING", "CREATING", "GUARDIAN", "DOCUMENT", "AGREEING",
                "GREENERY", "DYNAMITE", "FACILITY", "TRIPPING", "STEMMING", "LOYALIST",
                "RUSTLING", "CHAMBERS", "BREAKERS", "BRAWLING", "THINKING", "CLEANING"]

    znaky = []

    finalni_seznam = []

    heslo = None

    def vytvoreni_seznamu(self):

        # vytvoreni nahodnych znaku pomoci ASCII
        for x in range(40):
            znak = chr(random.randint(33,64))
            if znak.isdigit():
                pass
            elif znak in self.znaky:
                pass
            else:
                self.znaky.append(znak)


        # vyber jednoho seznamu s hesly a jeho prirazeni do promenne vybrany_seznam
        vyber_slov = random.randint(1,4)
        if vyber_slov == 1:
            vybrany_seznam = self.slova_01
        elif vyber_slov ==2:
            vybrany_seznam = self.slova_03
        else:
            vybrany_seznam = self.slova_02


        # smichani znaku a slovu do promennne finalni_seznam
        for slovo in vybrany_seznam:
            self.finalni_seznam.append(slovo)

        for q in range(5):
            for znak in self.znaky:
                self.finalni_seznam.append(znak)

        random.shuffle(self.finalni_seznam)

        # vytvoreni hesla z jednoho nahodneho slova
        self.heslo = vybrany_seznam[random.randint(0, len(vybrany_seznam)-1)]


    def vypsani_seznamu(self):


        for i, x in enumerate(self.finalni_seznam):
            if i > 0 and i % 20 == 0:
                print("")
            print(x + "_", end="")
            time.sleep(0.02)



    def zadej_heslo(self):

        pocet_pokusu = 4
        while pocet_pokusu > 0:
            try:
                print("\n")
                zadane_heslo = input("Zadejte heslo: ")
                zadane_heslo = zadane_heslo.upper()
                if zadane_heslo != self.heslo and pocet_pokusu == 1:
                    print("TERMINAL UZAMCEN. PROSIM KONTAKTUJTE ADMINISTRATORA")
                    break

                elif zadane_heslo != self.heslo and pocet_pokusu > 1:
                    pocet_pokusu -= 1
                    shodne_znaky = 0
                    index = 0
                    for znak in zadane_heslo:
                        if znak == self.heslo[index]:
                            shodne_znaky += 1
                        index += 1
                    print(f"SHODNE ZNAKY: {shodne_znaky}/{len(self.heslo)}")
                    print(f"CHYBNE ZADANE HESLO. ZBYVAJICI POCET POKUSU: {pocet_pokusu}")
                else:
                    print("SPRAVNE ZADANE HESLO")
                    print("Terminal odemcen.")
                    print("*****************")
                    break
            except IndexError:
                print(f"CHYBNE ZADANE HESLO. ZBYVAJICI POCET POKUSU: {pocet_pokusu}")


    def spusteni(self):

        self.vytvoreni_seznamu()
        self.vypsani_seznamu()
        self.zadej_heslo()
