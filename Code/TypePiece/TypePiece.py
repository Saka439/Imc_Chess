from enum import Enum

class TypePiece(Enum):
    ROI = 1
    DAME = 2
    TOUR = 3
    FOU = 4
    CAVALIER = 5
    PION = 6

    def vers_chaine(self):
        if self == TypePiece.ROI:
            return "Roi"
        elif self == TypePiece.DAME:
            return "DAME"
        elif self == TypePiece.TOUR:
            return "Tour"
        elif self == TypePiece.FOU:
            return "Fou"
        elif self == TypePiece.CAVALIER:
            return "Cavalier"
        elif self == TypePiece.PION:
            return "Pion"
        
