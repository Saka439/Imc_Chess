import unittest
import os
import sys
import tempfile

from Plateau import* 

class TestPlateau(unittest.TestCase):

    def test_initialisation_plateau(self):
        plateau = Plateau()
        for ligne in plateau.matCases:
            for case in ligne:
                self.assertIsNone(case.piece)

    def test_ajoute_et_bouge_piece(self):
        plateau = Plateau()
        piece = Piece(TypePiece.FOU, Couleur.BLANC)
        pos_initiale = Pos(1, 1)
        pos_finale = Pos(2, 2)

        plateau.ajoute_piece(piece, pos_initiale)
        self.assertEqual(plateau.matCases[0][0].piece, piece)

        plateau.bouge_piece(pos_initiale, pos_finale)
        self.assertIsNone(plateau.matCases[0][0].piece)
        self.assertEqual(plateau.matCases[1][1].piece, piece)

    def test_est_case_occupe(self):
        plateau = Plateau()
        pos = Pos(1, 1)
        self.assertFalse(plateau.est_case_occupe(pos))

        piece = Piece(TypePiece.PION, Couleur.NOIR)
        plateau.ajoute_piece(piece, pos)
        self.assertTrue(plateau.est_case_occupe(pos))

    def test_init_partie(self):
        plateau = Plateau()
        plateau.init_partie()

        # Vérifier que les pions sont correctement placés
        for i in range(1, plateau.NCOLONNES + 1):
            self.assertIsInstance(plateau.piece_a_position(Pos(2, i)), Piece)
            self.assertIsInstance(plateau.piece_a_position(Pos(7, i)), Piece)
            self.assertEqual(plateau.piece_a_position(Pos(2, i)).type, TypePiece.PION)
            self.assertEqual(plateau.piece_a_position(Pos(7, i)).type, TypePiece.PION)

        # Vérifier que les autres pièces sont correctement placées
        for i, type_piece in [(1, TypePiece.TOUR), (2, TypePiece.CAVALIER),
                               (3, TypePiece.FOU), (4, TypePiece.DAME), (5, TypePiece.ROI)]:
            self.assertIsInstance(plateau.piece_a_position(Pos(1, i)), Piece)
            self.assertIsInstance(plateau.piece_a_position(Pos(8, i)), Piece)
            self.assertEqual(plateau.piece_a_position(Pos(1, i)).type, type_piece)
            self.assertEqual(plateau.piece_a_position(Pos(8, i)).type, type_piece)

        # Vérifier la couleur des pièces
        for i in range(1, plateau.NCOLONNES + 1):
            self.assertEqual(plateau.piece_a_position(Pos(2, i)).couleur, Couleur.NOIR)
            self.assertEqual(plateau.piece_a_position(Pos(7, i)).couleur, Couleur.BLANC)


    def test_liste_piece(self):
        plateau = Plateau()
        self.assertEqual(len(plateau.liste_piece()), 0)

        piece = Piece(TypePiece.PION, Couleur.NOIR)
        plateau.ajoute_piece(piece, Pos(1, 1))
        self.assertEqual(len(plateau.liste_piece()), 1)

        plateau = Plateau()
        plateau.init_partie()
        self.assertEqual(len(plateau.liste_piece()), 32)

    def test_piece_a_position(self):
        plateau = Plateau()
        piece = Piece(TypePiece.DAME, Couleur.BLANC)
        pos = Pos(1, 1)
        plateau.ajoute_piece(piece, pos)

        self.assertEqual(plateau.piece_a_position(pos), piece)
        self.assertIsNone(plateau.piece_a_position(Pos(2, 2)))
    
    def test_ajoute_piece_positions_variees(self):
        plateau = Plateau()
        piece = Piece(TypePiece.CAVALIER, Couleur.NOIR)

        # Test sur différentes positions
        positions_test = [Pos(1, 1), Pos(4, 4), Pos(8, 8)]
        for pos in positions_test:
            plateau.ajoute_piece(piece, pos)
            self.assertEqual(plateau.matCases[pos.ligne - 1][pos.colonne - 1].piece, piece)

    def test_bouge_piece_positions_variees(self):
        plateau = Plateau()
        piece = Piece(TypePiece.TOUR, Couleur.BLANC)
        pos_depart = Pos(1, 1)
        plateau.ajoute_piece(piece, pos_depart)

        # Bouger la pièce à différentes positions
        positions_arrivee = [Pos(1, 2), Pos(3, 3), Pos(8, 8)]
        for pos_arrivee in positions_arrivee:
            plateau.bouge_piece(pos_depart, pos_arrivee)
            self.assertIsNone(plateau.matCases[pos_depart.ligne - 1][pos_depart.colonne - 1].piece)
            self.assertEqual(plateau.matCases[pos_arrivee.ligne - 1][pos_arrivee.colonne - 1].piece, piece)
            pos_depart = pos_arrivee  # Mise à jour de la position de départ pour le prochain mouvement

    def test_case_vide_apres_mouvement(self):
        plateau = Plateau()
        piece = Piece(TypePiece.DAME, Couleur.NOIR)
        pos_depart = Pos(4, 4)
        pos_arrivee = Pos(5, 5)
        
        plateau.ajoute_piece(piece, pos_depart)
        plateau.bouge_piece(pos_depart, pos_arrivee)

        # La case de départ doit être vide après le mouvement
        self.assertFalse(plateau.est_case_occupe(pos_depart))
        self.assertTrue(plateau.est_case_occupe(pos_arrivee))

    def test_bouge_piece_sur_piece_existante(self):
        plateau = Plateau()
        piece_depart = Piece(TypePiece.TOUR, Couleur.BLANC)
        piece_arrivee = Piece(TypePiece.PION, Couleur.NOIR)
        pos_depart = Pos(1, 1)
        pos_arrivee = Pos(2, 2)

        plateau.ajoute_piece(piece_depart, pos_depart)
        plateau.ajoute_piece(piece_arrivee, pos_arrivee)
        plateau.bouge_piece(pos_depart, pos_arrivee)

        # Vérifier que la pièce a été déplacée et que la pièce initiale à pos_arrivee a été remplacée
        self.assertIsNone(plateau.matCases[pos_depart.ligne - 1][pos_depart.colonne - 1].piece)
        self.assertEqual(plateau.matCases[pos_arrivee.ligne - 1][pos_arrivee.colonne - 1].piece, piece_depart)

    def test_ajoute_piece_sur_case_occupee(self):
        plateau = Plateau()
        premiere_piece = Piece(TypePiece.TOUR, Couleur.BLANC)
        deuxieme_piece = Piece(TypePiece.DAME, Couleur.NOIR)
        pos = Pos(1, 1)

        plateau.ajoute_piece(premiere_piece, pos)
        plateau.ajoute_piece(deuxieme_piece, pos)

        # Vérifier que la deuxième pièce remplace la première
        self.assertEqual(plateau.matCases[pos.ligne - 1][pos.colonne - 1].piece, deuxieme_piece)

    def test_liste_piece_apres_mouvements(self):
        plateau = Plateau()
        plateau.init_partie()
        pos_depart = Pos(2, 1)
        pos_arrivee = Pos(4, 1)

        plateau.bouge_piece(pos_depart, pos_arrivee)
        self.assertEqual(len(plateau.liste_piece()), 32)
        self.assertTrue(any(p['emplacement'] == 'a4' for p in plateau.liste_piece()))

if __name__ == '__main__':
    if not os.path.exists(os.path.dirname(os.path.realpath(__file__))+'/logs'):
        os.mkdir(os.path.dirname(os.path.realpath(__file__))+'/logs')
    with open(os.path.dirname(os.path.realpath(__file__))+'/logs/tests_results_Plateau.txt', 'w') as f:
        loader = unittest.TestLoader()
        suite = loader.loadTestsFromModule(sys.modules[__name__])
        unittest.TextTestRunner(f, verbosity=2).run(suite)


