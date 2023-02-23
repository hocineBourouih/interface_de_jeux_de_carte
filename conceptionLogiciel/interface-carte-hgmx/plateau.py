from frame import *
from event import *
from paquet import *
from exceptions import *
import pygame


class Plateau(Frame):
    def __init__(self, largeur, hauteur):
        super().__init__(largeur, hauteur)
        self.paquets = []
        self.carte_en_main = Paquet(vide=True)
        self.fond_ecran = pygame.image.load("images/plateau.jpeg")
        self.fond_ecran = pygame.transform.scale(self.fond_ecran, (largeur, hauteur))

        self.boutons.add_bouton(["quitter", "param", "music"])

        self.creer_paquet()
        self.paquets[0].teleporter(300, 300)
        self.paquets[0].melanger()

        self.souris = Souris()

        pygame.mouse.get_rel()

    def react(self, event):
        super().react(event)
        self.boutons.react(event)

        if event.type == pygame.KEYDOWN and event.key == K_TAB:
            pygame.event.post(pygame.event.Event(SELECTEUR_SWAP_ON))

        # PRENDRE UNE CARTE DANS LA MAIN
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not self.keyDict[pygame.K_LCTRL]:
            for paquet in self.paquets[::-1]:
                if paquet[-1].rect.collidepoint(pygame.mouse.get_pos()):
                    self.carte_en_main.add(paquet[-1])
                    paquet.remove(paquet[-1])
                    #print("Transfert paquet vers main")
                    if paquet.sprites() == []:
                        #print("Suppression du paquet")
                        self.paquets.remove(paquet)
                    break

        # SORTIR UNE CARTE DE LA MAIN
            # - CRÉER UN PAQUET LORSQUE LA MAIN NE TOUCHE PAS DE PAQUET
            # - INSÉRER LA CARTE EN MAIN DANS LE PAQUET SINON 
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1 and len(self.carte_en_main) < 2:
            self.souris.reinitialiser()
            
            if self.carte_en_main.sprites() == []:
                return

            carte_dans_paquet = False

            for paquet in self.paquets:
                #print(paquet.taille())
                if (abs(self.carte_en_main[0].rect.centerx - paquet[len(paquet)-1].rect.centerx) < 50
                and abs(self.carte_en_main[0].rect.centery - paquet[len(paquet)-1].rect.centery) < 50):
                    self.carte_en_main[0].rect.centerx = paquet[-1].rect.centerx
                    self.carte_en_main[0].rect.centery = paquet[-1].rect.centery
                    paquet.add(self.carte_en_main[0])

                    #print("Transfert main vers paquet")
                    carte_dans_paquet = True
                    break

            if not carte_dans_paquet:
                paq = Paquet(vide=True)
                self.paquets.append(paq)
                paq.add(self.carte_en_main[0])
                #print("Création du paquet")
            self.carte_en_main.empty()  # Enlève la carte de la main


        # RETOURNER LA CARTE:
            # - SI AUCUNE CARTE EN MAIN, RETOURNE LA CARTE SOUS LA SOURIS
            # - SINON, RETOURNE LA CARTE EN MAIN
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3 and not self.keyDict[pygame.K_LCTRL]:  # Lorsque clic droit enfoncé
            if self.carte_en_main.sprites() != []:  # si main non vide
                self.carte_en_main.retourner()  # retourne la carte dans la main
            else:
                for paquet in self.paquets[::-1]:  # sinon test si carte en dessous de la souris puis la retourne
                    if paquet.sprites()[-1].rect.collidepoint(pygame.mouse.get_pos()):
                        paquet[-1].retourner()
                        break

        # PREND UN PAQUET
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.keyDict[pygame.K_LCTRL]:
            print(enumerate(self.paquets))
            for i, paq in list(enumerate(self.paquets))[::-1]:
                if paq[-1].rect.collidepoint(pygame.mouse.get_pos()):
                    self.carte_en_main = paq
                    self.paquets.pop(i)
                    break
        # LACHE PAQUET EN MAIN
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            for paquet in self.paquets:
                if (abs(self.carte_en_main[0].rect.centerx - paquet[len(paquet)-1].rect.centerx) < 50
                and abs(self.carte_en_main[0].rect.centery - paquet[len(paquet)-1].rect.centery) < 50):
                    paquet.ajouter_cartes(self.carte_en_main)
                    self.carte_en_main = Paquet(True)
                    return

            self.paquets.append(self.carte_en_main)
            self.carte_en_main = Paquet(True)
        
        # RETOURNE UN PAQUET
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3 and self.keyDict[pygame.K_LCTRL]:
            print(self.carte_en_main.sprites())
            if self.carte_en_main.sprites() != []:
                self.carte_en_main.retourner()
            for paq in self.paquets[::-1]:
                if paq[-1].rect.collidepoint(pygame.mouse.get_pos()):
                    paq.retourner()

        #MELANGER UN PAQUET
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_m:
            if self.carte_en_main.taille() != 0:
                self.carte_en_main.melanger()
                return
            for paq in self.paquets[::-1]:
                if paq[-1].rect.collidepoint(pygame.mouse.get_pos()):
                    paq.melanger()

        ### DEBUG
        if (event.type == pygame.MOUSEBUTTONUP or event.type == pygame.MOUSEBUTTONDOWN) and event.button == 1:
            print("_____________________________________________________")
            if event.type == pygame.MOUSEBUTTONDOWN:
                print("ENFONCÉ")
            elif event.type == pygame.MOUSEBUTTONUP:
                print("DÉSENFONCÉ")
            for i, paq in enumerate(self.paquets):
                print(" Paquet", i, ":", len(paq), "Position :",(paq.x, paq.y))
            print(" Cartes en main :", len(self.carte_en_main), "Position :",(paq.x, paq.y))
            if event.type == pygame.MOUSEBUTTONUP:
                print("\n")
            

    def draw(self, window):
        super().draw(window)

        card_update = []
        for paquet in self.paquets:
            paquet.draw(window)

        move = pygame.mouse.get_rel()
        for carte in self.carte_en_main.sprites():
            carte.deplacer(move[0], move[1])
        self.carte_en_main.draw(window)

        self.souris.update(window)

    def __getitem__(self, i):
        return self.paquets[i]

    def creer_paquet(self, vide=False, joker=False):  # cree un paquet sur le plateau
        self.paquets.append(Paquet(vide, joker))

    def supprimer_paquet(self, paquet):  # supprime un paquet du plateau
        for i in range(len(self.paquets)):
            if self.paquets[i] is paquet:
                self.paquets.pop(i)
                del paquet
                return
        raise paquetPasSurLePlateauError(self)

    def ajouter_paquet(self, paquet):  # ajoute un paquet deja existant sur le plateau
        self.paquets.append(paquet)
 