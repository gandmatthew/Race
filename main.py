import pygame
import math

from settings import *
from player import *
from camera import *
from tile import *

class Game():

    def __init__(self):
        
        pygame.init()

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()

        pygame.display.set_caption("Race")
    
    def run(self):

        self.collision_sprites = pygame.sprite.Group()
        self.camera_group = CameraGroup()

        r = 20

        for x in range(0, r):
            y = round(math.sqrt(pow(r, 2) - pow(x, 2)))
            print(x, y)
            Barricade(pos = (SCREEN_HEIGHT // 2 + (x * 32) - 50, SCREEN_WIDTH // 2 + (y * 32)), group = [self.camera_group, self.collision_sprites])
            Barricade(pos = (-(SCREEN_HEIGHT // 2 + (x * 32) - 50), SCREEN_WIDTH // 2 + (y * 32)), group = [self.camera_group, self.collision_sprites])

        self.player = Player(pos = (SCREEN_HEIGHT // 2 - 32, SCREEN_WIDTH // 2 - 32), group = self.camera_group, obstacles = self.collision_sprites)

        while True:
            self.screen.fill("black") 

            self.camera_group.update()
            self.camera_group.draw(self.player)

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