#(bienvenue dans le marché de l'octet en concurrence avec plateau.py)

import pygame.font
from plateau import *
from random import choice  #permet de faire une dinguerie en animation (je vous jure)



class Regle(Frame):
    def __init__(self, largeur, hauteur):
        super().__init__(largeur, hauteur)
        self.time = 0
        self.trigger = False
        self.index = 0
        self.click = False
        self.nvPaquet = []
        self.vide = False
        self.joker = False
        self.posx = largeur
        self.posy = hauteur


        self.fond_ecran = pygame.image.load("images/plateau.jpeg")
        self.fond_ecran = pygame.transform.scale(self.fond_ecran, (largeur, hauteur))

        self.imgRegle = pygame.image.load("images/Regle_du_jeux.jpg")
        self.imgRegle = pygame.transform.scale(self.imgRegle, (largeur/2, hauteur/2))
        self.imgRegle = Bouton(largeur/4,hauteur/4,self.imgRegle)

        self.back = pygame.image.load("images/go_back.png")
        self.back = pygame.transform.scale(self.back,(60, 60))
        self.back = Bouton(0,0,self.back)

        self.box = pygame.image.load("images/text_box.png")
        self.box = pygame.transform.scale(self.box,(largeur/1.8, hauteur/8))
        self.box = Dialogue(largeur/4.5,hauteur/1.3,self.box,self.index)

        self.sourisTutoInv = pygame.image.load("images/Cotton_gloves_update.png")
        self.sourisTutoInv = pygame.transform.scale(self.sourisTutoInv, (70, 70))
        self.sourisTutoInv = pygame.transform.rotate(self.sourisTutoInv, -90)


        self.sourisTuto = pygame.image.load("images/Cotton_gloves.png")
        self.sourisTuto = pygame.transform.scale(self.sourisTuto, (100, 100))
        self.sourisTuto = pygame.transform.rotate(self.sourisTuto, -90)

        self.sourisTuto1 = Animation(largeur/1.2, hauteur/2, self.sourisTuto,self.ligne1(largeur/1.2,hauteur/2,largeur/12,hauteur/2,50),49) #Doit contenir : position de depart , image , la fonction ligne 1 avec tout ses parametres (et index pas obligatoire)
        self.sourisTuTo1 = Animation(largeur/1.2,hauteur/2, self.sourisTuto,self.ligne1(largeur/1.2,hauteur/2,largeur/12,hauteur/2,50),1)   #deux variables differentes t et T .

        self.sourisTuTo2 = Animation(largeur/12,hauteur/2,self.sourisTuto,self.ligne1(largeur/12,hauteur/2,largeur/3,hauteur/2,50))

        self.carte = pygame.image.load("images/cartes 2 (avec Jokers)/red_joker.png")
        self.carteAs = pygame.image.load("images/cartes 2 (avec Jokers)/ace_of_spades2.png")
        self.carteHearth = pygame.image.load("images/cartes 2 (avec Jokers)/4_of_hearts.png")
        self.carteRetourner = pygame.image.load("images/cartes 2 (avec Jokers)/dos-bleu.png")
        #index 4

        self.carte1_1 = Animation(largeur/3,hauteur/2,self.carte,self.ligne1(largeur/3,hauteur/2,largeur/1.2,hauteur/3,50))
        self.carte1_2 = Animation(largeur/3,hauteur/2,self.carte,self.ligne1(largeur/3,hauteur/2,largeur/1.2,hauteur/1.5,50))
        self.carte1 = choice([self.carte1_1,self.carte1_2])

        self.sourisTuTo3_1 = Animation(largeur / 3, hauteur / 2, self.sourisTutoInv,self.ligne1(largeur / 3, hauteur / 2, largeur / 1.2, hauteur / 3, 50))
        self.sourisTuTo3_2 = Animation(largeur / 3, hauteur / 2, self.sourisTutoInv,self.ligne1(largeur / 3, hauteur / 2, largeur / 1.2, hauteur / 1.5, 50))
        self.sourisTuTo3 = choice([self.sourisTuTo3_1,self.sourisTuTo3_2])

        #index 5
        #doit contenir un curseur avec 3-4 animations et 3 cartes qui vont partager les memes co
        self.carte2 = Animation(largeur/1.2,hauteur/2,self.carte,self.ligne1(largeur/1.2,hauteur/2,largeur/2,hauteur/2,50))
        self.carteAs1 = Animation(largeur/2,hauteur/2,self.carteAs,self.ligne1(largeur/2,hauteur/2,largeur/2,hauteur/2,1))  #ne va pas bouger
        self.carteHearth1 = Animation(largeur/6,hauteur/2,self.carteHearth,self.ligne1(largeur/6,hauteur/2,largeur/3,hauteur/3,50))

        self.sourisIndex5_1 = Animation(largeur/1.2,hauteur/2,self.sourisTutoInv,self.ligne1(largeur/1.2,hauteur/2,largeur/2,hauteur/2,50))
        self.sourisIndex5_2 = Animation(largeur/2,hauteur/2,self.sourisTuto,self.ligne1(largeur/2,hauteur/2,largeur/6,hauteur/2,50))
        self.sourisIndex5_3 = Animation(largeur/6,hauteur/2,self.sourisTutoInv,self.ligne1(largeur/6,hauteur/2,largeur/2,hauteur/2,50))
        self.sourisIndex5_4 = Animation(largeur/2,hauteur/2,self.sourisTuto,self.ligne1(largeur/2,hauteur/2,largeur/2,hauteur/2,1))

        #index 6
        #doit contenir 2 sprites de cartes et 3-4 mouvement de souris
        self.carteHearth2 = Animation(largeur/4,hauteur/2,self.carteHearth,self.ligne1(largeur/4,hauteur/2,largeur/2,hauteur/2,50))
        self.carte3 = Animation(largeur/2,hauteur/2,self.carte,self.ligne1(largeur/2,hauteur/2,largeur/2,hauteur/2,1))  #ne va pas bouger

        self.sourisIndex6_1 = Animation(largeur/12,hauteur/2,self.sourisTuto,self.ligne1(largeur/12,hauteur/2,largeur/4,hauteur/2,50))
        self.sourisIndex6_2 = Animation(largeur/4, hauteur/2,self.sourisTutoInv,self.ligne1(largeur/4,hauteur/2,largeur/2,hauteur/2,50))

        self.sourisIndex6_3_1 = Animation(largeur/2,hauteur/2,self.sourisTutoInv,self.ligne1(largeur/2,hauteur/2,largeur/12,hauteur/2,50))
        self.sourisIndex6_3_2 = Animation(largeur/2,hauteur/2,self.sourisTutoInv,self.ligne1(largeur/2,hauteur/2,largeur/1.2,hauteur/2,50))
        self.sourisIndex6_3 = choice([self.sourisIndex6_3_1,self.sourisIndex6_3_2])

        self.carteHearth3_1 = Animation(largeur/2,hauteur/2,self.carteHearth,self.ligne1(largeur/2,hauteur/2,largeur/12,hauteur/2,50))
        self.carteHearth3_2 = Animation(largeur/2,hauteur/2,self.carteHearth,self.ligne1(largeur/2,hauteur/2,largeur/1.2,hauteur/2,50))
        self.carteHearth3 = choice([self.carteHearth3_1,self.carteHearth3_2])

        #Index 7
        #doit contenir Une 1 carte et une souris
        self.carteHearth4 = Animation(largeur/2,hauteur/2,self.carteHearth,self.ligne1(largeur/2,hauteur/2,largeur/2,hauteur/2,1))
        self.cartehearth4_1 = Animation(largeur/2,hauteur/2,self.carteRetourner,self.ligne1(largeur/2,hauteur/2,largeur/2,hauteur/2,1))
        self.sourisIndex7 = Animation(largeur/2,hauteur/2,self.sourisTuto,self.ligne1(largeur/2,hauteur/2,largeur/2,hauteur/2,1))

        #Index 8
        #Affiche un paquet .
        self.sourisIndex8_1 = Animation(largeur/2,hauteur/2,self.sourisTuto,self.ligne1(largeur/2,hauteur/2,largeur/2,hauteur/2,1))






    def ligne1(self,x,y,xP,yP,v):   #x et y = position de depart  xP et yP = position d'arrivé et v = nombre de point :)
        a=[]
        dx = x - xP  # distance entre les 2 points x et xP
        dy = y - yP  # distance entre les 2 points y et yP
        ux = dx / v  # V correspond au nombre de point qui seront crée
        uy = dy / v
        dx = abs(dx)
        dy = abs(dy) #rend compatible la fonction avec les valeurs negatives .
        while dx > 0 or dy > 0:

            x = x - ux
            y = y - uy
            a.append((x, y))  # permet de calculer chaque point un à un

            dx = dx - abs(ux)
            dy = dy - abs(uy)

        return a



    def react(self,event):                   #liste des evenements
        super().react(event)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.back.rect.collidepoint((self.souris.rect.x, self.souris.rect.y)):
            pygame.event.post(pygame.event.Event(SWAP_MENU))
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.imgRegle.rect.collidepoint((self.souris.rect.x, self.souris.rect.y)):
            self.trigger = True
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.box.recti.collidepoint((self.souris.rect.x, self.souris.rect.y)):
            if self.index >= 9 :
                pygame.event.post(pygame.event.Event(SWAP_MENU))      #permet d'eviter un crash le chiffre correspond au nombre de dialogue present dans les listes
            else:
                self.index = self.index + 1


            #Voir thread python




