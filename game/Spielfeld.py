from ..util import Zufallsgenerator as zg

class Spielfeld:
    def __init__(self, _Konfiguration):
        self._Konfiguration = _Konfiguration
        self._Feld = list()
        self._Zielsymbol = zg.generiere_random_chars('\0', _Konfiguration._Schwierigkeit._Zielsymbollaenge)
        self._Zielposition = zg.generiere_Position()

    def generieren():
        pass

    def anzeigen():
        pass