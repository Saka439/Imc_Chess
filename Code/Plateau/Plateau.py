import sys
import os

chemin_dossier_1 = os.path.dirname(os.path.realpath(__file__)) + '/../Pos'
chemin_dossier_2 = os.path.dirname(os.path.realpath(__file__)) + '/../CasePlateau'



if chemin_dossier_1 not in sys.path:
    sys.path.append(chemin_dossier_1)
if chemin_dossier_2 not in sys.path:
    sys.path.append(chemin_dossier_2)

from Pos import*
from CasePlateau import*


class Plateau:
    NLIGNES = 8
    NCOLONNES = 8

    def __init__(self):
        Matrice=[]
        self.matCases=Matrice
        for i in range(self.NLIGNES):
            liste=[]
            for j in range(self.NCOLONNES):
                liste.append(CasePlateau())
            (self.matCases).append(liste)

    def ajoute_piece(self, piece, pos):
        ((self.matCases)[(pos.ligne)-1][(pos.colonne)-1])=CasePlateau(piece)

    def bouge_piece(self, pos_depart, pos_fin):
        (self.matCases)[(pos_fin.ligne)-1][(pos_fin.colonne)-1]=(self.matCases)[(pos_depart.ligne)-1][(pos_depart.colonne)-1]
        (self.matCases)[(pos_depart.ligne)-1][(pos_depart.colonne)-1]=CasePlateau()
    def est_case_occupe(self, pos):
        if((self.matCases)[(pos.ligne)-1][(pos.colonne)-1]).piece==None:
            return False
        else:
            return True

    def init_partie(self):
        (self.matCases)[0][0]=CasePlateau(Piece(TypePiece.TOUR,Couleur.NOIR))
        (self.matCases)[0][1]=CasePlateau(Piece(TypePiece.CAVALIER,Couleur.NOIR))
        (self.matCases)[0][2]=CasePlateau(Piece(TypePiece.FOU,Couleur.NOIR))
        (self.matCases)[0][3]=CasePlateau(Piece(TypePiece.DAME,Couleur.NOIR))
        (self.matCases)[0][4]=CasePlateau(Piece(TypePiece.ROI,Couleur.NOIR))
        (self.matCases)[0][5]=CasePlateau(Piece(TypePiece.FOU,Couleur.NOIR))
        (self.matCases)[0][6]=CasePlateau(Piece(TypePiece.CAVALIER,Couleur.NOIR))
        (self.matCases)[0][7]=CasePlateau(Piece(TypePiece.TOUR,Couleur.NOIR))
        for j in range(8):
            (self.matCases)[1][j]=CasePlateau(Piece(TypePiece.PION,Couleur.NOIR))
        (self.matCases)[7][0]=CasePlateau(Piece(TypePiece.TOUR,Couleur.BLANC))
        (self.matCases)[7][1]=CasePlateau(Piece(TypePiece.CAVALIER,Couleur.BLANC))
        (self.matCases)[7][2]=CasePlateau(Piece(TypePiece.FOU,Couleur.BLANC))
        (self.matCases)[7][3]=CasePlateau(Piece(TypePiece.DAME,Couleur.BLANC))
        (self.matCases)[7][4]=CasePlateau(Piece(TypePiece.ROI,Couleur.BLANC))
        (self.matCases)[7][5]=CasePlateau(Piece(TypePiece.FOU,Couleur.BLANC))
        (self.matCases)[7][6]=CasePlateau(Piece(TypePiece.CAVALIER,Couleur.BLANC))
        (self.matCases)[7][7]=CasePlateau(Piece(TypePiece.TOUR,Couleur.BLANC))
        for j in range(8):
            (self.matCases)[6][j]=CasePlateau(Piece(TypePiece.PION,Couleur.BLANC))
                  

    def liste_piece(self):
        liste=[]
        for i in range(8):
            for j in range(8):
                if(((self.matCases)[i][j].piece)!=None):
                    d={}
                    d['type']=((self.matCases)[i][j]).piece.type
                    d['nom']=((self.matCases)[i][j]).piece.type
                    d['couleur']=((self.matCases)[i][j]).piece.couleur
                    d['emplacement']=Pos(i+1,j+1).get_emplacement
                    liste.append(d)
        return liste

    def piece_a_position(self, pos):
        return ((self.matCases)[(pos.ligne)-1][(pos.colonne)-1]).piece
