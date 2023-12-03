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
        self.interface = Interface()
        self.plateau=Plateau()
        self.joueurCourant=Couleur.BLANC 
    

    def est_case_joueur(self, pos, joueur):
        if(1<=pos.ligne<=8 and 1<=pos.colonne<=8):
            if(self.plateau.matCases[pos.ligne-1][pos.colonne-1].piece!=None):
                if((self.plateau.matCases)[pos.ligne-1][pos.colonne-1].piece.couleur==joueur):
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False


    def est_case_joueur_inverse(self, pos, joueur):
        if(1<=pos.ligne<=8 and 1<=pos.colonne<=8):
            if(self.plateau.matCases[pos.ligne-1][pos.colonne-1].piece!=None):
                if(self.plateau.matCases[pos.ligne-1][pos.colonne-1].piece.couleur==~joueur):
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False


    def liste_mouvement_cavalier(self, pos):
        moveCav=[]
        depCav=[Pos(2,1),Pos(2,-1),Pos(-2,1),Pos(-2,-1),Pos(1,2),Pos(1,-2),Pos(-1,2),Pos(-1,-2)]
        for dep in depCav:
            npos=pos+dep
            if(1<=npos.ligne<=8 and 1<=npos.colonne<=8):
                if(self.plateau.matCases[npos.ligne-1][npos.colonne-1].est_occupe()==True):
                    if(self.plateau.matCases[pos.ligne-1][pos.colonne-1].piece.couleur!=self.plateau.matCases[npos.ligne-1][npos.colonne-1].piece.couleur):
                        moveCav.append(npos)
                else:
                    moveCav.append(npos)
        return moveCav

        

    def liste_mouvement_fou(self, pos):
        moveCav=[]
        depCav=[(1,1),(1,-1),(-1,1),(-1,-1)]
        for dep in depCav:
            j=1
            flag=True
            while (j<=max(self.plateau.NLIGNES,self.plateau.NCOLONNES) and flag):
                npos=pos+Pos(dep[0]*j,dep[1]*j)
                if(not(1<=npos.ligne<=8 and 1<=npos.colonne<=8)):
                    flag=False
                    continue
                if(self.plateau.matCases[npos.ligne-1][npos.colonne-1].est_occupe()==True):
                    if(self.plateau.matCases[pos.ligne-1][pos.colonne-1].piece.couleur!=self.plateau.matCases[npos.ligne-1][npos.colonne-1].piece.couleur):
                        moveCav.append(npos)
                    flag=False
                else:
                    moveCav.append(npos)
                j+=1
        return moveCav

    def liste_mouvement_tour(self, pos):
        moveCav=[]
        depCav=[(1,0),(-1,0),(0,1),(0,-1)]
        for dep in depCav:
            j=1
            flag=True
            while (j<=max(self.plateau.NLIGNES,self.plateau.NCOLONNES) and flag):
                npos=pos+Pos(dep[0]*j,dep[1]*j)
                if(not(1<=npos.ligne<=8 and 1<=npos.colonne<=8)):
                    flag=False
                    continue
                if(self.plateau.matCases[npos.ligne-1][npos.colonne-1].est_occupe()==True):
                    if(self.plateau.matCases[pos.ligne-1][pos.colonne-1].piece.couleur!=self.plateau.matCases[npos.ligne-1][npos.colonne-1].piece.couleur):
                        moveCav.append(npos)
                    flag=False
                else:
                    moveCav.append(npos)
                j+=1
        return moveCav

    def liste_mouvement_dame(self, pos):
        moveCav=[]
        depCav=[(1,1),(1,-1),(-1,1),(-1,-1),(1,0),(-1,0),(0,1),(0,-1)]
        for dep in depCav:
            j=1
            flag=True
            while (j<=max(self.plateau.NLIGNES,self.plateau.NCOLONNES) and flag):
                npos=pos+Pos(dep[0]*j,dep[1]*j)
                if(not(1<=npos.ligne<=8 and 1<=npos.colonne<=8)):
                    flag=False
                    continue
                if(self.plateau.matCases[npos.ligne-1][npos.colonne-1].est_occupe()==True):
                    if(self.plateau.matCases[pos.ligne-1][pos.colonne-1].piece.couleur!=self.plateau.matCases[npos.ligne-1][npos.colonne-1].piece.couleur):
                        moveCav.append(npos)
                    flag=False
                else:
                    moveCav.append(npos)
                j+=1
        return moveCav
    def liste_mouvement_roi(self, pos, juste_mouvement=False):
        moveCav=[]
        depCav=[Pos(1,0),Pos(-1,0),Pos(0,1),Pos(0,-1),Pos(1,1),Pos(1,-1),Pos(-1,1),Pos(-1,-1)]
        for dep in depCav:
            npos=pos+dep
            if(1<=npos.ligne<=8 and 1<=npos.colonne<=8):
                if(self.plateau.matCases[npos.ligne-1][npos.colonne-1].est_occupe()==True):
                    if(self.plateau.matCases[pos.ligne-1][pos.colonne-1].piece.couleur!=self.plateau.matCases[npos.ligne-1][npos.colonne-1].piece.couleur):
                        if(juste_mouvement==True):
                            moveCav.append(npos)
                        else:
                            roi=self.plateau.matCases[pos.ligne-1][pos.colonne-1].piece
                            piece=self.plateau.matCases[npos.ligne-1][npos.colonne-1].piece
                            self.plateau.matCases[npos.ligne-1][npos.colonne-1].piece=roi
                            self.plateau.matCases[pos.ligne-1][pos.colonne-1].piece=None
                            if(self.est_echec(self.plateau.matCases[npos.ligne-1][npos.colonne-1].piece.couleur)==False):
                                moveCav.append(npos)
                            self.plateau.matCases[pos.ligne-1][pos.colonne-1].piece=roi
                            self.plateau.matCases[npos.ligne-1][npos.colonne-1].piece=piece
                else:
                    moveCav.append(npos)
        return moveCav

    def liste_mouvement_pion(self, pos):
        liste=[]
        if(self.plateau.matCases[pos.ligne-1][pos.colonne-1].piece.couleur==Couleur.NOIR):
            dep=[(1,0),(1,-1),(1,1)]
        elif(self.plateau.matCases[pos.ligne-1][pos.colonne-1].piece.couleur==Couleur.BLANC):
            dep=[(-1,0),(-1,1),(-1,-1)]
        for deplacement in dep:
            posf=pos+Pos(deplacement[0],deplacement[1])
            if(1<=posf.ligne<=8 and 1<=posf.colonne<=8):
                if(deplacement[1]==0):
                    if(self.plateau.matCases[posf.ligne-1][posf.colonne-1].est_occupe()==False):
                        liste.append(posf)
                        if(self.plateau.matCases[pos.ligne-1][pos.colonne-1].piece.couleur==Couleur.NOIR and pos.ligne==2):
                            posd=pos+Pos(2,0)
                            if(self.plateau.matCases[posd.ligne-1][posd.colonne-1].est_occupe()==False):
                                liste.append(posd)
                        elif(self.joueurCourant==Couleur.BLANC and pos.ligne==7):
                            posd=pos+Pos(-2,0)
                            if(self.plateau.matCases[posd.ligne-1][posd.colonne-1].est_occupe()==False):
                                liste.append(posd)
                else:
                    if(self.plateau.matCases[posf.ligne-1][posf.colonne-1].est_occupe()==True):
                        if(self.plateau.matCases[pos.ligne-1][pos.colonne-1].piece.couleur!=self.plateau.matCases[posf.ligne-1][posf.colonne-1].piece.couleur):
                            liste.append(posf)
        return liste

                                

    def est_mouvement_valide(self, pos_depart, pos_fin):
        valide=False
        if(1<=pos_depart.ligne<=8 and 1<=pos_depart.colonne<=8):
            if(self.plateau.matCases[pos_depart.ligne-1][pos_depart.colonne-1].est_occupe()==True):
                if(self.plateau.matCases[pos_depart.ligne-1][pos_depart.colonne-1].piece.type==TypePiece.CAVALIER):
                    for pos in self.liste_mouvement_cavalier(pos_depart):
                        if(pos==pos_fin):
                            valide=True
                            break
                elif(self.plateau.matCases[pos_depart.ligne-1][pos_depart.colonne-1].piece.type==TypePiece.FOU):
                    for pos in self.liste_mouvement_fou(pos_depart):
                        if(pos==pos_fin):
                            valide=True
                            break
                elif(self.plateau.matCases[pos_depart.ligne-1][pos_depart.colonne-1].piece.type==TypePiece.TOUR):
                    for pos in self.liste_mouvement_tour(pos_depart):
                        if(pos==pos_fin):
                            valide=True
                            break
                elif(self.plateau.matCases[pos_depart.ligne-1][pos_depart.colonne-1].piece.type==TypePiece.DAME):
                    for pos in self.liste_mouvement_dame(pos_depart):
                        if(pos==pos_fin):
                            valide=True
                            break
                elif(self.plateau.matCases[pos_depart.ligne-1][pos_depart.colonne-1].piece.type==TypePiece.PION):
                    for pos in self.liste_mouvement_pion(pos_depart):
                        if(pos==pos_fin):
                            valide=True
                            break
                if(self.plateau.matCases[pos_depart.ligne-1][pos_depart.colonne-1].piece.type==TypePiece.ROI):
                    for pos in self.liste_mouvement_roi(pos_depart):
                        if(pos==pos_fin):
                            valide=True
                            break
        return valide            
    
    def liste_mouvement_valide_joueur(self, joueur, juste_mouvement=False):
        listemouv=[]
        for i in range(self.plateau.NLIGNES):
            for j in range(self.plateau.NCOLONNES):
                if(self.plateau.matCases[i][j].est_occupe()==True):
                    if(self.plateau.matCases[i][j].piece.couleur==joueur):
                        if(self.plateau.matCases[i][j].piece.type==TypePiece.PION):
                            listemouv.extend(self.liste_mouvement_pion(Pos(i+1,j+1)))
            
                        elif(self.plateau.matCases[i][j].piece.type==TypePiece.CAVALIER):
                            listemouv.extend(self.liste_mouvement_cavalier(Pos(i+1,j+1)))
                        
                        elif(self.plateau.matCases[i][j].piece.type==TypePiece.FOU):
                            listemouv.extend(self.liste_mouvement_fou(Pos(i+1,j+1)))
                        
                        elif(self.plateau.matCases[i][j].piece.type==TypePiece.TOUR):
                            listemouv.extend(self.liste_mouvement_tour(Pos(i+1,j+1)))
                        
                        elif(self.plateau.matCases[i][j].piece.type==TypePiece.DAME):
                            listemouv.extend(self.liste_mouvement_dame(Pos(i+1,j+1)))
                        
                        elif(self.plateau.matCases[i][j].piece.type==TypePiece.ROI):
                            listemouv.extend(self.liste_mouvement_roi(Pos(i+1,j+1),juste_mouvement))  
        return listemouv                      
                        
                        


    def liste_mouvement_valide_pos(self, pos, juste_mouvement=False):
        if(self.plateau.matCases[pos.ligne-1][pos.colonne-1].piece.type==TypePiece.CAVALIER):
            return self.liste_mouvement_cavalier(pos)
        elif(self.plateau.matCases[pos.ligne-1][pos.colonne-1].piece.type==TypePiece.FOU):
            return self.liste_mouvement_fou(pos)
        elif(self.plateau.matCases[pos.ligne-1][pos.colonne-1].piece.type==TypePiece.TOUR):
            return self.liste_mouvement_tour(pos)

        elif(self.plateau.matCases[pos.ligne-1][pos.colonne-1].piece.type==TypePiece.DAME):
            return self.liste_mouvement_dame(pos)
                
        elif(self.plateau.matCases[pos.ligne-1][pos.colonne-1].piece.type==TypePiece.PION):
            return self.liste_mouvement_pion(pos)

        elif(self.plateau.matCases[pos.ligne-1][pos.colonne-1].piece.type==TypePiece.ROI):
            return self.liste_mouvement_roi(pos,juste_mouvement)
        

    def pos_roi_joueur(self, joueur):
        for i in range(self.plateau.NLIGNES):
            for j in range(self.plateau.NCOLONNES):
                    if(self.plateau.matCases[i][j].est_occupe()==True):
                        if(self.plateau.matCases[i][j].piece.couleur==joueur and self.plateau.matCases[i][j].piece.type==TypePiece.ROI):
                            pos_roi=Pos(i+1,j+1)
                            return pos_roi
        return None
    def est_echec(self, joueur):
        pos_roi=self.pos_roi_joueur(joueur)
        if(type(pos_roi)==type(None)):
            return True
        mouvement_adv=self.liste_mouvement_valide_joueur(~joueur)
        echec=False
        for mouv in mouvement_adv:
            if(pos_roi==mouv):
                echec=True
                break
        return echec
    def est_en_echec_apres_mouvement(self, pos_depart, pos_fin, joueur):
        piece=self.plateau.matCases[pos_depart.ligne-1][pos_depart.colonne-1].piece
        self.plateau.matCases[pos_depart.ligne-1][pos_depart.colonne-1].piece=None
        self.plateau.matCases[pos_fin.ligne-1][pos_fin.colonne-1].piece=piece
        echec=self.est_echec(joueur)
        self.plateau.matCases[pos_fin.ligne-1][pos_fin.colonne-1].piece=None
        self.plateau.matCases[pos_depart.ligne-1][pos_depart.colonne-1].piece=piece
        return echec


    def est_echec_et_mat(self, joueur):
        position_roi=self.pos_roi_joueur(joueur)
        if(type(position_roi)==type(None)):
           return True
        liste_roi=self.liste_mouvement_roi(position_roi)
        for mouv in liste_roi:
            if(self.est_en_echec_apres_mouvement(position_roi,mouv,joueur)==False):
                return False
        for i in range(self.plateau.NLIGNES):
            for j in range(self.plateau.NCOLONNES):
                pos=Pos(i+1,j+1)
                if(self.est_case_joueur(pos,joueur)==True):
                    liste=self.liste_mouvement_valide_pos(pos)
                    for mov in liste:
                        if(self.est_en_echec_apres_mouvement(pos,mov,joueur)==False):
                            return False
        if(self.est_echec(joueur)==True):
            return True
        else:
            return False 



