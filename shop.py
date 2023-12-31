import pygame
import pygame_gui
from pygame_gui.elements import UIButton

class Settings:
    def __init__(self, screen):
        self.screen = screen


    def handle_events(self, event):
        # Handle settings-specific events
        if event.type == pygame.QUIT:
            pygame.quit()
            
    def update(self):
        # Update settings-specific logic
        pass

    def draw(self):
        # Draw the settings-specific elements
        pass

    def next_state(self):
        # Determine if the state should change
        return None
