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
        pass

    def ajoute_piece(self, piece, pos):
        pass

    def bouge_piece(self, pos_depart, pos_fin):
        pass

    def est_case_occupe(self, pos):
        pass

    def init_partie(self):
        pass


    def liste_piece(self):
        pass

    def piece_a_position(self, pos):
        pass
