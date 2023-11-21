from enum import Enum

class Couleur(Enum):
    BLANC = 1
    NOIR = 0

    def __invert__(self):
        if(self==Couleur.BLANC):
            return Couleur.NOIR
        else:
            return Couleur.BLANC
         

    @classmethod
    def vers_chaine(cls, couleur):
        if(couleur==Couleur.BLANC):
            return "Blanc"
        else:
            return "Noir"

