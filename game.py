import pygame
import random
import math
import time 

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.screen_width = 1280
        self.screen_height = 720

    def handle_events(self, event):
        
        # Handle game-specific events
        pass
    def update(self):
        # Update game-specific logic
        pass
    def draw(self):
        # Draw the game-specific elements
        # Draw some craters on the moon's surface
        black = (0,0,0)
        white = (255,255,255)

        # Update the screen
        #pygame.display.update()

    def set_scene(self):
        #draw stars 
        black = (0,0,0)
        white = (255,255,255)
        gray = (0,0,100)
        curve_height = 700
        rect = (0, 700, 1280, 600)

        pygame.display.flip()
        self.screen.fill(black)

        # Draw stars in the night sky
        for _ in range(50):
            x = random.randint(0, self.screen_width)
            y = random.randint(0, self.screen_height)
            pygame.draw.circle(self.screen, white, (x, y), 2)

        moon_fn = "background.jpg"  # Replace with the path to your image
        moon = pygame.image.load(BACKGROUND_IMAGE)
        moon = pygame.transform.scale(background, (self.screen_width, self.screen_height))
        
       # screen.blit(background, (0, 0))


    def next_state(self):
        # Determine if the state should change
        return None
