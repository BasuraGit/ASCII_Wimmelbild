import random

class Zufallsgenerator:
    def generiere_random_Char():
        ASCII_Code = random.randint(33,126)
        return chr(ASCII_Code)
    def generiere_random_String_of_laenge(self,laenge):
