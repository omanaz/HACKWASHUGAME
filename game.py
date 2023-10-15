import pygame
import random
from player import Player
# from plant import Plant

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.screen_width, self.screen_height = pygame.display.get_surface().get_size()
        self.player = Player(10,screen)
        self.turn_count = 1
        self.water_count = 3
        self.dig_count = 2
        self.sunx = 190
        self.suny = 30
        self.player.set_water(3)
        self.player.set_dig(2)


    def handle_events(self, event):

        # if event.type == pygame.KEYDOWN:
        #     self.player.move(event)

        if event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the mouse click occurred within the "End Turn" button

            if event.button == 1:  # Left mouse button
                mouse_x, mouse_y = pygame.mouse.get_pos()
                end_turn_button_rect = pygame.Rect(self.screen_width - 150, 10, 140, 40)

                if end_turn_button_rect.collidepoint(mouse_x, mouse_y):
                    # The mouse click occurred within the "End Turn" button
                    print("End Turn")

                    

                    self.turn_count += 1
                    if self.turn_count <= 10:
                        self.player.set_water(3)
                        self.player.set_dig(2)
                        self.sunx +=190
                        for plant in self.player.get_plants():
                            plant.update()
                            
                        if self.turn_count > 3 and self.turn_count < 7:
                            self.suny = 0
                        else:
                            self.suny = 30
                if self.turn_count == 11:
                    self.turn_count = 0
                    self.sunx = 150
                    self.suny = 30
                    return True
        #add function to handle end turn button click
        # Handle game-specific events
        return False
    def update(self):
        self.player.update()
    
        pass
    def draw(self):#, turn_count):
        # Draw the game-specific elements
        black = (0, 0, 0)
        white = (255, 255, 255)

        self.screen.fill(black)

        # Draw stars in the night sky
        for _ in range(150):
            x = random.randint(0, self.screen_width)
            y = random.randint(0, self.screen_height)
            pygame.draw.circle(self.screen, white, (x, y), 5)

        moon_fn = r"data\moon.png"  # Replace with the path to your image
        moon = pygame.image.load(moon_fn)
        moon = pygame.transform.scale(moon, (self.screen_width, self.screen_height))
        self.screen.blit(moon, (0, 0))

        # Draw "End Turn" button in the top right
        end_turn_button = pygame.draw.rect(self.screen, (0, 128, 0), (self.screen_width - 150, 10, 140, 40))
        font = pygame.font.Font(None, 36)
        text = font.render("End Turn", True, white)
        text_rect = text.get_rect(center=end_turn_button.center)
        self.screen.blit(text, text_rect)

        # Draw turn counter to the left of the "End Turn" button
        turn_counter_text = font.render(f"Turn: {self.turn_count}", True, white)
        self.screen.blit(turn_counter_text, (self.screen_width - 300, 10))

        self.player.draw()

        self.get_dig()
        self.get_water()
        self.screen.blit(pygame.transform.scale(pygame.image.load('data/sun.png'),(150,150)),(self.sunx,self.suny))
        self.screen.blit(pygame.transform.scale(pygame.image.load('data/water.png'),(150,150)),(10,10))
        self.screen.blit(pygame.transform.scale(pygame.image.load('data/shovel.png'),(70,70)),(50,150))
        self.screen.blit(pygame.font.Font(None,60).render(str(self.water_count), True, white),(20,75))
        self.screen.blit(pygame.font.Font(None,60).render(str(self.dig_count), True, white),(20,170))
        pygame.display.flip()


    def next_state(self):
        # Determine if the state should change
        return None

    def get_water(self):
        self.water_count = self.player.get_water()
        return self.water_count 
    def get_dig(self):
        self.dig_count = self.player.get_dig()
        return self.dig_count 
