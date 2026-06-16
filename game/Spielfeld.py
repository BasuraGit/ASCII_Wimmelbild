from util import Zufallsgenerator as zg


class Spielfeld:
    """
    Repräsentiert das Spielfeld einer Spielrunde.

    Die Klasse ist für die Generierung des Zeichenfeldes zuständig.
    Sie bestimmt das Zielsymbol, dessen Position und erzeugt die
    zufälligen Inhalte des Spielfelds.
    """

    def __init__(self, konfiguration):
        """
        Initialisiert das Spielfeld mit der übergebenen Konfiguration.

        Parameter:
            konfiguration: Enthält die Einstellungen des Spiels,
                            insbesondere den aktuellen Schwierigkeitsgrad.
        """
        self.konfiguration = konfiguration
        self.sk = self.konfiguration.schwierigkeit
        self.feld = list()

    def generieren(self):
        """
        Erzeugt ein neues Spielfeld.

        Der Ablauf besteht aus folgenden Schritten:
        - Generierung eines zufälligen Zielsymbols.
        - Bestimmung einer zufälligen Zielposition.
        - Erzeugung aller Spielfeldzeilen.
        - Platzierung des Zielsymbols an der Zielposition.
        - Auffüllen der übrigen Felder mit Zufallszeichen.
        """
        # Leert das Feld für eine neue Generierung
        self.feld.clear()

        # Erzeugt die Zeichen, aus denen das Zielsymbol besteht.
        zielsymbolarray = zg.generiere_random_chars(
            self.sk.zielsymbollaenge
        )

        # Setzt die einzelnen Zeichen zu einem String zusammen.
        self.zielsymbol = str()

        for char in zielsymbolarray:
            self.zielsymbol += char

        # Ermittelt die Position des Zielsymbols innerhalb des Spielfelds.
        self.zielposition = zg.generiere_Position(self.sk)

        # Erzeugt jede Zeile des Spielfelds.
        for zeile in range(self.sk.zeilen):

            # Zeilen ohne Zielsymbol.
            if(zeile != self.zielposition.zeile):

                diese_zeile = zg.generiere_random_chars(
                    self.sk.spalten,
                    blocked_char=self.zielsymbol
                )

            # Zeile, die das Zielsymbol enthält.
            else:
                # Anzahl der Zeichen vor dem Zielsymbol.
                laenge_vor = self.zielposition.spalte

                # Anzahl der Zeichen nach dem Zielsymbol.
                laenge_nach = (
                    self.sk.spalten
                    - self.zielposition.spalte
                    - self.sk.zielsymbollaenge
                )

                # Generiert die Zeichen vor dem Zielsymbol.
                diese_zeile = zg.generiere_random_chars(
                    laenge_vor,
                    blocked_char=self.zielsymbol
                )

                # Fügt das Zielsymbol ein.
                diese_zeile += self.zielsymbol

                # Generiert die Zeichen nach dem Zielsymbol.
                diese_zeile += zg.generiere_random_chars(
                    laenge_nach,
                    blocked_char=self.zielsymbol
                )

            # Fügt die fertige Zeile dem Spielfeld hinzu.
            self.feld.append(diese_zeile)