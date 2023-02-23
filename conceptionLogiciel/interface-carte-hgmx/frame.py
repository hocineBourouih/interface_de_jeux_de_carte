import pygame
from event import *
from souris import *
from bouton import *
from groupeBouton import *


class Frame:
    def __init__(self, largeur, hauteur):
        self.souris = Souris()

        self.fond_ecran = None

        self.hauteur = hauteur
        self.largeur = largeur

        self.test_musique = False

        self.boutons = GroupeBouton([], largeur, hauteur)

        self.keyDict = {pygame.K_LCTRL : False}


    def react(self, event):
        
        if event.type == pygame.KEYDOWN:
            self.keyDict[event.key] = True
        if event.type == pygame.KEYUP:
            self.keyDict[event.key] = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Lorsque clic gauche enfoncé
            self.souris.click_G()

        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:  #  Lorsque clic gauche désenfoncé
            self.souris.reinitialiser()  # Reset le sprite de la souris

    def draw(self, window):

        window.blit(self.fond_ecran, (0, 0))
        self.boutons.draw(window)