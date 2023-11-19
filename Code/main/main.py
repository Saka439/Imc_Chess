import sys
import os


chemin_dossier_1 = os.path.dirname(os.path.realpath(__file__)) + '/../JeuEchec'

if chemin_dossier_1 not in sys.path:
    sys.path.append(chemin_dossier_1)


from JeuEchec import*

def est_emplacement_valide(jeu, pos):
        
    return jeu.plateau.est_case_occupe(pos) and jeu.plateau.matCases[pos.ligne- 1][pos.colonne- 1].piece.couleur == jeu.joueurCourant and \
            (not(jeu.est_echec(jeu.joueurCourant)) or jeu.plateau.matCases[pos.ligne - 1][pos.colonne - 1].piece.type == TypePiece.ROI)

def tour_joueur_courant(jeu):
    # Sélection de la pièce à déplacer
    flag = True
    while flag:
        emplacement_depart = jeu.interface.saisir_emplacement()
        pos_depart = Pos(emplacement_depart)
        if est_emplacement_valide(jeu, pos_depart):
            flag = False

    # Sélection de la destination et déplacement de la pièce
    flag = True
    while flag:
        valid_moves = jeu.liste_mouvement_valide_pos(pos_depart)
        for move in valid_moves:
            jeu.interface.place_curseur(move.get_emplacement)

        emplacement_fin = jeu.interface.saisir_emplacement()
        pos_fin = Pos(emplacement_fin)
        if Pos.est_dans_liste_pos(pos_fin, valid_moves):
            jeu.plateau.bouge_piece(pos_depart, pos_fin)
            jeu.interface.piece_mangee(emplacement_fin)
            jeu.interface.enleve_curseur()
            jeu.interface.affiche_liste_piece(jeu.plateau.liste_piece())

            # Vérifiez si le pion atteint la dernière rangée pour la promotion
            piece_fin = jeu.plateau.piece_a_position(pos_fin)
            if piece_fin.type == TypePiece.PION and ((piece_fin.couleur == Couleur.BLANC and pos_fin.ligne == 1) or \
                                                    (piece_fin.couleur == Couleur.NOIR and pos_fin.ligne == 8)):
                jeu.interface.default_board()
                jeu.plateau.ajoute_piece(Piece(TypePiece.DAME, piece_fin.couleur), pos_fin)
                jeu.interface.affiche_liste_piece(jeu.plateau.liste_piece())

            flag = False


def jouer_partie(jeu):
    jeu.plateau.init_partie()
    jeu.interface.affiche_liste_piece(jeu.plateau.liste_piece())

    while not jeu.est_echec_et_mat(jeu.joueurCourant):

        tour_joueur_courant(jeu)
        jeu.joueurCourant = Couleur.NOIR if jeu.joueurCourant == Couleur.BLANC else Couleur.BLANC
        print(jeu.joueurCourant)
        if jeu.est_echec(jeu.joueurCourant):
            jeu.interface.place_curseur_roi(jeu.pos_roi_joueur(jeu.joueurCourant).get_emplacement)


if __name__ == '__main__':   
    jeu = JeuEchec()
    jeu.plateau.init_partie()
    jouer_partie(jeu)