from game.Spielfeld import Spielfeld
from game.Timer import Timer
from ui.SpielEingabe import SpielEingabe
from ui.SpielAusgabe import SpielAusgabe
from ui.ZwischenMenue import ZwischenMenue
from util.Enums import ErfolgsEnum, ProgrammZustand
from util.Konfiguration import Konfiguration as Konfig
from ui.HauptMenue import HauptMenue as Menu

import asyncio

from prompt_toolkit.application import Application
from prompt_toolkit.layout import Layout
from prompt_toolkit.layout.containers import HSplit
from prompt_toolkit.widgets import Label, TextArea
from prompt_toolkit.key_binding import KeyBindings

class Spiel:
    """
    Steuert den Ablauf einer Spielsitzung.

    Die Klasse koordiniert die Zusammenarbeit der einzelnen Komponenten,
    wie Spielfeld, Ein- und Ausgabe sowie die Menüsteuerung.
    """

    def __init__(self, konfiguration: Konfig, menu: Menu):
        """
        Initialisiert eine neue Spielinstanz.

        Parameter:
            konfiguration: Enthält die aktuellen Spieleinstellungen.
        """
        self.konfiguration = konfiguration

        self.menu = Menu

        # Erzeugt das Spielfeld auf Basis der aktuellen Konfiguration.
        self.spielfeld = Spielfeld(self.konfiguration)

        # Speichert eine Referenz auf den aktuellen Schwierigkeitsgrad.
        self.schwierigkeit = self.konfiguration.schwierigkeit

        # Zählt die aktuell gespielte Runde.
        self.aktuelle_runde = 1

        # Zählt die erfolgreich gelösten Runden.
        self.score = 0

        # Merkt sich die Restzeit für die nächste Runde.
        self.restzeit = self.konfiguration.timer_max

        # Speichert den letzten Erfolgszustand für das Zwischenmenü.
        self.letzter_erfolg = None

        # Zuständig für die Konsolenausgabe.
        self.spiel_ausgabe = SpielAusgabe()

        # Zuständig für die Eingaben des Nutzers.
        self.spiel_eingabe = SpielEingabe()

        # Timer für die Zeitbegrenzung.
        self.timer = Timer()


    async def starten(self):
        """
        Startet eine neue Spielrunde.

        Das Spielfeld wird erzeugt und anschließend in der Konsole
        dargestellt.

        Ein ablaufender Timer wird gestartet und der Nutzer kann eine Lösung eingeben.
        """
        
        # neues Spielfeld mit einer Instanz des Zielsymbols generieren
        self.spielfeld.generieren()

        # Konsolenausgabe leeren
        self.spiel_ausgabe.clear_console()


        # Labels für Formatierte Ausgabe mit promp_toolkit definieren
        ziel_label = Label(self.spiel_ausgabe.get_zielsymbol(self.spielfeld))
        timer_label = Label(f"Zeit: 00:{self.restzeit:02d}")
        feld_label = Label(self.spiel_ausgabe.get_spielfeld(self.spielfeld))
        input_feld = TextArea(
            prompt ="Gib die Position des gesuchten Symbols ein (Zeile, Spalte):  ",
            multiline = False,
        )
        feedback_label = Label("")

        # Labels im Layout sortieren
        layout = HSplit([
            ziel_label,
            timer_label,
            feld_label,
            input_feld,
            feedback_label
        ])

        # Input einrichten
        self.input_queue = asyncio.Queue()
        kb = KeyBindings()

        # Input an SpielEingabe "nachreichen" wenn Enter gedrückt wird 
        @kb.add("enter")
        def _(event):
            self.input_queue.put_nowait(input_feld.text)

        # Application definieren
        self.app = Application(
            layout=Layout(layout, focused_element=input_feld),
            key_bindings=kb,
            full_screen=False
        )

        # Erzeuge und Starte Timer und Input 

        tasks = [
            asyncio.create_task(
                self.timer.start(self.restzeit, timer_label, self.app)
            ),
            asyncio.create_task(
                self.spiel_eingabe.start(
                    self.input_queue, 
                    self.spielfeld.zielposition,
                    self.schwierigkeit, 
                    feedback_label)
                )
        ]

        # Application starten ( Ausgabe )
        app_task = asyncio.create_task(
            self.app.run_async()
        )

        fertige_task, pending_task = await asyncio.wait(
            tasks,
            return_when = asyncio.FIRST_COMPLETED
        )

        # Lies rückgegeben ErfolgsCode von erster beendeter Funktion
        erfolg = fertige_task.pop().result()
        
        # Beende und warte auf beenden der Durchlaufsanzeige
        self.app.exit()
        await app_task
        
        # Beende die Task die nicht als Erstes fertig war
        for task in pending_task:
            task.cancel()

        # Aufgrund von Rückgabewert zum Hauptmenü oder ins Zwischenmenü springen
        return self.auswerten(erfolg)

    def neue_runde(self):
        """
        Startet eine weitere Spielrunde.

        Vor Beginn der neuen Runde wird die maximale Suchzeit
        reduziert, um den Schwierigkeitsgrad schrittweise zu erhöhen.
        Die Rundenanzahl wird mitgezählt.
        """
        self.aktuelle_runde += 1
        self.starten()

    def neues_spiel(self):
        """Setzt den Spielstand für einen neuen Durchlauf zurück."""
        self.aktuelle_runde = 1
        self.score = 0
        self.restzeit = self.konfiguration.timer_max
        self.letzter_erfolg = None

    def auswerten(self, erfolgscode: ErfolgsEnum):
        """
        Wertet das Ergebnis der Spielrunde aus.

        Zunächst wird eine Rückmeldung ausgegeben.
        Anschließend wird abhängig vom Ergebnis das passende Menü
        aufgerufen.

        Parameter:
            erfolgscode: Enum-Wert, der das Ergebnis der Runde beschreibt.
        """
        self.letzter_erfolg = erfolgscode

        if (erfolgscode == ErfolgsEnum.RIGHTINPUT):
            self.spiel_ausgabe.zeige_rueckmeldung(erfolgscode)
            self.score += 1
            self.aktuelle_runde += 1
            self.restzeit = self.timer.letzte_restzeit
            return ProgrammZustand.ZWISCHENMENUE
        elif (erfolgscode == ErfolgsEnum.TIMEOUT):
            self.restzeit = self.timer.letzte_restzeit
            return ProgrammZustand.ZWISCHENMENUE
        else:
            self.spiel_ausgabe.zeige_rueckmeldung(erfolgscode)
            self.restzeit = self.konfiguration.timer_max
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