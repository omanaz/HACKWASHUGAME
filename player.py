
import pygame
from plant import Plant
# from settings import *
# from support import *
Plant_dict = {
    'potato' : 1,
    'carrot' : 2,
    'spinach' : 5,
    'cabbage' : 2.5,
    'broccoli' : .05,
    'corn' : 3,
    'beet': 2,
    'pepper': 7,
}

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
        self.menu_rects = []
        self.hole = pygame.image.load(r'data\hole.png')
        # self.planted_hole = pygame.image.load(r"data\sprout.png")
        self.water = pygame.image.load(r"data\watered.png")
        self.water = pygame.transform.scale(self.water, (100, 100))
        self.hole = pygame.transform.scale(self.hole, (100, 100))
        # self.planted_hole = pygame.transform.scale(self.planted_hole, (100, 100))
        self.hole_list = []
        self.planted_hole_list = []
        self.watered_list = []
        self.plants = []
        self.selected_plant = 'potato'
        self.firstcol = []
        self.seccol = []

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
        # stop from planting or digging when no digs left
        if keys[pygame.K_RETURN]:
            if self.y < 300:
                return
            # if self.x+100 not in [i[0] for i in self.hole_list]and self.y+10 not in [i[1] for i in self.hole_list]:
            for i in self.hole_list:
                x,y = i
                if self.x+100 > x-100 and self.x+100 < x+100:
                    if self.y+10 > y-100 and self.y+10 < y+100:
                        return

            if self.dig_count >0:
                self.hole_list.append((self.x+100,self.y+10))   
                self.dig_count -=1
            
        if (keys[pygame.K_RSHIFT] or keys[pygame.K_LSHIFT]) and (self.x+100,self.y+10) in self.hole_list:
            new_plant = Plant(self.x+100,self.y+10, self.screen, self.selected_plant, Plant_dict)
            self.planted_hole_list.append(new_plant)
            # call plant 
            self.plants.append(new_plant)
            self.hole_list.remove((self.x+100,self.y+10))

       
        if keys[pygame.K_w]:
            if self.water_count >0:
                self.water_count -=1
                for plant in self.plants:
                    x = plant.x
                    y = plant.y
                    if self.x+100 > x-100 and self.x+100 < x+100:
                        if self.y+10 > y-100 and self.y+10 < y+100:
                            plant.water()
                            print('waterd')

            # for i in self.hole_list:
            #     x,y = i
            #     if not self.x+100 > x-100 and self.x+100 < x+100:
            #         if not self.y+10 > y-100 and self.y+10 < y+100:
            #             print('asdfasd')
            #             return
            # if (self.x+100,self.y+10) in self.hole_list:
            #     if self.water_count >0:
            #         self.watered_list.append((self.x+100,self.y+10))
            #         self.water_count -=1
        #add function to harvest
        # add function to fertilize

    def draw(self):
        self.screen.blit(self.image, self.rect)
        for plant in self.plants:
            if plant.growth_stage < 2:
                plant.draw()
        if self.menu_active:
            self.draw_menu()
        for h in self.hole_list: self.screen.blit(self.hole, h)
        # for ph in self.planted_hole_list: 
        #     # print(self.planted_hole_list[0].check_dead())
        #     # print(self.plants[0].check_dead())
        #     if ph.get_growth_stage()>1:
        #         continue
        #     if ph.check_dead():
        #         continue
            # self.screen.blit(self.planted_hole, (ph.x,ph.y))
            # else:
            #     print('nodead')
        for w in self.watered_list: self.screen.blit(self.water, w)


    def draw_menu(self):
        if not self.menu_active:
            return

        # Define the menu background rectangle
        values = list(Plant_dict.keys())  # Get all values and convert to a list

        # Calculate the midpoint to split the values
        midpoint = len(values) // 2

        # Split the values into two separate lists
        self.firstcol = values[:midpoint]
        self.seccol = values[midpoint:]

        menu_items = [self.firstcol,self.seccol]
        menu_rects = []
        for i, col in enumerate(menu_items):
            col_x = i*150
            for i, item in enumerate(col):
                color = (0, 128, 255)
                if item == self.selected_plant:
                    color =  (255, 0, 0)
                button_rect = pygame.Rect(self.x + 150 + col_x, self.y + 10 + (100 * i), 80, 80)
                pygame.draw.rect(self.screen, color, button_rect)  # Button color

                font = pygame.font.Font(None, 36)
                text_surface = font.render(item, True, (255, 255, 255))
                text_rect = text_surface.get_rect(center=button_rect.center)
                self.screen.blit(text_surface, text_rect)

                menu_rects.append(button_rect)
                #fix in menu add selected
        
        self.menu_rects = menu_rects

    def handle_click(self,mousex,mousey):
        for i, button_rect in enumerate(self.menu_rects):
            if button_rect.collidepoint(mousex, mousey):
                # A button is clicked; set self.selected_plant to the corresponding item
                if i < len(self.firstcol):
                    self.selected_plant = self.firstcol[i]
                else:
                    self.selected_plant = self.seccol[i - len(self.firstcol)]


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
    
        
    def get_points(self):
        sum = 0
        for plant in self.plants:
            sum += plant.get_points()
        return sum