"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Jana Barotová
email: jana.barotova@seznam.cz
"""

import random
import time

UVODNI_RADKY = [
    "Hi there!",
    "I've generated a random 4 digit number for you.",
    "Let's play a bulls and cows game."
]
DELKA_CARY = max(len(radek) for radek in UVODNI_RADKY)

def print_cara():
    print("-" * DELKA_CARY)

def vypis_blok(radky):
    print_cara()
    for radek in radky:
        print(radek)
    print_cara()

def pozdrav():
    vypis_blok(UVODNI_RADKY)

def generuj_tajne_cislo():
    vsechny_cislice = list("123456789")
    prvni_cislice = random.choice(vsechny_cislice)
    vsechny_cislice.remove(prvni_cislice)
    vsechny_cislice.append('0')
    dalsi_tri = random.sample(vsechny_cislice, 3)
    tajne_cislo = prvni_cislice + ''.join(dalsi_tri)
    return tajne_cislo

def validuj_tip(tip):
    if not tip.isdigit():
        print("Chyba: Zadej pouze číslice.")
        return False
    if len(tip) != 4:
        print("Chyba: Číslo musí mít přesně 4 číslice.")
        return False
    if tip[0] == '0':
        print("Chyba: Číslo nesmí začínat nulou.")
        return False
    if len(set(tip)) != 4:
        print("Chyba: Číslice se nesmí opakovat.")
        return False
    return True

def vyhodnot_tip(tip, tajne):
    bulls = sum(1 for i in range(4) if tip[i] == tajne[i])
    cows = sum(1 for i in range(4) if tip[i] in tajne and tip[i] != tajne[i])
    return bulls, cows

def vypis_vysledek(bulls, cows):
    bull_str = "bull" if bulls == 1 else "bulls"
    cow_str = "cow" if cows == 1 else "cows"
    print(f"{bulls} {bull_str}, {cows} {cow_str}")
    print_cara()

def hlavni():
    pozdrav()
    tajne = generuj_tajne_cislo()
    pokusy = 0
    start_cas = time.time()

    while True:
        print("Enter a number:")
        print_cara()
        tip = input(">>> ")
        if not validuj_tip(tip):
            continue

        pokusy += 1
        bulls, cows = vyhodnot_tip(tip, tajne)

        if bulls == 4:
            cas = round(time.time() - start_cas, 2)
            print("Correct, you've guessed the right number")
            print(f"in {pokusy} {'guess' if pokusy == 1 else 'guesses'}!")
            print(f"(Time: {cas:.2f} seconds)")
            print_cara()
            print("That's amazing!")
            break
        else:
            vypis_vysledek(bulls, cows)

bulls, cows = vyhodnot_tip("1234", "1243")
assert bulls == 2, f"Expected 2 bulls, got {bulls}"
assert cows == 2, f"Expected 2 cows, got {cows}"

bulls, cows = vyhodnot_tip("5678", "1234")
assert bulls == 0, f"Expected 0 bulls, got {bulls}"
assert cows == 0, f"Expected 0 cows, got {cows}"

print("Všechny testy prošly!")

if __name__ == "__main__":
    hlavni()