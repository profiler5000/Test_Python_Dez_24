import pygame

from Game.src.settings import SETTINGS

class Game:
    def __init__(self):
        pygame.init()
        self.window = SETTINGS.WINDOWMAXIMIZED
        self.quit = SETTINGS.WINCLOSED
        self.deltatime = SETTINGS.CLOCK
        self.run = True

        def running(self):
            while self.run:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.run = False
                        self.quit()
                self.window.fill(255, 255, 255)
                pygame.display.update()
                #('Green', rect=None, special_flags=0)

game = Game()
game.run()

                        
        
