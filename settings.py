import pygame
import pygame_gui
from pygame_gui.elements import UIButton

class Settings:
    def __init__(self, screen):
        self.screen = screen
        self.ui_manager = pygame_gui.UIManager((1280, 720))
        self.clock = pygame.time.Clock()
        self.slider_value = 0.5  # Initial slider value

        button_rect = pygame.Rect(100, 100, 100, 40)  # Define the button's position and size
        self.button = UIButton(button_rect, 'Menu', self.ui_manager)  # Create the button

        # Create a slider element
        slider_rect = pygame.Rect(100, 200, 200, 20)
        self.slider = pygame_gui.elements.UIHorizontalSlider(slider_rect, self.slider_value, (0.0, 1.0), self.ui_manager)


        value_label_rect = pygame.Rect(100, 175, 200, 20)
        self.value_label = pygame_gui.elements.UILabel(value_label_rect, str(self.slider_value), self.ui_manager)


    def handle_events(self, event):
        # Handle settings-specific events
        if event.type == pygame.QUIT:
            pygame.quit()
        self.ui_manager.process_events(event)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.button.rect.collidepoint(event.pos):
                return 'menu'

    def update(self):
        # Update settings-specific logic
        self.ui_manager.update(self.clock.tick(60) / 1000.0)

        # Get the current slider value
        self.slider_value = self.slider.get_current_value()*100

        # Update the value label with the current slider value
        self.value_label.set_text(f"Volume: {self.slider_value:.1f}%")

    def draw(self):
        # Draw the settings-specific elements
        self.screen.fill((0, 0, 128))  # Navy background color
        self.ui_manager.draw_ui(self.screen)

    def next_state(self):
        # Determine if the state should change
        return None
