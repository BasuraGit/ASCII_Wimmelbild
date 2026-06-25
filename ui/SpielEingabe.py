from util.Enums import ErfolgsEnum

class SpielEingabe:
    
    async def start(self, input_future, ziel_pos):
               
        ein_position = await input_future

        ein_zeile, ein_spalte = ein_position.strip().split(",")
        ein_zeile = ord(ein_zeile.upper()) - 65
        ein_spalte = ord(ein_spalte.upper()) - 65
        erfolg = (ein_spalte == ziel_pos.spalte) & (ein_zeile == ziel_pos.spalte)
        if erfolg:
            return ErfolgsEnum.RIGHTINPUT
        return ErfolgsEnum.WRONGINPUT