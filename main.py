from game.Spiel import Spiel
from util.Konfiguration import Konfiguration
from ui.HauptMenue import HauptMenue
from ui.ZwischenMenue import ZwischenMenue
from ui.Einstellungen import Einstellungen
from util.Enums import ProgrammZustand
import asyncio

konfiguration = Konfiguration()
haupt_menue = HauptMenue()
zwischen_menue = ZwischenMenue()
einstellungen = Einstellungen()

spiel=Spiel(konfiguration, haupt_menue)

zustand = ProgrammZustand.HAUPTMENUE

while zustand != ProgrammZustand.BEENDEN:

    if zustand == ProgrammZustand.HAUPTMENUE:
        zustand = haupt_menue.starten()

        if zustand == ProgrammZustand.SPIEL:
            spiel.neues_spiel(konfiguration)

    elif zustand == ProgrammZustand.EINSTELLUNGEN:
        zustand = einstellungen.aufrufen(konfiguration)

    elif zustand == ProgrammZustand.SPIEL:
        zustand = asyncio.run(spiel.starten())

    elif zustand == ProgrammZustand.ZWISCHENMENUE:
        zustand = zwischen_menue.starten(spiel)
