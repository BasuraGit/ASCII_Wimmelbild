import Spielfeld
import Schwierigkeit
from ..io import SpielEingabe
from ..io import SpielAusgabe

class Spiel:
    def __init__(self, _Konfiguration):
        self._Spielfeld = Spielfeld(_Konfiguration)
        self._Schwierigkeit = Schwierigkeit(_Konfiguration)
        self._Aktuelle_Runde = 1
        self._Spiel_Ausgabe = SpielAusgabe()
        self._Spiel_Eingabe = SpielEingabe()
    
    def starten(self):
        self._Spielfeld.generieren()
        self._Spielfeld.ausgeben()
        self._Timer.start()
        self._Spiel_Eingabe.start()
    
    def neue_runde(self):
        pass
    
    def auswerten(self):
        pass

    def beenden(self):
        pass

