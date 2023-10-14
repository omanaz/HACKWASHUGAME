import pygame
import random
import math
import time 

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.screen_width, self.screen_height = pygame.display.get_surface().get_size()

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

        moon_fn = r"C:\Users\o.a.reinhart\Desktop\HACKWASHU\HACKWASHUGAME\data\moon.png"  # Replace with the path to your image
        moon = pygame.image.load(moon_fn)
        moon = pygame.transform.scale(moon, (self.screen_width, self.screen_height))
        self.screen.blit(moon, (0, 0))
        pygame.display.flip()


    def next_state(self):
        # Determine if the state should change
        return None
