import pygame
import math


class Plant:
    def __init__(self, x, y, screen, plant_type, Plant_dict):
        self.plant_dict = Plant_dict
        self.x = x
        self.y = y
        self.screen = screen
        self.health = 20
        self.rate = Plant_dict[plant_type]
        self.growth_stage = 0  # Growth stage (0: Seedling, 1: Young, 2: Mature)
        self.water_level = 0  # Water level
        self.is_ready_for_harvest = False
        self.image = pygame.transform.scale(pygame.image.load('data\\plants\\' +str(plant_type)+'.png'), (40, 40))
        # self.image.fill((0, 255, 0))  # Green color for a healthy plant
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.age = 0 #age of the plant in turns 
        self.days_since_water = 0
        # self.is_fertilized = True
        self.plant_type = plant_type
        self.plant_points = 0

    def draw_health_bar(self, screen):
        # Calculate the width of the health bar based on the plant's health
        bar_width = int(40 * (self.health / 100))
        bar_color = (255 - int(255 * (self.health / 100)), int(255 * (self.health / 100)), 0)  # Red to Green

        # Calculate the position of the health bar
        bar_x = self.x
        bar_y = self.y + 60  # Position it just below the plant

        # Draw the health bar
        pygame.draw.rect(screen, bar_color, (bar_x, bar_y, bar_width, 5))

    def update(self):
        # Update the appearance of the plant based on its growth stage and health
        
        self.is_ready_for_harvest = self.growth_stage == 2
        if self.rate <3:
            agecut = math.ceil(self.rate)
        else:
            agecut = 3
        if self.health > 40 + 10*self.rate and self.age %agecut ==0:
            self.grow()

        # if self.plant_type == 'potato':
        #     if self.health > 50:
        #         self.grow()
        # elif self.plant_type == 'carrot':
        #     if (self.age % 2 ==0) and self.health > 70:
        #         self.grow()
        # # Check for growth based on plant type and health
        # else: 
        #     if self.age % 3 == 0 and self.health > 80:  # Plants grow every 3 turns
        #         self.grow()

        self.age += 1


        # Check if the plant is ready for harvest (e.g., at a mature growth stage)
        self.is_ready_for_harvest = self.growth_stage == 2
        self.update_health()

    def draw(self):
        if self.growth_stage > 0:
            self.screen.blit(self.image, self.rect)

    def update_health(self, amount=0):
        decrease_rate = 10 *self.rate
        # if self.is_fertilized:
        #     if (self.plant_type == 'potato' and self.days_since_water == 6):
        #         decrease_rate = 5
        #     elif (self.plant_type == 'carrot' and self.days_since_water == 4):
        #         decrease_rate = 15
        #     elif (self.plant_type == 'spinach' and self.days_since_water == 2):
        #         decrease_rate = 25
        # else:
        #     if (self.plant_type == 'potato' and self.days_since_water == 3):
        #         decrease_rate = 10
        #     elif (self.plant_type == 'carrot' and self.days_since_water == 2):
        #         decrease_rate = 30
        #     elif (self.plant_type == 'spinach' and self.days_since_water == 1):
        #         decrease_rate = 50

                

        health_increase = amount
        self.health += health_increase
        self.health -= decrease_rate

        if self.health < 0:
            self.health = 0
        elif self.health > 100:
            self.health = 100

    def grow(self):
        if self.growth_stage < 2:
            self.growth_stage += 1

    def harvest(self):
        if self.is_ready_for_harvest:
            # Perform harvesting action (e.g., increase player's resources)
            points = 5 *self.rate


    def get_points(self):
        return self.plant_points

            #clear plant and grow spot out of picture
 