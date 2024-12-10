
import pygame



class SETTINGS:
    pygame.init()
 


    CLOCK = pygame.pygame.time.tick(60) / 1000
    # window is is in a window^^
    WINDOW = pygame.display.set_mode(800, 600)

    # window is maxed
    WINDOWMAXIMIZED = pygame.display.set_mode(pygame.FULLSCREEN)

    # window will be hidden
    WINHIDE = pygame.WINDOWHIDDEN = pygame.WINDOWHIDDEN

    # window is opened in visible mode (default)
    WINSHOW = pygame.WINDOWSHOWN

    # window will be closed
    WINCLOSED = pygame.WINDOWCLOSE
