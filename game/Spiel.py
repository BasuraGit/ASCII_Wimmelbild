from game.Spielfeld import Spielfeld
from game.Schwierigkeit import Schwierigkeit
from game.Timer import Timer
from ui.SpielEingabe import SpielEingabe
from ui.SpielAusgabe import SpielAusgabe

class Spiel:
    def __init__(self, konfiguration):
        self.konfiguration = konfiguration
        self.spielfeld = Spielfeld(self.konfiguration)
        self.schwierigkeit = self.konfiguration.schwierigkeit
        self.aktuelle_runde = 1
        self.spiel_ausgabe = SpielAusgabe()
        self.spiel_eingabe = SpielEingabe()
        # self.timer = Timer()
    
    def starten(self):
        self.spielfeld.generieren()
        self.spiel_ausgabe.zeige_spiel(self.spielfeld)
        # self.timer.start(self.konfiguration.timer_max)
        self.spiel_eingabe.start()
    
    def neue_runde(self):
        pass
    
    def auswerten(self):
        pass

    def beenden(self):
        pass

