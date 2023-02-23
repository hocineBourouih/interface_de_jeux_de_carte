import pygame
import time
from event import *

pygame.mixer.init()


playlist = list()
playlist.append ( "musiques/musique1.mp3" )  # charger la musique 1
playlist.append ( "musiques/music2.mp3" )
playlist.append ( "musiques/music3.mp3" )  # charger la musique 2
playlist.append ( "musiques/music4.mp3" )  # charger la musique 3

music_index = 0

pygame.mixer.music.set_endevent(CHANGE_MUSIC)   
pygame.mixer.music.load(playlist[music_index])  
pygame.mixer.music.play()   

def next_music():
    global music_index
    pygame.mixer.music.stop()
    music_index = (music_index + 1)%(len(playlist))
    pygame.mixer.music.load(playlist[music_index])
    pygame.mixer.music.play()