#continuer la suite de sprite

    def draw(self, window):
        super().draw(window)
        if(self.trigger == False):
            self.imgRegle.update(window)
        self.back.update(window)

        if(self.trigger == True):
            self.box.phrase = self.box.font.render(self.box.list_text[self.index], True, (0, 0, 0))
            self.box.phrase1 = self.box.font.render(self.box.list_text2[self.index], True, (0, 0, 0))
            self.box.phrase2 = self.box.font.render(self.box.list_text3[self.index], True, (0, 0, 0))

            if (self.index > 0 and self.index <4):
                if (self.sourisTuto1.step < 50 and self.sourisTuTo1.step == 1):

                    self.sourisTuto1.draw(window)
                    self.sourisTuto1.rectio.center = self.sourisTuto1.animation[self.sourisTuto1.step]
                if(self.sourisTuto1.step ==0 and self.sourisTuTo1.step > 1):
                    self.sourisTuTo1.draw(window)
                    self.sourisTuTo1.rectio.center = self.sourisTuTo1.animation[self.sourisTuTo1.step]


            if (self.index == 2):
                self.time = self.time + 1
                if (self.time%7 == 0):               #permet de ralentir la cadence du programme de cette maniere le sprite bouge pas trop vite
                    if(self.sourisTuto1.step < 50 and self.sourisTuTo1.step == 1):
                        self.sourisTuto1.step = self.sourisTuto1.step + 1

                        if (self.sourisTuto1.step == 50):
                            self.sourisTuTo1.step = 51
                            self.sourisTuto1.step = 0
                    if(self.sourisTuto1.step ==0 and self.sourisTuTo1.step > 1): #j'aurai pu faire un reverse -_-
                        self.sourisTuTo1.step = self.sourisTuTo1.step - 1
                        if (self.sourisTuTo1.step ==1):
                            self.sourisTuto1.step = 0
                            self.sourisTuTo1.step = 1


            if (self.index == 3):
                self.time = self.time +1
                if (self.time%40 == 0):

                    if (self.click == False):
                        self.sourisTuto1.images(self.sourisTutoInv)
                        self.sourisTuTo1.images(self.sourisTutoInv)
                        self.click = True
                    else:
                        self.sourisTuto1.images(self.sourisTuto)
                        self.sourisTuTo1.images(self.sourisTuto)
                        self.click = False
            if (self.index == 4):

                self.carte1.draw(window)
                self.carte1.rectio.center = self.carte1.animation[self.carte1.step]
                self.time = self.time + 1
