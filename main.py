from game.Spiel import Spiel
from util.Konfiguration import Konfiguration
from ui.HauptMenue import HauptMenue

konfiguration = Konfiguration()


spiel=Spiel(konfiguration)

spiel.starten()