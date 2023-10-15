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
        self.rect.topleft = (x+100, y-10)
        self.age = 0 #age of the plant in turns 
        self.days_since_water = 0
        # self.is_fertilized = True
        self.plant_type = plant_type
        self.plant_points = 0
        self.is_dead = False 

    def draw_health_bar(self, screen):
        # Calculate the width of the health bar based on the plant's health
        bar_width = int(40 * (self.health / 100))
        # bar_color = (255 - int(255 * (self.health / 100)), int(255 * (self.health / 100)), 0)  # Red to Green
        bar_color = (255 - min(254,int(255 * (self.health / 100))), min(255,int(255 * (self.health / 100))), 0)  # Red to Green

        # Calculate the position of the health bar
        bar_x = self.x
        bar_y = self.y + 60  # Position it just below the plant

        # Draw the health bar
        pygame.draw.rect(screen, bar_color, (bar_x, bar_y, bar_width, 5))

    def update(self):
        # Update the appearance of the plant based on its growth stage and health        

        if self.rate <3:
            agecut = math.ceil(self.rate)
        else:
            agecut = 3
        if self.health > 40 + 10*self.rate and self.age %agecut ==0:
            self.grow()

        self.is_ready_for_harvest = self.growth_stage == 2

        self.age += 1


        # Check if the plant is ready for harvest (e.g., at a mature growth stage)
        self.is_ready_for_harvest = self.growth_stage == 2
        self.update_health()

    def draw(self):
        if self.is_dead is False:
            self.draw_health_bar(self.screen)
            if self.growth_stage == 0:
                # pygame.transform.scale(self.planted_hole, (100, 100))
                self.screen.blit(pygame.transform.scale(pygame.image.load(r"data\sprout.png"), (100,100)), self.rect)
            else:
                self.screen.blit(self.image, self.rect)

    def update_health(self, amount=0):
        decrease_rate = 10 *self.rate * self.days_since_water

        health_increase = amount
        self.health += health_increase
        self.health -= decrease_rate
        if self.health < 0:
            self.health = 0
        elif self.health > 100:
            self.health = 100

        if self.health == 0: 
            self.is_dead == True #death
            self.image = (0,0)


    def grow(self):
        if self.growth_stage < 2:
            self.growth_stage += 1

    def harvest(self):
        if self.is_ready_for_harvest:
            # Perform harvesting action (e.g., increase player's resources)
            self.plant_points = 5 *self.rate

    def get_points(self):
        return self.plant_points

    def water(self):
        self.days_since_water = 0
        self.health += 10         
         #clear plant and grow spot out of picture

    def check_dead(self):
        # print(self.is_dead)
        if self.health == 0: 
            return True
        return self.is_dead
    
    def get_growth_stage(self):
        print(self.growth_stage)
        return self.growth_stage