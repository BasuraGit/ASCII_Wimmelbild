from util.Enums import ErfolgsEnum

class SpielAusgabe:
    """
    Verantwortlich für die vollständige Ausgabe einer Spielrunde
    in der Konsole.
    """

    def __init__(self):
        self.gedruckte_zeilen = 0


    def get_zielsymbol(self, spielfeld):
        """
        Gibt das vom Nutzer zu suchende Symbol aus.

        Parameter:
            spielfeld: Das aktuell verwendete Spielfeldobjekt.
        """
        return f"Das gesuchte Symbol ist: {spielfeld.zielsymbol}\n"
        


    def zeige_rueckmeldung(self, erfolg: ErfolgsEnum):
        """
        Gibt eine Rückmeldung über das Ergebnis der Nutzereingabe aus.

        Parameter:
            Erfolg: Enum-Wert, der den Ausgang der Runde beschreibt.
        """
        if(erfolg == ErfolgsEnum.RIGHTINPUT):
            print("Sehr Gut! Das war die richtige Position.")
        elif(erfolg == ErfolgsEnum.WRONGINPUT):
            print("Das war leider nicht die richtige Position.")
        elif(erfolg == ErfolgsEnum.TIMEOUT):
            print("Du warst leider zu langsam. Die Zeit ist abgelaufen.")
        else:
            print("Fehler bei der Auswertung.")

    def get_index_char(self, index):
        """
        Wandelt einen numerischen Index in eine für die Anzeige geeignete
        Darstellung um.

        Die Indizes 0 bis 8 werden als Zahlen von 1 bis 9 dargestellt.
        Anschließend werden die Indizes als Großbuchstaben ausgegeben.

        Beispiele:
            0 -> "1"
            8 -> "9"
            9 -> "A"
            10 -> "B"

        Parameter:
            index: Numerischer Index.

        Rückgabewert:
            Zeichenkette zur Darstellung des Indexes.
        """

        if(index<26):
            index = chr(65 + index)
        return index
    

    def get_spielfeld(self, spielfeld):
        """
        Gibt das aktuelle Spielfeld inklusive Zeilen- und
        Spaltenbeschriftung in der Konsole aus.

        Die Darstellung berücksichtigt die in der Konfiguration
        festgelegten Abstände zwischen Zeilen und Spalten.

        Parameter:
            spielfeld: Das aktuell verwendete Spielfeldobjekt.
        """
        schwierigkeit = spielfeld.konfiguration.schwierigkeit
        index_string = "    "
        print_list = list()

        # Erzeugt die Beschriftung der Spalten.
        for spalte in range(schwierigkeit.spalten):
            
            index_string += self.get_index_char(spalte) + " " * schwierigkeit.spalten_abstand

        print_list.append(index_string + "\n")        
        print_list.append("\n")        


        zeilencounter = 0

        # Gibt jede Zeile des Spielfelds aus.
        for zeile in spielfeld.feld:

            # Fügt die Zeilenbeschriftung hinzu.
            zeilenstring = self.get_index_char(zeilencounter) + "   "
            zeilencounter += 1

            # Fügt die Zeichen der aktuellen Zeile hinzu.
            for char in zeile:
                zeilenstring += char + schwierigkeit.spalten_abstand * " "
            print_list.append(zeilenstring + "\n")        


            # Fügt Leerzeilen zwischen den Spielfeldzeilen ein.
            for i in range(schwierigkeit.zeilen_abstand):
                print_list.append("\n")  

        return "".join(print_list)      

    def clear_console(self):
        print("\033[H\033[3J", end="")
