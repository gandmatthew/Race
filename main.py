import pygame

from settings import *
from player import *

class Game():

    def __init__(self):

        pygame.init()

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()

        pygame.display.set_caption("Race")

        self.player = Player(pos = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
    
    def run(self):

        while True:
            self.screen.fill("black")

            self.player.draw(self.screen)
            self.player.update()

            pygame.display.flip()
            self.clock.tick(60)

            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    pygame.quit()
                    exit()

                self.player.keybind(event)

if __name__ == '__main__':
    game = Game()
    game.run()