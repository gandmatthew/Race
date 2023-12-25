import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.x = int(pos[0])
        self.y = int(pos[1])
        self.rect = pygame.Rect(self.x, self.y, 32, 32)
        self.color = (250, 120, 60)
        self.velX = 0
        self.velY = 0
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        self.speed = 5
        self.accelerate = 0.5
        self.reverse = 0.10

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def keybind(self, event):
        if (event.type == pygame.KEYUP):
            if (event.key == pygame.K_LEFT):
                self.left_pressed = False
            if (event.key == pygame.K_RIGHT):
                self.right_pressed = False
            if (event.key == pygame.K_UP):
                self.up_pressed = False
            if (event.key == pygame.K_DOWN):
                self.down_pressed = False
        if (event.type == pygame.KEYDOWN):
            if (event.key == pygame.K_LEFT):
                self.left_pressed = True
            if (event.key == pygame.K_RIGHT):
                self.right_pressed = True
            if (event.key == pygame.K_UP):
                self.up_pressed = True
            if (event.key == pygame.K_DOWN):
                self.down_pressed = True

    def update(self):
        if (not self.left_pressed):
            if (self.velX < 0):
                self.velX += self.reverse
        if (not self.right_pressed):
            if (self.velX > 0):
                self.velX -= self.reverse
        if (not self.up_pressed):
            if (self.velY < 0):
                self.velY += self.reverse
        if (not self.down_pressed):
            if (self.velY > 0):
                self.velY -= self.reverse

        if self.left_pressed and not self.right_pressed:
            if (self.velX > 0):
                self.velX -= self.reverse
            if (self.velX >= -self.speed):
                self.velX -= self.accelerate
        if self.right_pressed and not self.left_pressed:
            if (self.velX < 0):
                self.velX += self.reverse
            if (self.velX <= self.speed):
                self.velX += self.accelerate
        if self.up_pressed and not self.down_pressed:
            if (self.velY > 0):
                self.velY -= self.reverse
            if (self.velY >= -self.speed):
                self.velY -= self.accelerate
        if self.down_pressed and not self.up_pressed:
            if (self.velY < 0):
                self.velY += self.reverse
            if (self.velY <= self.speed):
                self.velY += self.accelerate
        
        self.x += self.velX
        self.y += self.velY

        print(self.velX)
        print(self.velY)

        self.rect = pygame.Rect(self.x, self.y, 32, 32)
