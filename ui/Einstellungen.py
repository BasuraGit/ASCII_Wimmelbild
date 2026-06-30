from util.Konfiguration import Konfiguration as Konfig
from util.Enums import ProgrammZustand
import os

class Einstellungen:
    def aufrufen(self, konfiguration: Konfig):
        """Zeigt derzeitige Konfiguration und ermöglicht Änderung dieser."""

        self.menue_anzeigen(konfiguration)
        return self.auswahl_verarbeiten(konfiguration)


    def menue_anzeigen(self, konfiguration: Konfig):
        """Leert das Terminal und gibt die Einstellungen aus."""
        os.system("cls" if os.name == "nt" else "clear")

        print("================================")
        print("  Schwierigkeitseinstellungen")
        print("================================")
        print(f"1: Maximale Timerdauer: {konfiguration.timer_max} sec")
        print(f"2: Spielfeldhöhe: {konfiguration.schwierigkeit.zeilen} zeilen")
        print(f"3: Spielfeldbreite: {konfiguration.schwierigkeit.spalten} spalten")
        print(f"4: Zeilenabstand: {konfiguration.schwierigkeit.zeilen_abstand} zeilen")
        print(f"5: Spaltenabstand: {konfiguration.schwierigkeit.spalten_abstand} spalten")
        print("6: Zum Hauptmenü")
        print()

    def auswahl_verarbeiten(self, konfiguration: Konfig):
        """Verarbeitet die Benutzerauswahl."""

        while True:
            auswahl = input("Auswahl: ")

            if auswahl == "1":
                return self.timer_aendern(konfiguration)
            elif auswahl == "2":
                return self.zeilen_aendern(konfiguration)
            elif auswahl == "3":
                return self.spalten_aendern(konfiguration)
            elif auswahl == "4":
                return self.zeilen_dist_aendern(konfiguration)
            elif auswahl == "5":
                return self.spalten_dist_aendern(konfiguration)
            elif auswahl == "6":
                return ProgrammZustand.HAUPTMENUE
            
            input("Ungültige Eingabe. Enter zum Fortfahren...")
            self.menue_anzeigen()

    def timer_aendern(self, konfiguration: Konfig):
        """Aus- und Eingabe für die Einstellung des timer_max."""

        print("================================")
        print(f"  Maximale Timerdauer:  {konfiguration.timer_max} sec")
        print("================================")
        print("""Stellt die Timerdauer am Anfang eines Durchlaufes ein.
Der Timer spiegelt die Zeit über den gesamten Durchlauf wieder.
Nach jedem erfolgreichen Spiel bleibt nur die übergebliebene 
Zeit für die nächsten Spiele über.
Gib eine Zahl zwischen 15 und 60 Sekunden ein.""")
        print()

        while True:
            try:
                auswahl = int(input("Auswahl: "))

                if auswahl <= 60 and auswahl>= 15:
                    konfiguration.timer_max = auswahl
                    break
                print("Zahl außerhalb des Wertebereichs. Versuche es erneut.")
            except ValueError:
                print("Keine reine Zahl eingegeben. Versuche es erneut.")

        return ProgrammZustand.EINSTELLUNGEN
    
    def zeilen_aendern(self, konfiguration: Konfig):
        """Aus- und Eingabe für die Einstellung der Spielfeldhöhe."""

        print("================================")
        print(f"     Spielfeldhöhe:  {konfiguration.schwierigkeit.zeilen} zeilen")
        print("================================")
        print("""Stellt die Höhe des Spielfeldes ein.
                 Die Anzahl der Zeilen muss zwischen 5 und 26 liegen.""")
        print(f"Derzeitiger Wert: {konfiguration.schwierigkeit.zeilen}")
        print()
        
        while True:
            try:
                auswahl = int(input("Auswahl: "))

                if auswahl <= 26 and auswahl>= 5:
                    konfiguration.schwierigkeit.zeilen = auswahl
                    break
                print("Zahl außerhalb des Wertebereichs. Versuche es erneut.")
            except ValueError:
                print("Keine reine Zahl eingegeben. Versuche es erneut.")

        return ProgrammZustand.EINSTELLUNGEN
    
    def spalten_aendern(self, konfiguration: Konfig):
        """Aus- und Eingabe für die Einstellung der Spielfeldbreite."""

        print("================================")
        print(f"  Spielfeldbreite: {konfiguration.schwierigkeit.spalten} spalten")
        print("================================")
        print("""Stellt die Breite des Spielfeldes ein.
                 Die Anzahl der Spalten muss zwischen 5 und 26 liegen.""")
        print(f"Derzeitiger Wert: {konfiguration.schwierigkeit.spalten}")
        print()
        
        while True:
            try:
                auswahl = int(input("Auswahl: "))

                if auswahl <= 26 and auswahl>= 5:
                    konfiguration.schwierigkeit.spalten = auswahl
                    break
                print("Zahl außerhalb des Wertebereichs. Versuche es erneut.")
            except ValueError:
                print("Keine reine Zahl eingegeben. Versuche es erneut.")

        return ProgrammZustand.EINSTELLUNGEN
    
    def zeilen_dist_aendern(self, konfiguration: Konfig):
        """Aus- und Eingabe für die Einstellung der Zeilenabstände."""

        print("================================")
        print(f"    Zeilenabstände: {konfiguration.schwierigkeit.zeilen_abstand} zeilen")
        print("================================")
        print("""Stellt den Abstand der Zeilen auf dem Spielfeld ein.
                 Der Zeilenabstand kann entweder auf 0 oder auf 1 gestellt werden.""")
        print(f"Derzeitiger Wert: {konfiguration.schwierigkeit.zeilen_abstand}")
        print()
        
        while True:
                auswahl = input("Auswahl: ")

                if auswahl == "0":
                    konfiguration.schwierigkeit.zeilen_abstand = 0
                    break
                elif auswahl == "1":
                    konfiguration.schwierigkeit.zeilen_abstand = 1
                    break
                
                print("Gib 0 oder 1 ein.")

        return ProgrammZustand.EINSTELLUNGEN
    
    def spalten_dist_aendern(self, konfiguration: Konfig):
        """Aus- und Eingabe für die Einstellung der Spaltenabstände."""

        print("================================")
        print(f"  Spaltenabstände: {konfiguration.schwierigkeit.spalten_abstand} spalten")
        print("================================")
        print("""Stellt den Abstand der Spalten auf dem Spielfeld ein.
                 Der Spaltenabstand kann entweder auf 0, 1 oder 2 gestellt werden.""")
        print(f"Derzeitiger Wert: {konfiguration.schwierigkeit.spalten_abstand}")
        print()
        
        while True:
                auswahl = input("Auswahl: ")

                if auswahl == "0":
                    konfiguration.schwierigkeit.spalten_abstand = 0
                    break
                elif auswahl == "1":
                    konfiguration.schwierigkeit.spalten_abstand = 1
                    break
                elif auswahl == "2":
                    konfiguration.schwierigkeit.spalten_abstand = 2
                    break
                
                print("Gib 0, 1 oder 2 ein.")

        return ProgrammZustand.EINSTELLUNGEN