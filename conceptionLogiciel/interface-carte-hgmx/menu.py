from event import *

from plateau import *
from groupeBouton import * 

import pygame


class Menu(Frame):
    def __init__(self, largeur, hauteur):
        super().__init__(largeur, hauteur)

        self.largeur = largeur
        self.hauteur = hauteur

        self.fond_ecran = pygame.image.load("images/Cartes_fond_ecran.jfif")
        self.fond_ecran = pygame.transform.scale(self.fond_ecran, (largeur, hauteur))

        self.souris = Souris()

        self.boutons.add_bouton(["quitter", "jouer", "regle", "music"])

    def react(self, event):
        super().react(event)
        self.boutons.react(event)

    def draw(self, window):

        super().draw(window)

        self.souris.update(window)  # Affiche la Souris depuis souris.py