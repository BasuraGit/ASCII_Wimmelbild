import random
from ..game import Koordinate

class Zufallsgenerator:
    def generiere_random_Char():
        ASCII_Code = random.randint(33,126)
        return chr(ASCII_Code)
    
    def generiere_random_Chars(self,laenge, BlockedChar):
        Chars = list()
        for i in range(laenge):
            while(True):
                Char = chr(random.randint(33,126))
                if not(Char.__eq__(BlockedChar)):
                    break
            Chars.append(Char)
        return Chars

    def generiere_Position(self, Spalten, Zeilen, Ziellaenge):
        Zeile = random.randint(0,Zeilen-1)
        Spalte = random.randint(0, Spalten-(Ziellaenge+1))
        Zielposition = Koordinate(Zeile, Spalte)
        return Zielposition
