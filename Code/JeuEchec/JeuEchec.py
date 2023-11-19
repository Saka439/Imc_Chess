import sys
import os

chemin_dossier_1 = os.path.dirname(os.path.realpath(__file__)) + '/../Plateau'
chemin_dossier_2 = os.path.dirname(os.path.realpath(__file__)) + '/../Interface'


if chemin_dossier_1 not in sys.path:
    sys.path.append(chemin_dossier_1)
if chemin_dossier_2 not in sys.path:
    sys.path.append(chemin_dossier_2)


from Plateau import*
from Interface import*


class JeuEchec:

    def __init__(self):

        if not('unittest' in sys.modules.keys()):
           self.interface = Interface()
	pass

    def est_case_joueur(self, pos, joueur):
        pass

    def est_case_joueur_inverse(self, pos, joueur):
        pass

    def liste_mouvement_cavalier(self, pos):
        pass

    def liste_mouvement_fou(self, pos):
        pass

    def liste_mouvement_tour(self, pos):
        pass

    def liste_mouvement_dame(self, pos):
        pass

    def liste_mouvement_roi(self, pos, juste_mouvement=False):
        pass

    def liste_mouvement_pion(self, pos):
        pass

    def est_mouvement_valide(self, pos_depart, pos_fin):
	pass

    def liste_mouvement_valide_joueur(self, joueur, juste_mouvement=False):
        pass

    def liste_mouvement_valide_pos(self, pos, juste_mouvement=False):
        pass

    def pos_roi_joueur(self, joueur):
        pass

    def est_echec(self, joueur):
        pass


    def est_echec_et_mat(self, joueur):
        pass