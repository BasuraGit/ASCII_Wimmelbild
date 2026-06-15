from dataclasses import dataclass

@dataclass(frozen=True)
class Koordinate:
    _Zeile: int
    _Spalte: int