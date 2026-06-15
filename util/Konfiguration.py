class Konfiguration:
    def __init__(self):
        self.Zeilen = 5
        self.Spalten = 5
        self.Zielsymbollaenge = 1
        self.Timer = 60
        self.ZeichenAbstand = 1
    
    def reduceTimer(self):
        if self.Timer > 30:
            self.Timer -= 10

        elif self.Timer > 15:
            self.Timer -= 5

        elif self.Timer > 8:
            self.Timer -= 2

        elif self.Timer > 5:
            self.Timer -= 1