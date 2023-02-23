import pygame
from event import *
import musique

def rien(self):
    return

def quitter(self):
    pygame.event.post(pygame.event.Event(EXIT_INTERFACE))

def jouer(self):
    pygame.event.post(pygame.event.Event(SWAP_PLATEAU))

def regle(self):
    pygame.event.post(pygame.event.Event(SWAP_REGLE))

def music_on(self):
    self.image = pygame.image.load("images/musiqueOn.png")
    pygame.mixer.music.unpause()

def music_off(self):
    self.image = pygame.image.load("images/stopMusique.png")
    self.image = pygame.transform.scale(self.image, (60,60))
    pygame.mixer.music.pause()

def change_musique(self):
    musique.next_music()

def parametre_on(self):
    pygame.event.post(pygame.event.Event(PARAMETRE_SWAP_ON))


class Bouton(pygame.sprite.Sprite):
    def __init__(self, x, y, image, callback = rien):                                #Mon bouton à besoin d'une image et de deux pos .
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()                             #Creation de la hitbox
        self.rect.x = x
        self.rect.y = y


        self.action = callback

    def update(self,interface):
        interface.blit(self.image, self.rect)                         #Colle l'image au position de la hitbox

    def react(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.rect.collidepoint(event.pos):
            self.action(self)

class BoutonSwap(Bouton):
    def __init__(self, x, y, image, callback1, callback2):
        super().__init__(x, y, image, callback1)
        self.action2 = callback2
        self.activated = True
    
    def react(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.rect.collidepoint(event.pos):
            if self.activated:
                self.action(self)
            else:
                self.action2(self)

            self.activated = not self.activated
        