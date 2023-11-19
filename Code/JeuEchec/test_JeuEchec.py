import unittest
import os
import sys
import tempfile

from JeuEchec import*  

class TestJeuEchec(unittest.TestCase):

    def setUp(self):
        self.jeu = JeuEchec()
        self.jeu.plateau.init_partie()

    def test_est_case_joueur(self):
        pos_roi_blanc = Pos("b8")
        self.assertTrue(self.jeu.est_case_joueur(pos_roi_blanc, Couleur.BLANC))
        self.assertFalse(self.jeu.est_case_joueur(pos_roi_blanc, Couleur.NOIR))

    def test_est_case_joueur_inverse(self):
        pos_roi_noir = Pos("e1")
        self.assertTrue(self.jeu.est_case_joueur_inverse(pos_roi_noir, Couleur.BLANC))
        self.assertFalse(self.jeu.est_case_joueur_inverse(pos_roi_noir, Couleur.NOIR))

    def test_liste_mouvement_cavalier(self):
        pos_cavalier_blanc = Pos("b8")
        mouvements = self.jeu.liste_mouvement_cavalier(pos_cavalier_blanc)
        self.assertIn(Pos("a6"), mouvements)
        self.assertIn(Pos("c6"), mouvements)

    def test_liste_mouvement_cavalier_avec_capture(self):
        self.jeu.plateau.init_partie()
        pos_cavalier_blanc = Pos("b8")
        pos_piece_adverse = Pos("a6")  # Position où le cavalier peut se déplacer et capturer

        # Placer une pièce adverse sur la position cible
        piece_adverse = Piece(TypePiece.PION, Couleur.NOIR)
        self.jeu.plateau.ajoute_piece(piece_adverse, pos_piece_adverse)

        mouvements = self.jeu.liste_mouvement_cavalier(pos_cavalier_blanc)
        self.assertIn(pos_piece_adverse, mouvements)

        # Capturer la pièce adverse
        self.jeu.plateau.bouge_piece(pos_cavalier_blanc, pos_piece_adverse)
        self.assertIsNone(self.jeu.plateau.piece_a_position(pos_cavalier_blanc))
        self.assertEqual(self.jeu.plateau.piece_a_position(pos_piece_adverse).type, TypePiece.CAVALIER)

    def test_liste_mouvement_fou(self):
        pos_fou_blanc = Pos("e5")
        self.jeu.plateau.ajoute_piece(Piece(TypePiece.FOU, Couleur.BLANC), pos_fou_blanc)

        # Liste des mouvements attendus
        mouvements_attendus = [Pos("b2"), Pos("c3"), Pos("d4"), Pos("d6"), Pos("f4"), 
                               Pos("f6"), Pos("g3"), Pos("h2")]

        # Obtenir la liste des mouvements possibles du fou
        mouvements_reels = self.jeu.liste_mouvement_fou(pos_fou_blanc)

        # Vérifier que chaque mouvement attendu est présent dans la liste des mouvements réels
        for mouvement in mouvements_attendus:
            self.assertIn(mouvement, mouvements_reels)


    def test_liste_mouvement_fou_avec_capture(self):
        self.jeu.plateau.init_partie()
        pos_fou_blanc = Pos("e5")
        pos_piece_adverse = Pos("d6")  # Position sur la diagonale où le fou peut se déplacer et capturer

        # Placer une pièce adverse sur la position cible
        piece_adverse = Piece(TypePiece.PION, Couleur.NOIR)
        self.jeu.plateau.ajoute_piece(piece_adverse, pos_piece_adverse)

        # Ajouter un fou blanc et vérifier ses mouvements possibles
        self.jeu.plateau.ajoute_piece(Piece(TypePiece.FOU, Couleur.BLANC), pos_fou_blanc)
        mouvements = self.jeu.liste_mouvement_fou(pos_fou_blanc)
        self.assertIn(pos_piece_adverse, mouvements)

        # Capturer la pièce adverse
        self.jeu.plateau.bouge_piece(pos_fou_blanc, pos_piece_adverse)
        self.assertIsNone(self.jeu.plateau.piece_a_position(pos_fou_blanc))
        self.assertEqual(self.jeu.plateau.piece_a_position(pos_piece_adverse).type, TypePiece.FOU)
    
    def test_liste_mouvement_tour(self):
        pos_tour_noire = Pos("d4")
        self.jeu.plateau.ajoute_piece(Piece(TypePiece.TOUR, Couleur.NOIR), pos_tour_noire)

        # Liste des mouvements attendus pour la tour
        mouvements_attendus = [Pos("a4"), Pos("b4"), Pos("c4"), Pos("d3"), Pos("d5"), Pos("d6"), 
                               Pos("d7"), Pos("e4"), Pos("f4"), Pos("g4"), Pos("h4")]

        # Obtenir la liste des mouvements possibles de la tour
        mouvements_reels = self.jeu.liste_mouvement_tour(pos_tour_noire)

        # Vérifier que chaque mouvement attendu est présent dans la liste des mouvements réels
        for mouvement in mouvements_attendus:
            self.assertIn(mouvement, mouvements_reels)
    
    def test_liste_mouvement_tour_avec_capture(self):
        self.jeu.plateau.init_partie()
        pos_tour_noire = Pos("d4")
        pos_piece_adverse = Pos("d6")  # Position où la tour peut se déplacer et capturer

        # Placer une pièce adverse sur la position cible
        piece_adverse = Piece(TypePiece.PION, Couleur.BLANC)
        self.jeu.plateau.ajoute_piece(piece_adverse, pos_piece_adverse)

        # Ajouter une tour noire et vérifier ses mouvements possibles
        self.jeu.plateau.ajoute_piece(Piece(TypePiece.TOUR, Couleur.NOIR), pos_tour_noire)
        mouvements = self.jeu.liste_mouvement_tour(pos_tour_noire)
        self.assertIn(pos_piece_adverse, mouvements)

        # Capturer la pièce adverse
        self.jeu.plateau.bouge_piece(pos_tour_noire, pos_piece_adverse)
        self.assertIsNone(self.jeu.plateau.piece_a_position(pos_tour_noire))
        self.assertEqual(self.jeu.plateau.piece_a_position(pos_piece_adverse).type, TypePiece.TOUR)
    
    def test_liste_mouvement_dame(self):
        pos_dame = Pos("d4")
        self.jeu.plateau.ajoute_piece(Piece(TypePiece.DAME, Couleur.BLANC), pos_dame)

        # Liste des mouvements attendus pour la dame
        mouvements_attendus = [ Pos("a4"), Pos("b2"), Pos("b4"), Pos("b6"), Pos("c3"), 
                                Pos("c4"), Pos("c5"), Pos("d2"), Pos("d3"), Pos("d5"), 
                                Pos("d6"), Pos("e3"), Pos("e4"), Pos("e5"), Pos("f2"), 
                                Pos("f4"), Pos("f6"), Pos("g4"), Pos("h4")]

        # Obtenir la liste des mouvements possibles de la dame
        mouvements_reels = self.jeu.liste_mouvement_dame(pos_dame)

        # Vérifier que chaque mouvement attendu est présent dans la liste des mouvements réels
        for mouvement in mouvements_attendus:
            self.assertIn(mouvement, mouvements_reels)

    def test_liste_mouvement_dame_avec_capture(self):
        self.jeu.plateau.init_partie()
        pos_dame = Pos("d4")
        pos_piece_adverse = Pos("d6")  # Position où la dame peut se déplacer et capturer

        # Placer une pièce adverse sur la position cible
        piece_adverse = Piece(TypePiece.PION, Couleur.NOIR)
        self.jeu.plateau.ajoute_piece(piece_adverse, pos_piece_adverse)

        # Ajouter une dame blanche et vérifier ses mouvements possibles
        self.jeu.plateau.ajoute_piece(Piece(TypePiece.DAME, Couleur.BLANC), pos_dame)
        mouvements = self.jeu.liste_mouvement_dame(pos_dame)
        self.assertIn(pos_piece_adverse, mouvements)

        # Capturer la pièce adverse
        self.jeu.plateau.bouge_piece(pos_dame, pos_piece_adverse)
        self.assertIsNone(self.jeu.plateau.piece_a_position(pos_dame))
        self.assertEqual(self.jeu.plateau.piece_a_position(pos_piece_adverse).type, TypePiece.DAME)

    def test_liste_mouvement_dame_avec_multiples_captures(self):
        self.jeu.plateau.init_partie()
        pos_dame = Pos("d4")

        # Placer des pièces adverses sur les chemins de la dame
        positions_adverses = [Pos("d6"), Pos("b4"), Pos("f4"), Pos("b2"), Pos("f6")]
        for pos in positions_adverses:
            self.jeu.plateau.ajoute_piece(Piece(TypePiece.PION, Couleur.NOIR), pos)

        # Ajouter une dame blanche et vérifier ses mouvements possibles
        self.jeu.plateau.ajoute_piece(Piece(TypePiece.DAME, Couleur.BLANC), pos_dame)
        mouvements = self.jeu.liste_mouvement_dame(pos_dame)

        for pos_adverse in positions_adverses:
            self.assertIn(pos_adverse, mouvements)

        # Tester une capture sur chaque chemin
        for pos_capture in positions_adverses:
            self.jeu.plateau.bouge_piece(pos_dame, pos_capture)
            self.assertIsNone(self.jeu.plateau.piece_a_position(pos_dame))
            self.assertEqual(self.jeu.plateau.piece_a_position(pos_capture).type, TypePiece.DAME)
            self.jeu.plateau.ajoute_piece(Piece(TypePiece.DAME, Couleur.BLANC), pos_dame)  # Repositionner la dame pour le prochain test
    
    def test_liste_mouvement_roi(self):
        # Supposons que le roi est déplacé pour tester les mouvements
        pos_roi = Pos("d4")
        self.jeu.plateau.ajoute_piece(Piece(TypePiece.ROI, Couleur.BLANC), pos_roi)

        # Liste des mouvements attendus pour le roi
        mouvements_attendus = [Pos("c4"), Pos("c5"),Pos("d5"),Pos("e4"), Pos("e5")]

        # Obtenir la liste des mouvements possibles du roi
        mouvements_reels = self.jeu.liste_mouvement_roi(pos_roi)

        # Vérifier que chaque mouvement attendu est présent dans la liste des mouvements réels
        for mouvement in mouvements_attendus:
            self.assertIn(mouvement, mouvements_reels)

    def test_liste_mouvement_roi_avec_multiples_captures(self):
        self.jeu.plateau.init_partie()
        pos_roi = Pos("d4")

        # Placer des pièces adverses autour du roi
        positions_adverses = [Pos("c4"), Pos("c5"), Pos("e4"), Pos("e5")]
        for pos in positions_adverses:
            self.jeu.plateau.ajoute_piece(Piece(TypePiece.PION, Couleur.NOIR), pos)

        # Ajouter un roi blanc et vérifier ses mouvements possibles
        self.jeu.plateau.ajoute_piece(Piece(TypePiece.ROI, Couleur.BLANC), pos_roi)
        mouvements = self.jeu.liste_mouvement_roi(pos_roi)

        for pos_adverse in positions_adverses:
            self.assertIn(pos_adverse, mouvements)

        # Tester une capture sur chaque position
        for pos_capture in positions_adverses:
            self.jeu.plateau.bouge_piece(pos_roi, pos_capture)
            self.assertIsNone(self.jeu.plateau.piece_a_position(pos_roi))
            self.assertEqual(self.jeu.plateau.piece_a_position(pos_capture).type, TypePiece.ROI)
            self.jeu.plateau.ajoute_piece(Piece(TypePiece.ROI, Couleur.BLANC), pos_roi)  # Repositionner le roi pour le prochain test

    def test_liste_mouvement_pion(self):
        # Tester les mouvements initiaux du pion blanc
        pos_pion_blanc = Pos("b7")
        self.jeu.plateau.ajoute_piece(Piece(TypePiece.PION, Couleur.BLANC), pos_pion_blanc)
        mouvements_blanc = self.jeu.liste_mouvement_pion(pos_pion_blanc)
        self.assertIn(Pos("b6"), mouvements_blanc)  # Avance d'une case
        self.assertIn(Pos("b5"), mouvements_blanc)  # Avance de deux cases

        # Tester les mouvements initiaux du pion noir
        pos_pion_noir = Pos("g2")
        self.jeu.plateau.ajoute_piece(Piece(TypePiece.PION, Couleur.NOIR), pos_pion_noir)
        mouvements_noir = self.jeu.liste_mouvement_pion(pos_pion_noir)
        self.assertIn(Pos("g3"), mouvements_noir)
        self.assertIn(Pos("g4"), mouvements_noir)

    def test_liste_mouvement_pion_apres_Deplacement(self):
        # Tester un mouvement d'une case après le premier déplacement
        pos_pion_blanc = Pos("b7")
        self.jeu.plateau.bouge_piece(pos_pion_blanc, Pos("b6"))
        mouvements_blanc_apres_deplacement = self.jeu.liste_mouvement_pion(Pos("b6"))
        self.assertIn(Pos("b5"), mouvements_blanc_apres_deplacement)
        self.assertNotIn(Pos("b4"), mouvements_blanc_apres_deplacement)

    def test_liste_mouvement_pion_avec_prises(self):
        # Tester les mouvements initiaux et les prises en diagonale du pion blanc
        pos_pion_blanc = Pos("b7")
        self.jeu.plateau.ajoute_piece(Piece(TypePiece.PION, Couleur.BLANC), pos_pion_blanc)

        # Placer des pièces adverses pour les prises en diagonale
        pos_adverse_gauche = Pos("a6")
        pos_adverse_droite = Pos("c6")
        self.jeu.plateau.ajoute_piece(Piece(TypePiece.PION, Couleur.NOIR), pos_adverse_gauche)
        self.jeu.plateau.ajoute_piece(Piece(TypePiece.PION, Couleur.NOIR), pos_adverse_droite)

        mouvements_blanc = self.jeu.liste_mouvement_pion(pos_pion_blanc)
        self.assertIn(Pos("b6"), mouvements_blanc)  # Avance d'une case
        self.assertIn(Pos("b5"), mouvements_blanc)  # Avance de deux cases
        self.assertIn(pos_adverse_gauche, mouvements_blanc)  # Prise en diagonale gauche
        self.assertIn(pos_adverse_droite, mouvements_blanc)  # Prise en diagonale droite

        # Tester les mouvements initiaux du pion noir
        pos_pion_noir = Pos("g2")
        self.jeu.plateau.ajoute_piece(Piece(TypePiece.PION, Couleur.NOIR), pos_pion_noir)
        mouvements_noir = self.jeu.liste_mouvement_pion(pos_pion_noir)
        self.assertIn(Pos("g3"), mouvements_noir)
        self.assertIn(Pos("g4"), mouvements_noir)  # Avance d'une ou deux cases

    def test_pos_roi_joueur(self):
        pos_roi_blanc = self.jeu.pos_roi_joueur(Couleur.BLANC)
        self.assertEqual(pos_roi_blanc, Pos(8, 5))
        pos_roi_noir = self.jeu.pos_roi_joueur(Couleur.NOIR)
        self.assertEqual(pos_roi_noir, Pos(1, 5))

    def test_mouvement_valide_pour_differentes_pieces(self):
        self.jeu.plateau.init_partie()

        # Test pour un fou
        pos_fou = Pos(8, 3)  # Position initiale d'un fou blanc
        self.assertFalse(self.jeu.est_mouvement_valide(pos_fou, Pos(5, 6)))
        self.assertFalse(self.jeu.est_mouvement_valide(pos_fou, Pos(5, 5)))

        # Test pour une tour
        pos_tour = Pos(8, 1)  # Position initiale d'une tour blanche
        self.assertFalse(self.jeu.est_mouvement_valide(pos_tour, Pos(8, 4)))
        self.assertFalse(self.jeu.est_mouvement_valide(pos_tour, Pos(5, 1)))

        # Test pour un roi
        pos_roi = Pos(8, 5)  # Position initiale du roi blanc
        self.assertFalse(self.jeu.est_mouvement_valide(pos_roi, Pos(7, 5)))
        self.assertFalse(self.jeu.est_mouvement_valide(pos_roi, Pos(6, 5)))

        # Test pour un pion
        pos_pion = Pos(7, 2)  # Position initiale d'un pion blanc
        pos_pion_valide = Pos(5, 2)  # Avance de deux cases
        pos_pion_invalide = Pos(4, 2)  # Mouvement invalide (trop loin)
        self.assertTrue(self.jeu.est_mouvement_valide(pos_pion, pos_pion_valide))
        self.assertFalse(self.jeu.est_mouvement_valide(pos_pion, pos_pion_invalide))

    def test_mouvement_roi_sous_echec(self):
        # Placer le roi en situation d'échec et tester un mouvement
        self.jeu.plateau.init_partie()
        pos_roi_blanc = Pos(8, 5)
        pos_tour_noire = Pos(8, 8)
        self.jeu.plateau.ajoute_piece(Piece(TypePiece.TOUR, Couleur.NOIR), pos_tour_noire)
        mouvement_roi_invalide = Pos(7, 5)  # Reste sous échec
        self.assertFalse(self.jeu.est_mouvement_valide(pos_roi_blanc, mouvement_roi_invalide))

    def test_liste_mouvement_valide_joueur(self):
        self.jeu.plateau.init_partie()

        # Tester tous les mouvements pour un joueur au début du jeu
        mouvements_blancs = self.jeu.liste_mouvement_valide_joueur(Couleur.BLANC)
        mouvements_noirs = self.jeu.liste_mouvement_valide_joueur(Couleur.NOIR)

        # Vérifier le nombre de mouvements possibles pour chaque joueur au début du jeu
        self.assertEqual(len(mouvements_blancs), 20)  # 8 pions * 2 mouvements + 2 cavaliers * 2 mouvements
        self.assertEqual(len(mouvements_noirs), 20)

    def test_liste_mouvement_valide_joueur_scenario_simple(self):
        # Simuler quelques mouvements basiques
        self.jeu.plateau.init_partie()
        self.jeu.plateau.bouge_piece(Pos(2, 4), Pos(4, 4))  # Pion noir avance de deux cases
        self.jeu.plateau.bouge_piece(Pos(7, 4), Pos(5, 4))  # Pion blanc avance de deux cases
        self.jeu.plateau.bouge_piece(Pos(1, 2), Pos(3, 4))  # Cavalier noir se déplace

        mouvements_blancs = self.jeu.liste_mouvement_valide_joueur(Couleur.BLANC)
        mouvements_noirs = self.jeu.liste_mouvement_valide_joueur(Couleur.NOIR)

        self.assertEqual(len(mouvements_blancs), 27)
        self.assertEqual(len(mouvements_noirs), 28)

    def test_liste_mouvement_valide_joueur_scenario_elabore(self):
        # Initialiser la partie et effectuer une série de mouvements
        self.jeu.plateau.init_partie()

        # Mouvements pour les Blancs (8 mouvements)
        self.jeu.plateau.bouge_piece(Pos(2, 4), Pos(4, 4))  # Pion avance de deux cases
        self.jeu.plateau.bouge_piece(Pos(1, 2), Pos(3, 3))  # Cavalier se déplace
        self.jeu.plateau.bouge_piece(Pos(1, 7), Pos(3, 6))  # Cavalier se déplace
        self.jeu.plateau.bouge_piece(Pos(1, 6), Pos(3, 7))  # Cavalier se déplace
        self.jeu.plateau.bouge_piece(Pos(2, 3), Pos(4, 3))  # Pion avance de deux cases
        self.jeu.plateau.bouge_piece(Pos(1, 4), Pos(2, 4))  # Roi se déplace
        self.jeu.plateau.bouge_piece(Pos(1, 3), Pos(2, 3))  # Reine se déplace
        self.jeu.plateau.bouge_piece(Pos(1, 5), Pos(2, 5))  # Fou se déplace

        # Mouvements pour les Noirs (7 mouvements)
        self.jeu.plateau.bouge_piece(Pos(7, 4), Pos(5, 4))  # Pion avance de deux cases
        self.jeu.plateau.bouge_piece(Pos(8, 2), Pos(6, 3))  # Cavalier se déplace
        self.jeu.plateau.bouge_piece(Pos(8, 7), Pos(6, 6))  # Cavalier se déplace
        self.jeu.plateau.bouge_piece(Pos(8, 6), Pos(6, 7))  # Cavalier se déplace
        self.jeu.plateau.bouge_piece(Pos(7, 3), Pos(5, 3))  # Pion avance de deux cases
        self.jeu.plateau.bouge_piece(Pos(8, 4), Pos(7, 4))  # Roi se déplace
        self.jeu.plateau.bouge_piece(Pos(8, 3), Pos(7, 3))  # Reine se déplace

        # Calculer les mouvements valides pour chaque joueur après ces mouvements
        mouvements_blancs = self.jeu.liste_mouvement_valide_joueur(Couleur.BLANC)
        mouvements_noirs = self.jeu.liste_mouvement_valide_joueur(Couleur.NOIR)

        self.assertEqual(len(mouvements_blancs), 47)
        self.assertEqual(len(mouvements_noirs), 57)

    def test_liste_mouvement_valide_pos_pour_chaque_piece(self):
        # Test pour le Roi
        pos_roi = Pos(5, 5)
        self.jeu.plateau.ajoute_piece(Piece(TypePiece.ROI, Couleur.BLANC), pos_roi)
        mouvements_roi = self.jeu.liste_mouvement_valide_pos(pos_roi)
        self.assertIn(Pos(4, 4), mouvements_roi)

        # Test pour la Dame
        pos_dame = Pos(4, 4)
        self.jeu.plateau.ajoute_piece(Piece(TypePiece.DAME, Couleur.BLANC), pos_dame)
        mouvements_dame = self.jeu.liste_mouvement_valide_pos(pos_dame)
        self.assertIn(Pos(4, 5), mouvements_dame)

        # Test pour le Cavalier
        pos_cavalier = Pos(2, 1)
        self.jeu.plateau.ajoute_piece(Piece(TypePiece.CAVALIER, Couleur.BLANC), pos_cavalier)
        mouvements_cavalier = self.jeu.liste_mouvement_valide_pos(pos_cavalier)
        self.assertIn(Pos(3, 3), mouvements_cavalier)

        # Test pour la Tour
        pos_tour = Pos(6, 3)
        self.jeu.plateau.ajoute_piece(Piece(TypePiece.TOUR, Couleur.BLANC), pos_tour)
        mouvements_tour = self.jeu.liste_mouvement_valide_pos(pos_tour)
        self.assertIn(Pos(5, 3), mouvements_tour)

        # Test pour le Fou
        pos_fou = Pos(6, 3)
        self.jeu.plateau.ajoute_piece(Piece(TypePiece.FOU, Couleur.BLANC), pos_fou)
        mouvements_fou = self.jeu.liste_mouvement_valide_pos(pos_fou)
        self.assertIn(Pos(5, 4), mouvements_fou)

        # Test pour le Pion
        pos_pion = Pos(2, 2)
        self.jeu.plateau.ajoute_piece(Piece(TypePiece.PION, Couleur.NOIR), pos_pion)
        mouvements_pion = self.jeu.liste_mouvement_valide_pos(pos_pion)
        self.assertIn(Pos(3, 2), mouvements_pion)
    
    def test_est_echec(self):
        self.jeu.plateau.init_partie()

        # Placer le roi blanc en position d'échec
        pos_roi_blanc = Pos(5, 5)
        self.jeu.plateau.ajoute_piece(Piece(TypePiece.ROI, Couleur.BLANC), pos_roi_blanc)

        # Placer une tour noire de manière à mettre le roi blanc en échec
        pos_tour_noire = Pos(5, 8)
        self.jeu.plateau.ajoute_piece(Piece(TypePiece.TOUR, Couleur.NOIR), pos_tour_noire)

        # Vérifier que le roi blanc est en échec
        self.assertTrue(self.jeu.est_echec(Couleur.BLANC))

        # Bouger le roi blanc hors de la ligne de la tour
        pos_roi_blanc_safe = Pos(6, 5)
        self.jeu.plateau.bouge_piece(pos_roi_blanc, pos_roi_blanc_safe)

        # Vérifier que le roi blanc n'est plus en échec
        self.assertFalse(self.jeu.est_echec(Couleur.BLANC))

    def test_est_en_echec_apres_mouvement(self):
        self.jeu.plateau.init_partie()

        # Placer le roi blanc
        pos_roi_blanc = Pos(5, 5)
        self.jeu.plateau.ajoute_piece(Piece(TypePiece.ROI, Couleur.BLANC), pos_roi_blanc)

        # Placer une tour noire
        pos_tour_noire = Pos(5, 8)
        self.jeu.plateau.ajoute_piece(Piece(TypePiece.TOUR, Couleur.NOIR), pos_tour_noire)

        # Tester un mouvement qui ne met pas le roi en échec
        pos_pion_blanc = Pos(6, 5)
        self.jeu.plateau.ajoute_piece(Piece(TypePiece.PION, Couleur.BLANC), pos_pion_blanc)
        mouvement_safe = self.jeu.est_en_echec_apres_mouvement(pos_pion_blanc, Pos(6, 6), Couleur.BLANC)
        self.assertTrue(mouvement_safe)

        # Tester un mouvement qui met le roi en échec
        mouvement_danger = self.jeu.est_en_echec_apres_mouvement(pos_pion_blanc, Pos(5, 5), Couleur.BLANC)
        self.assertFalse(mouvement_danger)
    
    def test_est_echec_et_mat(self):
        self.jeu.plateau = Plateau()

        # Scénario 1: Échec et mat
        # Placer le roi blanc dans une position où il est en échec et mat
        pos_roi_blanc = Pos("d1")
        self.jeu.plateau.ajoute_piece(Piece(TypePiece.ROI, Couleur.BLANC), pos_roi_blanc)
        self.jeu.plateau.ajoute_piece(Piece(TypePiece.TOUR, Couleur.NOIR), Pos("a1"))
        self.jeu.plateau.ajoute_piece(Piece(TypePiece.DAME, Couleur.NOIR), Pos("d3"))

        self.assertTrue(self.jeu.est_echec_et_mat(Couleur.BLANC))

        # Scénario 2: Échec mais pas mat
        # Placer une pièce qui peut bloquer l'échec
        self.jeu.plateau.ajoute_piece(Piece(TypePiece.CAVALIER, Couleur.BLANC), Pos("f2"))
        self.jeu.plateau.ajoute_piece(Piece(TypePiece.FOU, Couleur.BLANC), Pos("b1"))
        self.assertFalse(self.jeu.est_echec_et_mat(Couleur.BLANC))

    def test_echec_et_mat_evite_par_sacrifice(self):
        self.jeu.plateau = Plateau()
        pos_roi_blanc = Pos("e1")
        self.jeu.plateau.ajoute_piece(Piece(TypePiece.ROI, Couleur.BLANC), pos_roi_blanc)
        self.jeu.plateau.ajoute_piece(Piece(TypePiece.DAME, Couleur.NOIR), Pos("e8"))
        self.jeu.plateau.ajoute_piece(Piece(TypePiece.PION, Couleur.BLANC), Pos("e2"))
        # Le pion blanc se sacrifie pour bloquer la dame noire
        self.assertFalse(self.jeu.est_echec_et_mat(Couleur.BLANC))

    def test_echec_et_mat_scenario(self):
        self.jeu.plateau = Plateau()
    
        # Pièces noires
        self.jeu.plateau.ajoute_piece(Piece(TypePiece.CAVALIER, Couleur.NOIR), Pos("b8"))
        self.jeu.plateau.ajoute_piece(Piece(TypePiece.ROI, Couleur.NOIR), Pos("e8"))
        self.jeu.plateau.ajoute_piece(Piece(TypePiece.FOU, Couleur.NOIR), Pos("f8"))
        self.jeu.plateau.ajoute_piece(Piece(TypePiece.TOUR, Couleur.NOIR), Pos("h8"))
        self.jeu.plateau.ajoute_piece(Piece(TypePiece.PION, Couleur.NOIR), Pos("a7"))
        self.jeu.plateau.ajoute_piece(Piece(TypePiece.PION, Couleur.NOIR), Pos("f7"))
        self.jeu.plateau.ajoute_piece(Piece(TypePiece.PION, Couleur.NOIR), Pos("g7"))
        self.jeu.plateau.ajoute_piece(Piece(TypePiece.DAME, Couleur.NOIR), Pos("e6")) 
        self.jeu.plateau.ajoute_piece(Piece(TypePiece.PION, Couleur.NOIR), Pos("e5")) 


        # Pièces blanches
        self.jeu.plateau.ajoute_piece(Piece(TypePiece.TOUR, Couleur.BLANC), Pos("d8"))
        self.jeu.plateau.ajoute_piece(Piece(TypePiece.FOU, Couleur.BLANC), Pos("g5"))
        self.jeu.plateau.ajoute_piece(Piece(TypePiece.PION, Couleur.BLANC), Pos("e4"))
        self.jeu.plateau.ajoute_piece(Piece(TypePiece.PION, Couleur.BLANC), Pos("a2"))
        self.jeu.plateau.ajoute_piece(Piece(TypePiece.PION, Couleur.BLANC), Pos("b2"))
        self.jeu.plateau.ajoute_piece(Piece(TypePiece.PION, Couleur.BLANC), Pos("c2")) 
        self.jeu.plateau.ajoute_piece(Piece(TypePiece.PION, Couleur.BLANC), Pos("f2"))
        self.jeu.plateau.ajoute_piece(Piece(TypePiece.PION, Couleur.BLANC), Pos("g2"))
        self.jeu.plateau.ajoute_piece(Piece(TypePiece.PION, Couleur.BLANC), Pos("h2"))        
        self.jeu.plateau.ajoute_piece(Piece(TypePiece.ROI, Couleur.BLANC), Pos("c1"))


        # La position actuelle est censée être un échec et mat pour les Noirs
        self.assertTrue(self.jeu.est_echec_et_mat(Couleur.NOIR))


if __name__ == '__main__':
    if not os.path.exists(os.path.dirname(os.path.realpath(__file__))+'/logs'):
        os.mkdir(os.path.dirname(os.path.realpath(__file__))+'/logs')
    with open(os.path.dirname(os.path.realpath(__file__))+'/logs/tests_results_JeuEchec.txt', 'w') as f:
        loader = unittest.TestLoader()
        suite = loader.loadTestsFromModule(sys.modules[__name__])
        unittest.TextTestRunner(f, verbosity=2).run(suite)