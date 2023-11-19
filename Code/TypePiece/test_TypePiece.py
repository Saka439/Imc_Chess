import unittest
import os
import sys
import tempfile

from TypePiece import*   

class TestTypePiece(unittest.TestCase):

    def test_vers_chaine_roi(self):
        self.assertEqual(TypePiece.ROI.vers_chaine(), 'Roi')

    def test_vers_chaine_dame(self):
        self.assertEqual(TypePiece.DAME.vers_chaine(), 'Dame')

    def test_vers_chaine_tour(self):
        self.assertEqual(TypePiece.TOUR.vers_chaine(), 'Tour')

    def test_vers_chaine_fou(self):
        self.assertEqual(TypePiece.FOU.vers_chaine(), 'Fou')

    def test_vers_chaine_cavalier(self):
        self.assertEqual(TypePiece.CAVALIER.vers_chaine(), 'Cavalier')

    def test_vers_chaine_pion(self):
        self.assertEqual(TypePiece.PION.vers_chaine(), 'Pion')

if __name__ == '__main__':
    if not os.path.exists(os.path.dirname(os.path.realpath(__file__))+'/logs'):
        os.mkdir(os.path.dirname(os.path.realpath(__file__))+'/logs')
    with open(os.path.dirname(os.path.realpath(__file__))+'/logs/tests_results_TypePiece.txt', 'w') as f:
        loader = unittest.TestLoader()
        suite = loader.loadTestsFromModule(sys.modules[__name__])
        unittest.TextTestRunner(f, verbosity=2).run(suite)