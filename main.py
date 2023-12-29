import pygame

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

        for i in range(0, 5):
            Barricade(pos = (SCREEN_HEIGHT // 2 + (i * 32), SCREEN_WIDTH // 2), group = [self.camera_group, self.collision_sprites])
        for i in range(10, 15):
            Barricade(pos = (SCREEN_HEIGHT // 2 + (i * 32), SCREEN_WIDTH // 2), group = [self.camera_group, self.collision_sprites])

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