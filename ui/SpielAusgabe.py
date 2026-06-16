class SpielAusgabe:
    def zeige_spiel(self, spielfeld):
        self.zeige_zielsymbol(spielfeld)
        self.zeige_spielfeld(spielfeld)
        self.zeige_input()
   
    def zeige_zielsymbol(self, spielfeld):
        print("Das gesuchte Symbol ist: " + spielfeld.zielsymbol)

    def zeige_input(self):
        print("Gib die Position des gesuchten Symbols ein: ")

    
    def get_index_char(self, index):
            if(index<9):
                index += 1
                index = f"{index}"
            elif(index<35):
                index = chr(65 + index - 9)
            return index
    

    def zeige_spielfeld(self, spielfeld):

        difficulty = spielfeld.konfiguration.schwierigkeit
        index_string = "\t"

        for spalte in range(difficulty.spalten):
            
            index_string += self.get_index_char(spalte) + " " * difficulty.spalten_abstand

        print(index_string)
        print()

        zeilencounter = 0
        for zeile in spielfeld.feld:
    
            zeilenstring = self.get_index_char(zeilencounter) + "\t"
            zeilencounter += 1

            for char in zeile:
                if(char == '\n'):
                    break
                zeilenstring += char + difficulty.spalten_abstand * " "
            print(zeilenstring)
            for i in range(difficulty.zeilen_abstand):
                print()
