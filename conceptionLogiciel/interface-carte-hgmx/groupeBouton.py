from pygame import *
from bouton import *
from event import *


class GroupeBouton(sprite.LayeredUpdates):
    def __init__(self, buttons, x, y):           # buttons sera une liste de chaines de caractères qui permettera d'ajouter tel ou tel bouton au groupe
        super().__init__(self)
        self.x = x
        self.y = y
        self.add_bouton(buttons)

    def add_bouton(self, buttons):
        tmp_button = None

        if isinstance(buttons, Bouton):
            self.add(buttons)
            return

        for button in buttons:
            
            if button == "quitter":
                tmp_button = pygame.image.load("images/Boutton_quitter.png")
                tmp_button = pygame.transform.scale(tmp_button, (60, 60))
                tmp_button = Bouton(self.x - 60, 0, tmp_button, quitter)

            elif button == "jouer":
                tmp_button = pygame.image.load("images/Boutton_play.png")
                tmp_button = Bouton(self.x / 2.4, self.y / 2.4, tmp_button, jouer)

            elif button == "regle":
                tmp_button = pygame.image.load("images/livre.png")
                tmp_button = pygame.transform.scale(tmp_button, (90, 90))
                tmp_button = Bouton(0, 0, tmp_button, regle)
            
            if button == "music":
                tmp_button = pygame.image.load("images/musiqueOn.png")
                tmp_button = BoutonSwap(self.x - 130, 0, tmp_button, music_off, music_on)
                self.add(tmp_button)
                tmp_button = pygame.image.load("images/musiquechangere")
                tmp_button = pygame.transform.scale(tmp_button, (60, 60))
                tmp_button = Bouton(self.x - 200, 0, tmp_button, change_musique)


            # PARAMETRES
            elif button == "param":
                tmp_button = pygame.image.load("images/parametre.png")
                tmp_button = pygame.transform.scale(tmp_button, (60, 60))
                tmp_button = Bouton(self.x - 65, self.y - 65, tmp_button, parametre_on)

            self.add(tmp_button)
            tmp_button = None


    def react(self, event):
        for sprite in self.sprites():
            sprite.react(event)
