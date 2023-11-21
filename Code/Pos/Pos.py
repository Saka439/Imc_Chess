class Pos:
    def __init__(self, ligne_emplacement_ind, colonne=None):
        liste=['a','b','c','d','e','f','g','h']
        if(type(ligne_emplacement_ind)==str):
            self.ligne=int(ligne_emplacement_ind[1])
            col=ligne_emplacement_ind[0]
            for i in liste:
                if(i==col):
                    break
            self.colonne=liste.index(i)+1
        elif(type(ligne_emplacement_ind)==int and colonne!=None):
            self.ligne=ligne_emplacement_ind
            self.colonne=colonne
        elif(type(ligne_emplacement_ind)==int and colonne==None):
            self.ligne=int(ligne_emplacement_ind/8)
            self.colonne=ligne_emplacement_ind%8

    @property
    def get_emplacement(self):
        liste=['a','b','c','d','e','f','g','h']
        for i in liste:
            if(liste.index(i)+1==self.colonne):
                break
        return i+str(self.ligne)


    def __add__(self, addPos):
        return Pos(self.ligne+addPos.ligne,self.colonne+addPos.colonne)

    def ind(self):
        indice=self.ligne*8+self.colonne+1
        return indice

    @staticmethod
    def est_hors_plateau(pos_list):
        liste_hors=[]
        if(1<=pos_list.ligne<=8 and 1<=pos_list.colonne<=8):
            liste_hors.append(False)
        else:
            liste_hors.append(True)
        return liste_hors

    @staticmethod
    def est_dans_liste_pos(pos, listePos):
        trouve=False
        for i in listePos:
            if(i.ligne==pos.ligne and i.colonne==pos.colonne):
                trouve=True
                break
        return trouve

    def __str__(self):
        return f"Ligne: {self.ligne}, Colonne: {self.colonne}, Emplacement: {self.get_emplacement}"

    def __eq__(self, pos):
        return (self.ligne==pos.ligne and self.colonne==pos.colonne)

    #Fournie
    def __hash__(self):
        return hash((self.ligne, self.colonne))
