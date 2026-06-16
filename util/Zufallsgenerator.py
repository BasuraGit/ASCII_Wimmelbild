import random
from game.Koordinate import Koordinate

def generiere_random_chars(laenge=1, *,blocked_char='\0'):
    return [generiere_random_char(blocked_char) for _ in range(laenge)]

def generiere_random_char(blocked_char):
        while(True):
            char = chr(random.randint(33,126))
            if char != blocked_char:  
                break
        return char

def generiere_Position(schwierigkeit):
    zeile = random.randint(0,schwierigkeit.zeilen-1)
    spalte = random.randint(0, schwierigkeit.spalten-(schwierigkeit.zielsymbollaenge+1))
    zielposition = Koordinate(zeile, spalte)
    return zielposition
