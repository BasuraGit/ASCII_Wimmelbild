from game.Schwierigkeit import Schwierigkeit

class Konfiguration:
    def __init__(self):
        self.schwierigkeit = Schwierigkeit(5,5,1,0,1)
        self.timer_max = 60
    
    def reduce_timer_max(self):
        if self.timer_max > 30:
            self.timer_max -= 10

        elif self.timer_max > 15:
            self.timer_max -= 5

        elif self.timer_max > 8:
            self.timer_max -= 2

        elif self.timer_max > 5:
            self.timer_max -= 1