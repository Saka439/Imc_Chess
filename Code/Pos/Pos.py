class Pos:
    def __init__(self, ligne_emplacement_ind, colonne=None):
        pass

    @property
    def get_emplacement(self):
        pass


    def __add__(self, addPos):
        pass

    def ind(self):
        pass

    @staticmethod
    def est_hors_plateau(pos_list):
        pass

    @staticmethod
    def est_dans_liste_pos(pos, listePos):
        pass

    def __str__(self):
        pass

    def __eq__(self, pos):
        pass

    #Fournie
    def __hash__(self):
        return hash((self.ligne, self.colonne))