######################################################################################
                if(self.sourisTuTo2.step != 50):
                    self.sourisTuTo2.draw(window)
                    self.sourisTuTo2.rectio.center = self.sourisTuTo2.animation[self.sourisTuTo2.step] #permet d'avoir 60 fps sur l'animation (je rigole pas c'est 100% réels)
                else:
                    self.sourisTuTo3.draw(window)
                    self.sourisTuTo3.rectio.center = self.carte1.animation[self.carte1.step]
#######################################################################################   Affichage des 2 souris

                if (self.time%5 == 0):

                    if (self.sourisTuTo2.step < 50):

                        self.sourisTuTo2.step = self.sourisTuTo2.step + 1

                    else:
                        if (self.carte1.step < 50):


                            self.carte1.step = self.carte1.step +1


                        if (self.carte1.step == 50):
                            self.sourisTuTo2.step = 0
                            self.sourisTuTo3 = choice([self.sourisTuTo3_1, self.sourisTuTo3_2])
                            self.carte1 = choice([self.carte1_1, self.carte1_2]) #choisi aleatoirement entre les deux animations
                            self.carte1.step = 0
########################################################################################################################
            if(self.index == 5):

                if(self.carte2.step !=50):

                    self.carteAs1.draw(window)
                    self.carteAs1.rectio.center = self.carteAs1.animation[self.carteAs1.step]
                if(self.carteHearth1.step != 50):

                    self.carte2.draw(window)
                    self.carte2.rectio.center = self.sourisIndex5_1.animation[self.sourisIndex5_1.step]

                self.carteHearth1.draw(window)
                self.carteHearth1.rectio.center = self.sourisIndex5_3.animation[self.sourisIndex5_3.step]
                self.time = self.time + 1

                if(self.sourisIndex5_1.step != 50):
                    self.sourisIndex5_1.draw(window)
                    self.sourisIndex5_1.rectio.center = self.sourisIndex5_1.animation[self.sourisIndex5_1.step]
                elif(self.sourisIndex5_2.step != 50):
                    self.sourisIndex5_2.draw(window)
                    self.sourisIndex5_2.rectio.center = self.sourisIndex5_2.animation[self.sourisIndex5_2.step]
                elif(self.sourisIndex5_3.step != 50):
                    self.sourisIndex5_3.draw(window)
                    self.sourisIndex5_3.rectio.center = self.sourisIndex5_3.animation[self.sourisIndex5_3.step]
                elif(self.sourisIndex5_4.step !=1):
                    self.sourisIndex5_4.draw(window)
                    self.sourisIndex5_4.rectio.center = self.sourisIndex5_4.animation[self.sourisIndex5_4.step]

                if(self.time%4 == 0):

                    if(self.sourisIndex5_1.step < 50):
                        self.sourisIndex5_1.step = self.sourisIndex5_1.step +1
                        self.carte2.step = self.carte2.step +1
                    elif(self.sourisIndex5_2.step < 50):
                        self.sourisIndex5_2.step = self.sourisIndex5_2.step +1
                    elif(self.sourisIndex5_3.step < 50):
                        self.sourisIndex5_3.step = self.sourisIndex5_3.step +1
                    elif(self.sourisIndex5_4.step <2):
                        self.sourisIndex5_4.step = self.sourisIndex5_4.step +1  #permet de faire une legere pause dans l'animation avant un reboot

                        pygame.time.wait(500)
                        self.sourisIndex5_3.step = 0
                        self.sourisIndex5_2.step = 0
                        self.sourisIndex5_1.step = 0
                        self.sourisIndex5_4.step = 0
