import os
import pygame
import sys

class Interface:
      # Variables de classes pour l'échéquier.
      WINDOW_WIDTH = 720
      WINDOW_HEIGHT = 720
      blockSize = 90

      def __init__(self):        
        
        # Init PyGame 
        pygame.init()
        pygame.display.set_caption("Jeu d'Echec")
       
        # Cree le GUI pour le jeu 
        self.SCREEN = pygame.display.set_mode((self.WINDOW_WIDTH + 220, self.WINDOW_HEIGHT + 20))
        self.font = pygame.font.SysFont('Arial', 25)
        self.SCREEN.fill(color=(160,82,45)) 
        self.default_board()  

        # Variables utilisées pour représenter les pièces perdues par chaque joueur sur
        # le côté du plateau. Cela permet juste de décaler les Sprites.
        self.pieces_perdues_blanches = 0
        self.pieces_perdues_noires = 0      
        
        # Chargement des images des pièces 
        self.load_assets()

      def default_board(self):
        """
        Initialise un échéquier vide, simplement avec le damier, les lettres/chiffres des lignes/colonnes ainsi
        que le côté droit de l'échéquier qui va servir à représenter les pièces perdues.
        """

        self.SCREEN.fill(color=(160,82,45), rect=(0, 0, self.WINDOW_WIDTH + 20, self.WINDOW_HEIGHT + 20)) 
        for i, x in enumerate(range(20, self.WINDOW_WIDTH, self.blockSize)):
            for j, y in enumerate(range(0, self.WINDOW_HEIGHT-20, self.blockSize)):
                rect = pygame.Rect(x, y, self.blockSize, self.blockSize)
                if (i + j) % 2 == 0:
                    fill_color = (139,69,19)
                else:
                    fill_color = (255,228,180)
                self.SCREEN.fill(color=fill_color, rect=rect)
                pygame.draw.rect(self.SCREEN, (0, 0, 0), rect, 1)

                if i == 0:
                    self.SCREEN.blit(self.font.render(str(j+1), True, (0,0,0)), (x-17, y+self.blockSize//2-10))
                if j == 7:
                    self.SCREEN.blit(self.font.render('ABCDEFGH'[i], True, (0,0,0)), (x - 8 +self.blockSize//2, y+self.blockSize - 5))

      def load_assets(self):
        """
        Chargement des images des pièces en mémoires. On met le tout dans un dictionnaire qu'on appelle qu'en on veut 
        montrer l'image.
        """
        curr_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')
        bishopB = pygame.transform.scale(pygame.image.load(os.path.join(curr_path, 'assets', 'bd.png')).convert_alpha(), (self.blockSize, self.blockSize))
        bishopW = pygame.transform.scale(pygame.image.load(os.path.join(curr_path, 'assets', 'bl.png')).convert_alpha(), (self.blockSize, self.blockSize))
        pawnB = pygame.transform.scale(pygame.image.load(os.path.join(curr_path, 'assets', 'pd.png')).convert_alpha(), (self.blockSize, self.blockSize))
        pawnW = pygame.transform.scale(pygame.image.load(os.path.join(curr_path, 'assets', 'pl.png')).convert_alpha(), (self.blockSize, self.blockSize))
        knightB = pygame.transform.scale(pygame.image.load(os.path.join(curr_path, 'assets', 'nd.png')).convert_alpha(), (self.blockSize, self.blockSize))
        knightW = pygame.transform.scale(pygame.image.load(os.path.join(curr_path, 'assets', 'nl.png')).convert_alpha(), (self.blockSize, self.blockSize))
        rookB = pygame.transform.scale(pygame.image.load(os.path.join(curr_path, 'assets', 'rd.png')).convert_alpha(), (self.blockSize, self.blockSize))
        rookW = pygame.transform.scale(pygame.image.load(os.path.join(curr_path, 'assets', 'rl.png')).convert_alpha(), (self.blockSize, self.blockSize))
        queenB = pygame.transform.scale(pygame.image.load(os.path.join(curr_path, 'assets', 'qd.png')).convert_alpha(), (self.blockSize, self.blockSize))
        queenW = pygame.transform.scale(pygame.image.load(os.path.join(curr_path, 'assets', 'ql.png')).convert_alpha(), (self.blockSize, self.blockSize))
        kingB = pygame.transform.scale(pygame.image.load(os.path.join(curr_path, 'assets', 'kd.png')).convert_alpha(), (self.blockSize, self.blockSize))
        kingW = pygame.transform.scale(pygame.image.load(os.path.join(curr_path, 'assets', 'kl.png')).convert_alpha(), (self.blockSize, self.blockSize))

        self.pieces_png = {'BLANC': {'ROI': kingW, 'DAME': queenW, 'CAVALIER': knightW, 'FOU': bishopW, 'TOUR': rookW, 'PION': pawnW},
                        'NOIR': {'ROI': kingB, 'DAME': queenB, 'CAVALIER': knightB, 'FOU': bishopB, 'TOUR': rookB, 'PION': pawnB}}

      def affiche_liste_piece(self, liste_piece = None):
        """
        Fonction pour afficher les pièces sur le plateau aux emplacements corrects. Prend en paramètre une liste de
        pièce comme retourné par la fonction "liste_piece" de la classe Plateau. Par défaut, on utilise l'attribute
        "liste_piece_to_render"
        """

        if not liste_piece:
           liste_piece = self.liste_piece_to_render

        for piece in liste_piece:
            self.SCREEN.blit(self.pieces_png[piece['couleur'].name][piece['nom'].name], \
             ((ord(piece['emplacement'][0]) - 96) * self.blockSize - 70, int(piece['emplacement'][1]) * self.blockSize - self.blockSize))
        # HACK: to rerender the piece after displaying the cursor since I don't want to have to play with sprite layers!
        self.liste_piece_to_render = liste_piece
        pygame.display.update()       
        

      def saisir_emplacement(self):
        """
        Fonction pour saisir l'emplacement que le joueur choisi. On récupère la position de la souris lorsque
        le joueur clique et on converti les coordonnées en case (par exemple 'a8') qui est retourné dans le programme.
        Bien sûr, on vérifie que le joueur clique dans le damier et non en dehors pour que la position soit valide.
        """
        isCaseSelected = False

        while not(isCaseSelected):
            
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    posMouse = pygame.mouse.get_pos()
                    # Not over the board
                    if 20 < posMouse[0] < self.WINDOW_WIDTH and posMouse[1] < self.WINDOW_HEIGHT - 20:
                        col = posMouse[0] // self.blockSize
                        line = posMouse[1] // self.blockSize + 1
                        isCaseSelected = True
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

        return 'abcdefgh'[col] + '' + str(line)

      def place_curseur(self, emplacement):
        """
        La fonction prend un emplacement (exemple 'a8') et affiche la case en vert. La fonction doit être appelée pour chaque
        emplacement que l'on veut illuminer en vert. Cela permet de montrer les mouvements possibles de la pièce en question
        """
        rect = pygame.Rect((ord(emplacement[0]) - 96) * self.blockSize - 70, int(emplacement[1]) * self.blockSize - self.blockSize, self.blockSize, self.blockSize)
        self.SCREEN.fill(color=(152,251,152), rect=rect)
        pygame.draw.rect(self.SCREEN, (0, 0, 0), rect, 1)
        self.affiche_liste_piece(self.liste_piece_to_render)

      def place_curseur_roi(self, emplacement, checkmate=False):
        """
        Cette fonction est appelée quand le roi est en échec ou en échec et mat. Si en échec, on l'affiche en jaune pour prévenir
        le joueur qu'il doit réagir. Si en échec et mat, on l'affiche en rouge et un texte "Checkmate !" est affiché sur le côté.
        """
        rect = pygame.Rect((ord(emplacement[0]) - 96) * self.blockSize - 70, int(emplacement[1]) * self.blockSize - self.blockSize, self.blockSize, self.blockSize)
        self.SCREEN.fill(color=(255,114,118) if checkmate else (255,239,0), rect=rect)
        pygame.draw.rect(self.SCREEN, (0, 0, 0), rect, 1)
        if checkmate:
            self.SCREEN.blit(self.font.render('Checkmate !', True, (0,0,0)), (750, 400))
        self.affiche_liste_piece()

      def enleve_curseur(self):
        """
        Fonction qui enlève les cases mises en surbrillance si le joueur change de pièce ou déplace pièce. Cela équivaut à nettoyer l'échéquier
        de tout marqueur pour n'avoir que les pièces.
        """
        
        self.default_board()
        pygame.display.update()

      def piece_mangee(self, emplacement):
        """
        Cette fonction ajoute une pièce qui vient d'être perdue sur le côté de l'échéquier. Elle prend en paramètre l'emplacement de la pièce 
        qui vient d'être perdue (ex: 'a8') et instancie le sprite équivalent sur le côté de l'échéquier mais en plus petit. 
        
        Remarque: il faut que la fonction soit appelée AVANT que le plateau soit modifié vu que l'on prend l'emplacement de la pièce
        qui vient d'être perdue avant qu'elle soit retirée.
        """

        for piece in self.liste_piece_to_render:
            if emplacement == piece['emplacement']:
                img_res = pygame.transform.scale(self.pieces_png[piece['couleur'].name][piece['nom'].name], (35, 35))
                if piece['couleur'].name == 'NOIR':
                   self.SCREEN.blit(img_res, (740 + 30 * (self.pieces_perdues_noires % 6), 540 + (self.pieces_perdues_noires // 6) * 50))
                   self.pieces_perdues_noires += 1
                else:
                   self.SCREEN.blit(img_res, (740 + 30 * (self.pieces_perdues_blanches % 6), 150 - (self.pieces_perdues_blanches // 6) * 50))
                   self.pieces_perdues_blanches += 1



