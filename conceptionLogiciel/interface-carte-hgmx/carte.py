import pygame

class Carte(pygame.sprite.Sprite):
    def __init__(self, enseigne, valeur):
        
        pygame.sprite.Sprite.__init__(self)
        
        self.enseigne = enseigne        # la couleur de la carte
        self.valeur = valeur            # la valeur de la carte (as = 1, valet = 11, dame=  12, roi = 13, et joker = 0)
        self.retournee = False           # Vrai si la carte est face caché

        self.updateSprite()

        self.rect = self.image.get_rect()
       #self.image est crée dans updateSprite()


    def updateSprite(self):                     # permet d'update le sprite
        if self.retournee:
            self.image = pygame.image.load("images/cartes 2 (avec Jokers)/dos-bleu.png")
        else :
            self.image = pygame.image.load(self.calcAddrFace())
    
    def calcAddrFace(self):             # permet de calculer le nom de l'image a utiliser dans le fichier à l'aide de l'enseigne et de la valeur
        addrFace = "images/cartes 2 (avec Jokers)/"
        if self.valeur == 0:
            addrFace += "black_joker.png"
        else:
            if self.valeur == 1:
                addrFace += "ace"
            
            elif self.valeur <= 10:
                addrFace += str(self.valeur)
            
            elif self.valeur == 11:
                addrFace += "jack"
            
            elif self.valeur == 12:
                addrFace += "queen"
            
            elif self.valeur == 13:
                addrFace += "king"
            
            else:
                addrFace += str(self.valeur)

            addrFace += "_of_"
            if self.enseigne == "pique":
                addrFace += "spades"
            elif self.enseigne == "coeur":
                addrFace += "hearts"
            
            elif self.enseigne == "treifle":
                addrFace += "clubs"
            
            elif self.enseigne == "carreau":
                addrFace += "diamonds"
            
            addrFace += ".png"
        return addrFace



    def estFigure(self):                # retourne vrai si la carte est un valet, une dame, ou un roi
        return self.valeur > 10
    
    def retourner(self):                # permet de retourner la carte (swap de True à False ou de False à True)
        self.retournee = not self.retournee
        self.updateSprite()
        
    
    def teleporter(self, x, y):
        self.rect.centerx = x
        self.rect.centery = y
    
    def deplacer(self, x, y):
        self.rect.centerx += x
        self.rect.centery += y
    