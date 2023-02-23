import pygame
pygame.init()

class Souris(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.reinitialiser()
        self.rect = self.curseur.get_rect()                                     #Creation de la hitbox


    def update(self,interface):
        pygame.mouse.set_visible(False)
        self.rect.x, self.rect.y = pygame.mouse.get_pos()                        #Rect afin d'avoir les coordonnées du sprite afin quel soit les memes que mon curseur
        if self.enfoncer == True :
            interface.blit(self.curseur, self.rect)                                 #Permet de coller le sprit de la souris sur l'interface a chaque tick
        else:
            interface.blit(self.curseur,(self.rect.x - 12,self.rect.y - 12))     #Le - 12 sert à repositionner le nv curseur




    def click_G(self):
        self.curseur = pygame.image.load("images/Cotton_gloves_update.png")
        self.curseur = pygame.transform.scale(self.curseur, (27, 27))
        self.curseur = pygame.transform.rotate(self.curseur, -90)
        self.enfoncer = True

    def click_M(self):
        self.curseur = pygame.image.load("images/Cotton_gloves_question_mark.png")
        self.curseur = pygame.transform.scale(self.curseur,(50, 50))
        self.curseur = pygame.transform.rotate(self.curseur, -90)
        self.demander = True

    def click_D(self):
        self.curseur = pygame.image.load("images/Cotton_gloves_retourner.png")
        self.curseur = pygame.transform.scale(self.curseur,(27,27))
        self.curseur = pygame.transform.rotate(self.curseur, -90)
        self.tourner = True




    def reinitialiser(self):
        self.curseur = pygame.image.load("images/Cotton_gloves.png")
        self.curseur = pygame.transform.scale(self.curseur, (50, 50))
        self.curseur = pygame.transform.rotate(self.curseur, -90)
        self.enfoncer = False                                            #Permet de reinitialiser le curseur
        self.demander = False
        self.tourner = False
























