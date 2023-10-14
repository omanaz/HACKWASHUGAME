import pygame
import random
from player import Player

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.screen_width, self.screen_height = pygame.display.get_surface().get_size()
        self.player = Player(10,screen)


    def handle_events(self, event):
        self.player.move(event)
        # Handle game-specific events
        pass
    def update(self):
        self.player.update()
        pass
    def draw(self):
        # Draw the game-specific elements
        # Draw some craters on the moon's surface
        black = (0,0,0)
        white = (255,255,255)
        

        self.screen.fill(black)

        # Draw stars in the night sky
        for _ in range(100):
            x = random.randint(0, self.screen_width)
            y = random.randint(0, self.screen_height)
            pygame.draw.circle(self.screen, white, (x, y), 2)

        moon_fn = r"C:\Users\olove\Desktop\hackwashu\data\moon.png"  # Replace with the path to your image
        moon = pygame.image.load(moon_fn)
        moon = pygame.transform.scale(moon, (self.screen_width, self.screen_height))
        self.screen.blit(moon, (0, 0))
        self.player.draw()
        pygame.display.flip()

    def next_state(self):
        # Determine if the state should change
        return None
