import unittest
import os
import sys
import tempfile

from Pos import*

class TestPos(unittest.TestCase):

    def test_initialisation_avec_numeriques(self):
        # Test avec des coordonnées numériques normales
        pos = Pos(3, 4)
        self.assertEqual((pos.ligne, pos.colonne), (3, 4))

        # Test avec la valeur limite (1, 1)
        pos = Pos(1, 1)
        self.assertEqual((pos.ligne, pos.colonne), (1, 1))

        # Test avec la valeur limite (8, 8)
        pos = Pos(8, 8)
        self.assertEqual((pos.ligne, pos.colonne), (8, 8))

        pos = Pos(4, 5)
        self.assertEqual((pos.ligne, pos.colonne), (4, 5))

    def test_initialisation_avec_chaine(self):
        # Test avec une chaîne de caractères valide
        pos = Pos("e4")
        self.assertEqual((pos.ligne, pos.colonne), (4, 5))

        # Test avec la chaîne en bas à gauche ("a1")
        pos = Pos("a1")
        self.assertEqual((pos.ligne, pos.colonne), (1, 1))

        # Test avec la chaîne en haut à droite ("h8")
        pos = Pos("h8")
        self.assertEqual((pos.ligne, pos.colonne), (8, 8))


    def test_get_emplacement(self):
        pos = Pos(4, 5)
        self.assertEqual(pos.get_emplacement, "e4")

    def test_addition(self):
        pos1 = Pos(3, 4)
        pos2 = Pos(2, 1)
        resultat = pos1 + pos2
        self.assertEqual(resultat, Pos(5, 5))

    def test_indice(self):
        pos = Pos(0,0)
        self.assertEqual(pos.ind(), 1)
        pos = Pos(7,7)
        self.assertEqual(pos.ind(), 64)

    def test_est_hors_plateau(self):
        self.assertTrue(Pos.est_hors_plateau(Pos(9, 9))[0])
        self.assertTrue(Pos.est_hors_plateau(Pos(0, 0))[0])
        self.assertFalse(Pos.est_hors_plateau(Pos(1, 1))[0])

    def test_est_dans_liste_positions(self):
        liste_positions = [Pos(2, 3), Pos(5, 6)]
        self.assertTrue(Pos.est_dans_liste_pos(Pos(2, 3), liste_positions))
        self.assertFalse(Pos.est_dans_liste_pos(Pos(1, 1), liste_positions))

    def test_representation_chaine(self):
        pos = Pos(3, 4)
        self.assertEqual(str(pos), "Ligne: 3, Colonne: 4, Emplacement: d3")

    def test_egalite(self):
        pos1 = Pos(4, 5)
        pos2 = Pos(4, 5)
        pos3 = Pos(5, 4)
        self.assertTrue(pos1 == pos2)
        self.assertFalse(pos1 == pos3)

if __name__ == '__main__':
    if not os.path.exists(os.path.dirname(os.path.realpath(__file__))+'/logs'):
        os.mkdir(os.path.dirname(os.path.realpath(__file__))+'/logs')
    with open(os.path.dirname(os.path.realpath(__file__))+'/logs/tests_results_Pos.txt', 'w') as f:
        loader = unittest.TestLoader()
        suite = loader.loadTestsFromModule(sys.modules[__name__])
        unittest.TextTestRunner(f, verbosity=2).run(suite)
