from enum import Enum,auto

class ErfolgsEnum(Enum):
    TIMEOUT = 0
    WRONGINPUT = 1
    RIGHTINPUT = 2

class ProgrammZustand(Enum):
    HAUPTMENUE = auto()
    ZWISCHENMENUE = auto()
    EINSTELLUNGEN = auto()
    SPIEL = auto()
    BEENDEN = auto()