#################################################################################################################
            if(self.index == 6):
                if (self.sourisIndex6_2.step != 50):
                    self.carte3.draw(window)
                    self.carte3.rectio.center = self.carte3.animation[self.carte3.step]
                    self.carteHearth2.draw(window)
                    self.carteHearth2.rectio.center = self.carteHearth2.animation[self.sourisIndex6_2.step]

                self.time = self.time +1

                if(self.sourisIndex6_1.step != 50):
                    self.sourisIndex6_1.draw(window)
                    self.sourisIndex6_1.rectio.center = self.sourisIndex6_1.animation[self.sourisIndex6_1.step]
                elif(self.sourisIndex6_2.step != 50):
                    self.sourisIndex6_2.draw(window)
                    self.sourisIndex6_2.rectio.center = self.sourisIndex6_2.animation[self.sourisIndex6_2.step]
                elif(self.sourisIndex6_3.step !=50):

                    self.carteHearth3.draw(window)
                    self.carteHearth3.rectio.center = self.carteHearth3.animation[self.carteHearth3.step]
                    self.sourisIndex6_3.draw(window)
                    self.sourisIndex6_3.rectio.center = self.carteHearth3.animation[self.carteHearth3.step]


                if(self.time%3 == 0):
                    if(self.sourisIndex6_1.step < 50):
                        self.sourisIndex6_1.step = self.sourisIndex6_1.step +1
                    elif(self.sourisIndex6_2.step < 50):
                        self.sourisIndex6_2.step = self.sourisIndex6_2.step +1
                    elif(self.carteHearth3.step < 50):
                        self.carteHearth3.step = self.carteHearth3.step +1
                    if(self.carteHearth3.step == 50):
                        self.sourisIndex6_1.step = 0
                        self.sourisIndex6_2.step = 0
                        self.carteHearth3 = choice([self.carteHearth3_1, self.carteHearth3_2])
                        self.carteHearth3.step = 0
                        pygame.time.wait(500)
                        self.click = False
