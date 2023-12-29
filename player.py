import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group, obstacles):
        super().__init__(group)

        self.rect = pygame.Rect(int(pos[0]), int(pos[1]), 32, 32)
        self.color = (50, 205, 50)
        self.image = pygame.Surface((32, 32))
        self.image.fill(self.color)

        self.velX = 0
        self.velY = 0

        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False

        self.speed = 8
        self.accelerate = 2
        self.reverse = 0.25

        self.obstacles = obstacles

    def collision(self, direction):
        collision_sprites = pygame.sprite.spritecollide(self, self.obstacles, False)
        if (collision_sprites):
            if (direction == "horizontal"):
                for sprite in collision_sprites:
                    if (self.rect.right >= sprite.rect.left and self.old_rect.right <= sprite.old_rect.left):
                        self.rect.right = sprite.rect.left
                        self.rect.x = self.rect.x

                    if (self.rect.left <= sprite.rect.right and self.old_rect.left >= sprite.old_rect.right):
                        self.rect.left = sprite.rect.right
                        self.rect.x = self.rect.x
                        
            if (direction == "vertical"):
                for sprite in collision_sprites:
                    if (self.rect.bottom >= sprite.rect.top and self.old_rect.bottom <= sprite.old_rect.top):
                        self.rect.bottom = sprite.rect.top
                        self.rect.y = self.rect.y

                    if (self.rect.top <= sprite.rect.bottom and self.old_rect.top >= sprite.old_rect.bottom):
                        self.rect.top = sprite.rect.bottom
                        self.rect.y = self.rect.y

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

    def move(self):
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

    def update(self):
        self.old_rect = self.rect.copy()
        self.move()

        self.rect.x += self.velX
        self.collision("horizontal")
        self.rect.y += self.velY
        self.collision("vertical")