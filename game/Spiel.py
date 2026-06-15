import Spielfeld
import Schwierigkeit
from ..io import SpielEingabe
from ..io import SpielAusgabe

class Spiel:
    def __init__(self, Konfiguration):
        self.spielfeld = Spielfeld(Konfiguration)
        self.schwierigkeit = Schwierigkeit(Konfiguration)
        self.aktuelle_Runde = 1
        self.spielAusgabe = SpielAusgabe()
        self.spielEingabe = SpielEingabe()
    
    def starten(self):
        pass
    
    def neue_runde(self):
        pass
    
    def auswerten(self):
        pass

    def beenden(self):
        pass

