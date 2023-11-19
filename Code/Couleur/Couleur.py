from enum import Enum

class Couleur(Enum):
    BLANC = 0
    NOIR = 1

    def __invert__(self):
         pass

    @classmethod
    def vers_chaine(cls, couleur):
        pass

