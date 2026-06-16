from dataclasses import dataclass

@dataclass(frozen=True)
class Koordinate:
    zeile: int
    spalte: int