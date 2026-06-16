from util import Zufallsgenerator as zg

class Spielfeld:
    def __init__(self, konfiguration):
        self.konfiguration = konfiguration
        self.sk = self.konfiguration.schwierigkeit
        self.feld = list()

    def generieren(self):
        zielsymbolarray = zg.generiere_random_chars(self.sk.zielsymbollaenge)
        self.zielsymbol = str()
        for char in zielsymbolarray:
            self.zielsymbol += char
        self.zielposition = zg.generiere_Position(self.sk)

        for zeile in range(self.sk.zeilen):
            if(zeile != self.zielposition.zeile):
                diese_zeile = zg.generiere_random_chars(self.sk.spalten, blocked_char=self.zielsymbol)
            else:
                laenge_vor   = self.zielposition.spalte
                laenge_nach  = self.sk.spalten - self.zielposition.spalte - self.sk.zielsymbollaenge
                diese_zeile  = zg.generiere_random_chars(laenge_vor, blocked_char=self.zielsymbol)
                diese_zeile += self.zielsymbol
                diese_zeile += zg.generiere_random_chars(laenge_nach, blocked_char=self.zielsymbol)
            diese_zeile += '\n'
            self.feld.append(diese_zeile)
