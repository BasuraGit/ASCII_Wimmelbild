from ..game import Schwierigkeit

class Konfiguration:
    def __init__(self):
        self._Schwierigkeit = Schwierigkeit(5,5,1,1)
        self._Timer = 60
    
    def reduceTimer(self):
        if self._Timer > 30:
            self._Timer -= 10

        elif self._Timer > 15:
            self._Timer -= 5

        elif self._Timer > 8:
            self._Timer -= 2

        elif self._Timer > 5:
            self._Timer -= 1