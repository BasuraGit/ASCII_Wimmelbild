from dataclasses import dataclass

@dataclass
class Schwierigkeit:
    zeilen: int
    spalten: int
    zielsymbollaenge: int
    zeilen_abstand: int
    spalten_abstand: int