####################################################################################################################
            if(self.index == 7):
                self.carteHearth4.draw(window)
                self.carteHearth4.rectio.center = self.carteHearth4.animation[self.carteHearth4.step]
                self.sourisIndex7.draw(window)
                self.sourisIndex7.rectio.center = self.sourisIndex7.animation[self.sourisIndex7.step]
                self.time = self.time + 1

                if (self.time % 60 == 0):

                    if (self.click == False):
                        self.carteHearth4.images(self.carteHearth)
                        self.click = True
                    else:
                        self.carteHearth4.images(self.carteRetourner)
                        self.click = False

###################################################################################################################
            if(self.index == 8):
                if(self.nvPaquet == []):
                    self.nvPaquet.append(Paquet(self.vide, self.joker))


                rect = self.nvPaquet[0][-1].image.get_rect()                                          #la fonction get_rect me permet d'avoir la pos x la pos y la largeur et la hauteur dans cette ordre la .
                x = rect[2]/2                                                                          #permet de prendre la moitié de la largeur
                y = rect[3]/2                                                                          #permet de prendre la moitié de la hauteur afin d'avoir le centre de la carte
                self.nvPaquet[0].teleporter(self.posx/2-x,self.posy/2-y)
                window.blit(self.nvPaquet[0][-1].image,(self.nvPaquet[0].x, self.nvPaquet[0].y))      #concretement Je fais la meme methode pour afficher les 42 cartes avec un paquet mais je n'affiche que la carte du haut car animation oblige
                self.sourisIndex8_1.draw(window)
                self.sourisIndex8_1.rectio.center = self.sourisIndex8_1.animation[self.sourisIndex8_1.step]
                self.time = self.time + 1
                self.click = False
                if(self.time % 50 == 0):
                    self.nvPaquet[0].melanger()






















        if(self.trigger == True):  #doit finir le react afin d'eviter qu'un sprite passe sur la boite de texte
            self.box.collage(window)
        self.souris.update(window)









class Dialogue(pygame.sprite.Sprite):
    def __init__(self,x,y,image,index):
        pygame.sprite.Sprite.__init__(self)


        self.image = image
        self.recti = self.image.get_rect()  # Creation de la hitbox
        self.recti.x = x
        self.recti.y = y

        self.font = pygame.font.Font("police/PermanentMarker.ttf", 30)
        self.list_text = ["Bienvenue sur Card Game nous allons vous", "Voici votre curseur!", "Vous pouvez le deplacer avec votre souris ","Vous pouvez egalement faire un clic gauche","Avec ce clic il est possible de déplacer","Il est possible de former des paquets en ","Avec un ctrl clic gauche il est possible de ","Avec un clic droit il est possible","Avec la touche M il est possible de ","Voila pour l'essentiel"]
        self.list_text2 = ["expliquer comment fonctionne notre jeu", " ", "Comme ceci : "," ","des cartes comme bon vous semble","empilant les cartes les unes sur les autres ","déplacer l'entiereté du paquet. ","de retourner des cartes.","mélanger les paquets .","---> Cliquer pour revenir au menu "]
        self.list_text3 = [" "," "," "," "," "," "," "," ","(Tabulation permet de créer des nouveaux paquets)"," "]
        self.phrase = self.font.render(self.list_text[index], True, (0, 0, 0))
        self.phrase1 = self.font.render(self.list_text2[index], True, (0, 0, 0))
        self.phrase2 = self.font.render(self.list_text3[index], True, (0, 0, 0))



    def collage(self,interface):
        interface.blit(self.image,self.recti)
        interface.blit(self.phrase, (self.recti.x+25,self.recti.y+5))
        interface.blit(self.phrase1, (self.recti.x+25,self.recti.y+30))
        interface.blit(self.phrase2, (self.recti.x + 25, self.recti.y + 55))



class Animation(pygame.sprite.Sprite):
    def __init__(self,x,y,image,parcour,step = 0):
        pygame.sprite.Sprite.__init__(self)

        self.imageD = image
        self.rectio = self.imageD.get_rect()  # Creation de la hitbox
        self.rectio.x = x
        self.rectio.y = y

        self.animation = [(x, y)]
        self.animation.extend((parcour))
        print(self.animation)

        self.step = step


    def draw(self,interface):
        interface.blit(self.imageD,self.rectio)

    def images(self,images):
        self.imageD = images














