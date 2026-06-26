from game.Spiel import Spiel
from util.Konfiguration import Konfiguration
from ui.HauptMenue import HauptMenue
from ui.ZwischenMenue import ZwischenMenue
from util.Enums import ProgrammZustand
import asyncio

konfiguration = Konfiguration()
haupt_menue = HauptMenue()
zwischen_menue = ZwischenMenue()

spiel=Spiel(konfiguration, haupt_menue)

zustand = ProgrammZustand.HAUPTMENUE

while zustand != ProgrammZustand.BEENDEN:

    if zustand == ProgrammZustand.HAUPTMENUE:
        zustand = haupt_menue.starten()

        if zustand == ProgrammZustand.SPIEL:
            spiel.neues_spiel()

    elif zustand == ProgrammZustand.SPIEL:
        zustand = asyncio.run(spiel.starten())

    elif zustand == ProgrammZustand.ZWISCHENMENUE:
        zustand = zwischen_menue.starten(spiel)
