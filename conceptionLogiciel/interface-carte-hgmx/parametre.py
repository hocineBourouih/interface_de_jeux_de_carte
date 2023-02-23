import pygame
from bouton import *
from frame import *


class Parametre(Frame):
    def __init__(self, largeur, hauteur):
        super().__init__(largeur, hauteur)

        self.trigger = False

        self.index = 0

        self.fond_ecran = pygame.image.load("images/imfond.jpeg")
        self.fond_ecran = pygame.transform.scale(self.fond_ecran, (largeur/2, hauteur/2))
        self.fond_ecran = self.fond_ecran.convert_alpha()
        bg = pygame.surface.Surface((largeur, hauteur))
        bg = bg.convert_alpha()
        bg.fill((0,0,0, 100))
        bg.blit(self.fond_ecran, ((self.largeur - self.largeur/2)/2, (self.hauteur - self.hauteur/2)/2))
        self.fond_ecran = bg


        self.retour = pygame.image.load("images/v.png")
        self.retour = pygame.transform.scale(self.retour,(90, 90))
        self.retour = Bouton(0, 0,self.retour)
        self.retour.rect.center = (largeur/2, hauteur/2)

        self.reprendre = pygame.image.load("images/repp.gif")
        self.reprendre = pygame.transform.scale(self.reprendre,(110, 110))
        self.reprendre = Bouton(0,0,self.reprendre)
        self.reprendre.rect.center = (2*largeur/5, hauteur/2)

        self.men = pygame.image.load("images/book.gif")
        self.men = pygame.transform.scale(self.men,(100, 100))
        self.men = Bouton(0,0,self.men)
        self.men.rect.center = (3*largeur/5, hauteur/2)



    def react(self,event):
        super().react(event)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.men.rect.collidepoint((self.souris.rect.x, self.souris.rect.y)):
            pygame.event.post(pygame.event.Event(SWAP_MENU))
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.reprendre.rect.collidepoint((self.souris.rect.x, self.souris.rect.y)):
            pygame.event.post(pygame.event.Event(PARAMETRE_SWAP_OFF))
        self.boutons.react(event)

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.retour.rect.collidepoint((self.souris.rect.x, self.souris.rect.y)):
            pygame.event.post(pygame.event.Event(SWAP_PLATEAU))



    def draw(self, window):
        super().draw(window)
        self.men.update(window)

        self.retour.update(window)
        self.reprendre.update(window)

        self.souris.update(window)
