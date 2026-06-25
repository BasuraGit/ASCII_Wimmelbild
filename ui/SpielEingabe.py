from game.Schwierigkeit import Schwierigkeit as sk
from game.Koordinate import Koordinate as pos
from util.Enums import ErfolgsEnum
from prompt_toolkit.widgets import Label
from asyncio import Queue

class SpielEingabe:
    
    async def start(
        self, 
        input_queue: Queue, 
        ziel_pos: pos, 
        schwierigkeit: sk, 
        feedback_label: Label
    ):
               
        while True:
            user_input = await input_queue.get()

            position = self.handle_input(
                user_input,
                schwierigkeit,
                feedback_label
            )

            # Eingabe ungültig -> nächste Eingabe
            if position is None:
                continue
            
            feedback_label.text = ""
            ein_zeile, ein_spalte = position

            if (
                ein_spalte == ziel_pos.spalte and
                ein_zeile == ziel_pos.zeile
            ):
                return ErfolgsEnum.RIGHTINPUT
            
            return ErfolgsEnum.WRONGINPUT       
    
    def handle_input(
        self, 
        input: str, 
        schwierigkeit: sk, 
        feedback_label: Label
    ):

        if input.find(",") == -1:
            feedback_label.text = "Die Position wurde nicht in der Form ZEILE, SPALTE eingegeben."
            return None
        
        zeile, spalte = input.split(",")

        zeile = zeile.strip()
        spalte = spalte.strip()

        if not zeile.__len__() == 1:
            feedback_label.text = "Der Zeileneintrag muss ein Zeichen lang sein."
            return None
        
        if not spalte.__len__() == 1:
            feedback_label.text = "Der Spalteneintrag muss ein Zeichen lang sein."
            return None
        
        if not zeile.isalpha():
            feedback_label.text = "Der Zeileneintrag muss ein Buchstabe sein."
            return None
        
        if not spalte.isalpha():
            feedback_label.text = "Der Spalteneintrag muss ein Buchstabe sein."
            return None
        
        # Position in int Indexen bestimmen
        zeile = ord(zeile.upper()) - 65
        spalte = ord(spalte.upper()) - 65

        if zeile >= schwierigkeit.zeilen:
            feedback_label.text = "Der Zeilenindex ist nicht innerhalb des Feldes."
            return None
        
        if spalte >= schwierigkeit.spalten:
            feedback_label.text = "Der Spaltenindex ist nicht innerhalb des Feldes."
            return None

        return [zeile, spalte]   
