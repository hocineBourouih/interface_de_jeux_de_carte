from souris import *
from bouton import *
from event import *

from menu import *  # États du jeu
from plateau import *
from regle import *
from parametre import *
from selecteur import *


import pygame

pygame.init()


class Interface:  # À compléter plus tard
    def __init__(self, largeur=800, hauteur=450):
        self.window = pygame.display.set_mode(
            (largeur, hauteur),  # Rajouter pygame.FULLSCREEN pour mettre en plein ecran
            pygame.FULLSCREEN)
        
        self.frame = Menu(largeur, hauteur)
        self.frame_buffer = []
        self.largeur = largeur
        self.hauteur = hauteur
        pygame.display.set_caption("Card Game")
        self.blockUselessEvents()

        self.clock = pygame.time.Clock()
    def loop(self):

        self.alive = True
        while self.alive:
            self.clock.tick()
            for event in pygame.event.get():

                if event.type == SWAP_MENU:  # Gestion du swap des états
                    self.frame = Menu(self.largeur, self.hauteur)
                    for i in range(len(self.frame_buffer)):
                        self.frame_buffer.pop(0)
                if event.type == SWAP_PLATEAU:
                    self.frame = Plateau(self.largeur, self.hauteur)
                    for i in range(len(self.frame_buffer)):
                        self.frame_buffer.pop(0)
                if event.type == SWAP_REGLE:
                    self.frame = Regle(self.largeur, self.hauteur)
                
                # Parametre
                if event.type == PARAMETRE_SWAP_ON:
                    self.frame_buffer.insert(0, self.frame)
                    self.frame = Parametre(self.largeur, self.hauteur)
                if event.type == PARAMETRE_SWAP_OFF:
                    self.frame = self.frame_buffer[0]
                    self.frame_buffer.pop(0)

                # Selecteur
                if event.type == SELECTEUR_SWAP_ON:
                    self.frame_buffer.insert(0, self.frame)
                    self.frame = Selecteur(self.largeur, self.hauteur, self)
                if event.type == SELECTEUR_SWAP_OFF:
                    self.frame = self.frame_buffer[0]
                    self.frame_buffer.pop(0)

                # Quitter
                if event.type == EXIT_INTERFACE or (event.type == pygame.KEYDOWN and event.key == K_ESCAPE):
                    self.alive = False

                self.frame.react(event)  # Gestion des évènements de l'état actuel

            for frame in self.frame_buffer:
                frame.draw(self.window)
            self.frame.draw(self.window)

            pygame.display.flip()
            print(self.clock.get_fps())

    def blockUselessEvents(self):
        pygame.event.set_blocked(pygame.JOYAXISMOTION)
        pygame.event.set_blocked(pygame.JOYBALLMOTION)
        pygame.event.set_blocked(pygame.JOYHATMOTION)
        pygame.event.set_blocked(pygame.JOYBUTTONDOWN)
        pygame.event.set_blocked(pygame.AUDIODEVICEADDED)
        pygame.event.set_blocked(pygame.AUDIODEVICEREMOVED)
        pygame.event.set_blocked(pygame.FINGERMOTION)
        pygame.event.set_blocked(pygame.FINGERDOWN)
        pygame.event.set_blocked(pygame.FINGERUP)
        pygame.event.set_blocked(pygame.MULTIGESTURE)
        pygame.event.set_blocked(pygame.TEXTEDITING)
        pygame.event.set_blocked(pygame.DROPBEGIN)
        pygame.event.set_blocked(pygame.DROPCOMPLETE)
        pygame.event.set_blocked(pygame.DROPFILE)
        pygame.event.set_blocked(pygame.DROPTEXT)
        pygame.event.set_blocked(pygame.MIDIIN)
        pygame.event.set_blocked(pygame.MIDIOUT)
        pygame.event.set_blocked(pygame.CONTROLLERDEVICEADDED)
        pygame.event.set_blocked(pygame.CONTROLLERDEVICEREMAPPED)
        pygame.event.set_blocked(pygame.CONTROLLERDEVICEREMOVED)
        pygame.event.set_blocked(pygame.JOYDEVICEADDED)
        pygame.event.set_blocked(pygame.JOYDEVICEREMOVED)

        pygame.event.set_blocked(pygame.WINDOWHITTEST)
