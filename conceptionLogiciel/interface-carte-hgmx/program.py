from paquet import *
from interface import *
from carte import *
from musique import *

fullscreen = pygame.display.Info()
x = fullscreen.current_w                             #renvoi les dimensions actuelle de votre ecran qu'importe la taille
y = fullscreen.current_h                             #Aller voir https://www.pygame.org/docs/ref/display.html#pygame.display.Info pour comprendre
interface = Interface(x, y)

interface.loop()


