import pygame
import random
import math
import time 

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.screen_width = 1280
        self.screen_height = 720

        start_time = time.time()
        # cur_time = start_time()

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

        pygame.draw.circle(self.screen, black, (200, 400), 50)
        pygame.draw.circle(self.screen, black, (500, 300), 70)
        pygame.draw.circle(self.screen, black, (700, 500), 60)

        # Update the screen
        #pygame.display.update()

    def set_scene(self):
        #draw stars 
        black = (0,0,0)
        white = (255,255,255)

        pygame.display.flip()
        self.screen.fill(black)

        # Draw stars in the night sky
        for _ in range(50):
            x = random.randint(0, self.screen_width)
            y = random.randint(0, self.screen_height)
            pygame.draw.circle(self.screen, white, (x, y), 2)
      

    def next_state(self):
        # Determine if the state should change
        return None
