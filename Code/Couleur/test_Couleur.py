import unittest
import os
import sys
import tempfile

from Couleur import*  

class TestCouleur(unittest.TestCase):

    def test_inversion_couleur(self):
        self.assertEqual(~Couleur.BLANC, Couleur.NOIR)
        self.assertEqual(~Couleur.NOIR, Couleur.BLANC)

    def test_vers_chaine(self):
        self.assertEqual(Couleur.vers_chaine(Couleur.BLANC), 'Blanc')
        self.assertEqual(Couleur.vers_chaine(Couleur.NOIR), 'Noir')


if __name__ == '__main__':
    if not os.path.exists(os.path.dirname(os.path.realpath(__file__))+'/logs'):
        os.mkdir(os.path.dirname(os.path.realpath(__file__))+'/logs')
    with open(os.path.dirname(os.path.realpath(__file__))+'/logs/tests_results_Couleur.txt', 'w') as f:
        loader = unittest.TestLoader()
        suite = loader.loadTestsFromModule(sys.modules[__name__])
        unittest.TextTestRunner(f, verbosity=2).run(suite)