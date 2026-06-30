from game.Schwierigkeit import Schwierigkeit

class Konfiguration:
    def __init__(self):
        self.schwierigkeit = Schwierigkeit(15,15,1,0,0)
        self.timer_max = 60
        