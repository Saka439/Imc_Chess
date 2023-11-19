import unittest
import os
import sys
import tempfile

from CasePlateau import*  

class TestCasePlateau(unittest.TestCase):

    def test_initialisation_case_vide(self):
        case = CasePlateau()
        self.assertIsNone(case.piece)

    def test_initialisation_case_avec_piece(self):
        piece = Piece(TypePiece.FOU, Couleur.BLANC)
        case = CasePlateau(piece)
        self.assertEqual(case.piece, piece)

    def test_case_est_occupe(self):
        case_vide = CasePlateau()
        self.assertFalse(case_vide.est_occupe())

        piece = Piece(TypePiece.CAVALIER, Couleur.NOIR)
        case_occupee = CasePlateau(piece)
        self.assertTrue(case_occupee.est_occupe())

if __name__ == '__main__':
    if not os.path.exists(os.path.dirname(os.path.realpath(__file__))+'/logs'):
        os.mkdir(os.path.dirname(os.path.realpath(__file__))+'/logs')
    with open(os.path.dirname(os.path.realpath(__file__))+'/logs/tests_results_CasePlateau.txt', 'w') as f:
        loader = unittest.TestLoader()
        suite = loader.loadTestsFromModule(sys.modules[__name__])
        unittest.TextTestRunner(f, verbosity=2).run(suite)

