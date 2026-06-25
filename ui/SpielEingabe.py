from game.Schwierigkeit import Schwierigkeit as sk
from game.Koordinate import Koordinate as pos
from util.Enums import ErfolgsEnum
from prompt_toolkit.widgets import Label
from asyncio import Queue

class SpielEingabe:
    
    async def start(
        self, 
        input_queue: Queue, 
        ziel_pos: pos, 
        schwierigkeit: sk, 
        feedback_label: Label
    ):
               
        ein_position = await input_future

        ein_zeile, ein_spalte = ein_position.strip().split(",")
        ein_zeile = ord(ein_zeile.upper()) - 65
        ein_spalte = ord(ein_spalte.upper()) - 65
        erfolg = (ein_spalte == ziel_pos.spalte and ein_zeile == ziel_pos.zeile)
        if erfolg:
            return ErfolgsEnum.RIGHTINPUT
        return ErfolgsEnum.WRONGINPUT