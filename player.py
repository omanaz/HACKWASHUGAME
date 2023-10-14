
import pygame
# from settings import *
# from support import *


class Player(pygame.sprite.Sprite):
    def __init__(self, speed,screen):
        super().__init__()
        self.speed = speed
        self.x = 100
        self.y = 100
        self.screen = screen

        self.image = pygame.image.load(r'C:\Users\olove\Desktop\hackwashu\data\sprite.png')
        self.rect = self.image.get_rect()

    def move(self,keys):
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.x += self.speed
        if keys[pygame.K_UP]:
            self.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.y += self.speed
        pass


    def update(self):
        # Update the sprite's position
        self.rect.x = self.x
        self.rect.y = self.y
        print(self.rect.x,self.rect.y,self.x)
        pygame.display.flip()



    def draw(self):
        self.screen.blit(self.image, self.rect)



