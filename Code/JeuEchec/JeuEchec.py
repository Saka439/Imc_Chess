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
        moveCav=[]
        depCav=[Pos(2,1),Pos(2,-1),Pos(-2,1),Pos(-2,-1),Pos(1,2),Pos(1,-2),Pos(-1,2),Pos(-1,-2)]
        for dep in depCav:
            npos=pos+dep
            if(1<=npos.ligne<=8 and 1<=npos.colonne<=8):
                if(self.plateau.matCases[npos.ligne-1][npos.colonne-1].est_occupe()==True):
                    if(self.joueurCourant!=self.plateau.matCases[npos.ligne-1][npos.colonne-1].piece.couleur):
                        moveCav.append(npos)
                else:
                    moveCav.append(npos)
        return moveCav

    def liste_mouvement_fou(self, pos):
        moveCav=[]
        depCav=[]
        for i in range(1,max(self.plateau.NLIGNES,self.plateau.NCOLONNES)):
            depCav.append(Pos(i,i))
            depCav.append(Pos(i,-i))
            depCav.append(Pos(-i,i))
            depCav.append(Pos(-i,-i))
        for dep in depCav:
            npos=pos+dep
            if(1<=npos.ligne<=8 and 1<=npos.colonne<=8):
                if(self.plateau.matCases[npos.ligne-1][npos.colonne-1].est_occupe()==True):
                    if(self.joueurCourant!=self.plateau.matCases[npos.ligne-1][npos.colonne-1].piece.couleur):
                        moveCav.append(npos)
                else:
                    moveCav.append(npos)
        return moveCav


    def liste_mouvement_tour(self, pos):
        moveCav=[]
        depCav=[]
        for i in range(1,max(self.plateau.NLIGNES,self.plateau.NCOLONNES)):
            depCav.append(Pos(i,0))
            depCav.append(Pos(-i,0))
            depCav.append(Pos(0,i))
            depCav.append(Pos(0,-i))
        for dep in depCav:
            npos=pos+dep
            if(1<=npos.ligne<=8 and 1<=npos.colonne<=8):
                if(self.plateau.matCases[npos.ligne-1][npos.colonne-1].est_occupe()==True):
                    if(self.joueurCourant!=self.plateau.matCases.piece.couleur):
                        moveCav.append(npos)
                else:
                    moveCav.append(npos)
    def liste_mouvement_dame(self, pos):
        moveCav=[]
        depCav=[]
        for i in range(1,max(self.plateau.NLIGNES,self.plateau.NCOLONNES)):
            depCav.append(Pos(i,i))
            depCav.append(Pos(i,-i))
            depCav.append(Pos(-i,i))
            depCav.append(Pos(-i,-i))
            depCav.append(Pos(i,0))
            depCav.append(Pos(-i,0))
            depCav.append(Pos(0,i))
            depCav.append(Pos(0,-i))
        for dep in depCav:
            npos=pos+dep
            if(1<=npos.ligne<=8 and 1<=npos.colonne<=8):
                if(self.plateau.matCases[npos.ligne-1][npos.colonne-1].est_occupe()==True):
                    if(self.joueurCourant!=self.plateau.matCases[npos.ligne-1][npos.colonne-1].piece.couleur):
                        moveCav.append(npos)
            else:    
                moveCav.append(npos)
        return moveCav

    def liste_mouvement_roi(self, pos, juste_mouvement=False):
        pass

    def liste_mouvement_pion(self, pos):
        liste=[]
        if(self.joueurCourant==Couleur.NOIR):
            dep=[(0,1),(-1,1),(1,1)]
        else:
            dep=[(0,-1),(1,-1)(-1,-1)]
        for deplacement in dep:
            posf=pos+Pos(deplacement[0],deplacement[1])
            if(1<=posf.ligne<=8 and 1<=posf.colonne<=8):
                if(deplacement[0]==0):
                    if(self.plateau.matCases[posf.ligne-1][posf.colonne-1].est_occupe()==False):
                        liste.append(posf)
                        if(self.joueurCourant==Couleur.NOIR and pos.ligne==2):
                            posd=pos+Pos(0,2)
                            if(self.plateau.matCases[posd.ligne-1][posd.colonne-1].est_occupe()==False):
                                liste.append(posd)
                        elif(self.joueurCourant==Couleur.BLANC and pos.ligne==7):
                            posd=pos+Pos(0,-2)
                            if(self.plateau.matCases[posd.ligne-1][posd.colonne-1].est_occupe()==False):
                                liste.append(posd)
                else:
                    if(self.plateau.matCases[posf.ligne-1][posf.colonne-1].est_occupe()==True):
                        liste.append(posf)
        return liste

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
