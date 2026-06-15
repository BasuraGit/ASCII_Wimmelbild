import random
from ..game import Koordinate

def generiere_random_chars(BlockedChar, laenge=1):
    return [generiere_random_char(BlockedChar) for _ in range(laenge)]

def generiere_random_char(BlockedChar):
        while(True):
            Char = chr(random.randint(33,126))
            if not(Char.__eq__(BlockedChar)):
                break
        return Char

def generiere_Position(Spalten, Zeilen, Ziellaenge):
    Zeile = random.randint(0,Zeilen-1)
    Spalte = random.randint(0, Spalten-(Ziellaenge+1))
    Zielposition = Koordinate(Zeile, Spalte)
    return Zielposition
