from frame import *
from pygame import *
from paquet import *
from bouton import *


# SCALE EN FONCTION DE L'ÉCRAN
class Selecteur(Frame):
    def __init__(self, largeur, hauteur, interface):
        super().__init__(largeur, hauteur)

        self.interface = interface
        self.main = []

        self.i = 0
        self.opening = True
        self.closing = False

        self.fond_ecran = pygame.surface.Surface((largeur, 200))
        self.fond_ecran = self.fond_ecran.convert_alpha()
        self.fond_ecran.fill((0,0,0, 100))


        self.paquet = pygame.image.load("images/paquet_icon.png")
        self.paquet = pygame.transform.scale(self.paquet, (100, 100))
        self.paquet = Bouton(40, 50 + self.hauteur - self.i, self.paquet)
        self.boutons.add_bouton(self.paquet)

    
    def react(self, event):
        super().react(event)
        print(self.keyDict)

        if event.type == pygame.KEYDOWN and event.key == K_TAB:
            self.closing = True
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(self.paquet.rect.collidepoint(event.pos), event.pos, self.paquet)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.paquet.rect.collidepoint(event.pos):
                print("test!!!")
                self.interface.frame_buffer[0].carte_en_main = Paquet(x = event.pos[0], y = event.pos[1])
                pygame.event.post(pygame.event.Event(SELECTEUR_SWAP_OFF))
            else:
                self.interface.frame_buffer[0].keyDict = self.keyDict
                self.interface.frame_buffer[0].react(event)
        
        if event.type == pygame.MOUSEBUTTONUP:
            if self.inWindow(event.pos):
                self.interface.frame_buffer[0].carte_en_main = Paquet(True)
            else:
                print("fonctionne")
                self.interface.frame_buffer[0].keyDict = self.keyDict
                self.interface.frame_buffer[0].react(event)

    
    def draw(self, window):
        self.animate()

        window.blit(self.fond_ecran, (0, self.hauteur - self.i))
        self.boutons.draw(window)

        self.souris.update(window)

    
    def animate(self):
        if self.opening:
            self.i += 20
            self.paquet.rect.y -=20
        elif self.closing:
            self.i -= 20
            self.paquet.rect.y +=20

        if self.i > 190:
            self.opening = False
        elif self.i < 1:
            self.closing = False
            pygame.event.post(pygame.event.Event(SELECTEUR_SWAP_OFF))

    def inWindow(self, point):
        return point[1] > self.hauteur-200