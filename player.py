
import pygame
from plant import Plant
# from settings import *
# from support import *


class Player(pygame.sprite.Sprite):
    def __init__(self, speed,screen):
        super().__init__()
        self.water_count = 0
        self.dig_count = 0
        self.speed = speed
        self.x = 300
        self.y = 300
        self.screen = screen
        self.menu_active = False
        self.image = pygame.image.load(r'data\sprite.png')
        self.rect = self.image.get_rect()

        self.hole = pygame.image.load(r'data\hole.png')
        self.planted_hole = pygame.image.load(r"data\planted_hole.png")
        self.water = pygame.image.load(r"data\watered.png")
        self.hole = pygame.transform.scale(self.hole, (100, 100))
        self.planted_hole = pygame.transform.scale(self.planted_hole, (100, 100))
        self.hole_list = []
        self.planted_hole_list = []
        self.watered_list = []
        self.plants = []
        self.selected_plant = 'potato'

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
        pygame.display.flip()
        for plant in self.plants:
            plant.draw_health_bar(self.screen)

    def plant(self, keys):
        #have the character dig holes
        if keys[pygame.K_RETURN]:
            # if self.x+100 not in [i[0] for i in self.hole_list]and self.y+10 not in [i[1] for i in self.hole_list]:
            self.hole_list.append((self.x+100,self.y+10))   
            self.dig_count -=1
            
        if (keys[pygame.K_RSHIFT] or keys[pygame.K_LSHIFT]) and (self.x+100,self.y+10) in self.hole_list:
            self.planted_hole_list.append((self.x+100,self.y+10))
            # call plant 
            self.plants.append(Plant(self.x+100,self.y+10, self.selected_plant))

       
        if keys[pygame.K_w]:
            self.watered_list.append([self.x-100, self.y])
            self.water_count -=1
        #add function to harvest
        # add function to fertilize

    def draw(self):
        self.screen.blit(self.image, self.rect)
        if self.menu_active:
            self.draw_menu()
        for w in self.watered_list: self.screen.blit(self.water, w)
        for h in self.hole_list: self.screen.blit(self.hole, h)
        for ph in self.planted_hole_list: self.screen.blit(self.planted_hole, ph)


    def draw_menu(self):
        if not self.menu_active:
            return

        # Define the menu background rectangle
        menu_items = [['1', '2', '3','4'],['1', '2', '3','4']]
        menu_rects = []
        for i, col in enumerate(menu_items):
            col_x = i*150
            for i, item in enumerate(col):
                button_rect = pygame.Rect(self.x + 150 + col_x, self.y + 10 + (100 * i), 80, 80)
                pygame.draw.rect(self.screen, (0, 128, 255), button_rect)  # Button color

                font = pygame.font.Font(None, 36)
                text_surface = font.render(item, True, (255, 255, 255))
                text_rect = text_surface.get_rect(center=button_rect.center)
                self.screen.blit(text_surface, text_rect)

                menu_rects.append(button_rect)
                #fix in menu add selected


    def set_menu(self,setting):
        self.menu_active = setting
    def set_water(self, water):
        self.water_count = water
    def set_dig(self, dig):
        self.dig_count = dig
    def get_water(self):
        return self.water_count
    def get_dig(self):
        return self.dig_count 
    def get_plants(self):
        return self.plants