from game.Spielfeld import Spielfeld
from game.Timer import Timer
from ui.SpielEingabe import SpielEingabe
from ui.SpielAusgabe import SpielAusgabe
from ui.ZwischenMenue import ZwischenMenue
from util.Enums import ErfolgsEnum, ProgrammZustand


class Spiel:
    """
    Steuert den Ablauf einer Spielsitzung.

    Die Klasse koordiniert die Zusammenarbeit der einzelnen Komponenten,
    wie Spielfeld, Ein- und Ausgabe sowie die Menüsteuerung.
    """

    def __init__(self, konfiguration, haupt_menue):
        """
        Initialisiert eine neue Spielinstanz.

        Parameter:
            konfiguration: Enthält die aktuellen Spieleinstellungen.
            haupt_menue: Referenz auf das Hauptmenü, um nach Spielende
                          dorthin zurückkehren zu können.
        """
        self.konfiguration = konfiguration

        # Erzeugt das Spielfeld auf Basis der aktuellen Konfiguration.
        self.spielfeld = Spielfeld(self.konfiguration)

        # Speichert eine Referenz auf den aktuellen Schwierigkeitsgrad.
        self.schwierigkeit = self.konfiguration.schwierigkeit

        # Zählt die aktuell gespielte Runde.
        self.aktuelle_runde = 1

        # Zuständig für die Konsolenausgabe.
        self.spiel_ausgabe = SpielAusgabe()

        # Zuständig für die Eingaben des Nutzers.
        self.spiel_eingabe = SpielEingabe()

        # Menü zwischen zwei Spielrunden.
        self.zwischen_menue = ZwischenMenue()

        # Referenz auf das Hauptmenü.
        self.haupt_menue = haupt_menue

        # Timer für die Zeitbegrenzung.
        # self.timer = Timer()

    def starten(self):
        """
        Startet eine neue Spielrunde.

        Das Spielfeld wird erzeugt und anschließend in der Konsole
        dargestellt.

        Ein ablaufender Timer und die Nutzereingabe werden als Threads erzeugt.
        """
        self.spielfeld.generieren()
        self.spiel_ausgabe.zeige_spiel(self.spielfeld)

        # TODO: TIMER und Eingabe als Threads umsetzen,
        # um beides gleichzeitig zu machen.

        # completion_event ? threading.Event()
        #
        # next_state=list()
        # timer_thread = Thread(target=self.timer.start, args=(self.konfiguration.timer_max, completion_event, next_state))
        # input_thread = Thread(target=self.spiel_eingabe.start, args=(completion_event, next_state))
        # timer_thread.start()
        # input_thread.start()
        #
        # End based on threading.Event() with completion_event.wait()
        # in thread: completion_event.set()
        #
        # more research regarding cleanup and its interaction with event based ending necessary
        #
        # return next_state[0]

    def neue_runde(self):
        """
        Startet eine weitere Spielrunde.

        Vor Beginn der neuen Runde wird die maximale Suchzeit
        reduziert, um den Schwierigkeitsgrad schrittweise zu erhöhen.
        Die Rundenanzahl wird mitgezählt.
        """
        self.aktuelle_runde += 1
        self.konfiguration.reduce_timer_max()
        self.starten()

    def auswerten(self, erfolgscode: ErfolgsEnum):
        """
        Wertet das Ergebnis der Spielrunde aus.

        Zunächst wird eine Rückmeldung ausgegeben.
        Anschließend wird abhängig vom Ergebnis das passende Menü
        aufgerufen.

        Parameter:
            erfolgscode: Enum-Wert, der das Ergebnis der Runde beschreibt.
        """
        self.spiel_ausgabe.zeige_rueckmeldung(erfolgscode)

        if (erfolgscode == ErfolgsEnum.RIGHTINPUT):
            return ProgrammZustand.ZWISCHENMENUE
        else:
            return ProgrammZustand.HAUPTMENUE

    def beenden(self):
        """
        Beendet die aktuelle Spielrunde.

        Der Ablauf entspricht einem Zeitüberschreitungsereignis.
        Die Auswertung erfolgt daher mit dem entsprechenden
        Erfolgsstatus.

        Die Beendigung des Timer-Threads ist als zukünftige
        Erweiterung vorgesehen.
        """
        # Timer thread beenden
        self.auswerten(ErfolgsEnum.TIMEOUT)