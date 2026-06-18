from game.Spiel import Spiel
from util.Konfiguration import Konfiguration
from ui.HauptMenue import HauptMenue
from ui.ZwischenMenue import ZwischenMenue
from util.Enums import ProgrammZustand

konfiguration = Konfiguration()
haupt_menue = HauptMenue()
zwischen_menue = ZwischenMenue()

spiel=Spiel(konfiguration, haupt_menue)

spiel.starten()

zustand = ProgrammZustand.HAUPTMENUE

while zustand != ProgrammZustand.BEENDEN:

    if zustand == ProgrammZustand.HAUPTMENUE:
        zustand = haupt_menue.starten()

    elif zustand == ProgrammZustand.SPIEL:
        zustand = spiel.starten()

    elif zustand == ProgrammZustand.ZWISCHENMENUE:
        zustand = zwischen_menue.starten()
        