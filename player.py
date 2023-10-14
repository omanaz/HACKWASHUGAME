
import pygame
# from settings import *
# from support import *


class Player(pygame.sprite.Sprite):
    def __init__(self, speed,screen):
        super().__init__()
        self.speed = speed
        self.x = 300
        self.y = 300
        self.screen = screen

        self.image = pygame.image.load(r'C:\Users\o.a.reinhart\Desktop\HACKWASHU\HACKWASHUGAME\data\sprite.png')
        self.rect = self.image.get_rect()

        self.hole = pygame.image.load(r'C:\Users\o.a.reinhart\Desktop\HACKWASHU\HACKWASHUGAME\data\hole.xcf')
        self.planted_hole = pygame.image.load(r"C:\Users\o.a.reinhart\Desktop\HACKWASHU\HACKWASHUGAME\data\planted_hole.xcf")
        self.hole = pygame.transform.scale(self.hole, (500, 250))
        self.planted_hole = pygame.transform.scale(self.planted_hole, (500, 250))
        self.hole_list = []
        self.planted_hole_list = []

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

    def plant(self, keys):
        #have the character dig holes
        if keys[pygame.K_RETURN]:
            self.hole_list.append([self.x-100,self.y])
            
        if (keys[pygame.K_RSHIFT] or keys[pygame.K_LSHIFT]) and self.x-100 in [i[0] for i in self.hole_list]:
            self.planted_hole_list.append([self.x-100,self.y])
        else: 
            print(self.hole_list)
            print(self.x-100)

    def draw(self):
        self.screen.blit(self.image, self.rect)
        for h in self.hole_list: self.screen.blit(self.hole, h)
        for ph in self.planted_hole_list: self.screen.blit(self.planted_hole, ph)



