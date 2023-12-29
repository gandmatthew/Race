import pygame

class Barricade(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        self.screen = pygame.display.get_surface()

        self.rect = pygame.Rect(int(pos[0]), int(pos[1]), 32, 32)
        self.color = (255, 0, 0)
        self.image = pygame.Surface((32, 32))
        self.image.fill(self.color)

    def update(self):

        self.old_rect = self.rect.copy()

        pygame.draw.rect(self.screen, self.color, self.rect)
        