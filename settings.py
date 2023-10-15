import pygame
import pygame_gui
from pygame_gui.elements import UIButton

class Settings:
    def __init__(self, screen):
        self.screen = screen
        self.ui_manager = pygame_gui.UIManager((1280, 720))
        self.clock = pygame.time.Clock()
        self.slider_value = 0.5  # Initial slider value
        self.nstate = None
        self.button = UIButton(pygame.Rect(100, 100, 100, 40), 'Menu', self.ui_manager)  # Create the button
        self.sprite = 'sprite'
        # Create a slider element
        slider_rect = pygame.Rect(100, 200, 200, 20)
        self.slider = pygame_gui.elements.UIHorizontalSlider(slider_rect, self.slider_value, (0.0, 1.0), self.ui_manager)
        self.sprite_buttons = []

        value_label_rect = pygame.Rect(100, 175, 200, 20)
        self.value_label = pygame_gui.elements.UILabel(value_label_rect, str(self.slider_value), self.ui_manager)


    def handle_events(self, event):
        # Handle settings-specific events
        if event.type == pygame.QUIT:
            pygame.quit()
        self.ui_manager.process_events(event)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.button.rect.collidepoint(event.pos):
                self.nstate = 'menu'

            for button in self.sprite_buttons:
                if button.rect.collidepoint(event.pos):
                    self.sprite = button.text  # Update self.sprite

    def update(self):
        # Update settings-specific logic
        self.ui_manager.update(self.clock.tick(60) / 1000.0)

        # Get the current slider value
        self.slider_value = self.slider.get_current_value()

        # Update the value label with the current slider value
        self.value_label.set_text(f"Volume: {self.slider_value*100:.1f}%")

    def draw(self):
        # Draw the settings-specific elements
        self.screen.fill((0, 0, 128))  # Navy background color
        self.ui_manager.draw_ui(self.screen)
        sprite_names = ['matt', 'sprite', 'cat', 'bear']

        # Define the position and size for the buttons
        button_width, button_height = 100, 40
        button_x, button_y = 100, 300
        vertical_spacing = 50  # Vertical space between buttons

        # Create buttons for each sprite name
        for sprite_name in sprite_names:
            button_rect = pygame.Rect(button_x, button_y, button_width, button_height)
            button = UIButton(button_rect, sprite_name, self.ui_manager)
            self.sprite_buttons.append(button)  # Add the button to the list
            button_y += vertical_spacing


    def next_state(self):
        # Determine if the state should change
        if self.nstate == 'menu':
            self.nstate = None
            return 'menu'
        return self.nstate

    def get_volume(self):
        return self.slider_value
    
    def get_sprite(self):
        return self.sprite