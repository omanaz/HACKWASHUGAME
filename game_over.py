import pygame
import pygame_gui
from pygame_gui.elements import UIButton

class GameOver:
    def __init__(self, screen, points):
        self.screen = screen
        self.points = points 
        font_path = r'data\LycheeSoda.ttf'
        self.font = pygame.font.Font(font_path, 50)
        self.button_x = self.screen_width/2 - (self.button_width/2)
        self.button_y = 100
        self.button_width = 300
        self.button_height = 75
        self.button_color = (255, 0, 0)  # Red color for the button
        self.button_list = ['New Game','Menu','Exit Game']

    def handle_events(self, event):
        
        # Handle menu-specific events
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Check for left mouse button click
                mouse_x, mouse_y = event.pos
                for i, button_text in enumerate(self.button_list):
                    button_rect = pygame.Rect(self.button_x, self.button_y + 100 * i, self.button_width, self.button_height)
                    if button_rect.collidepoint(mouse_x, mouse_y):
                        if button_text == 'New Game':
                            return "game"  # Transition to the game state
                        elif button_text == 'Menu':
                            return "menu"  # Transition to the settings state
                        elif button_text == 'Exit Game':
                            pygame.quit()
                            return None


    def update(self):
        # Update settings-specific logic
        self.ui_manager.update(self.clock.tick(60) / 1000.0)

        
    def draw(self):
        # Draw the menu-specific elements
        game_over_text = self.font.render("Game Over", True, white)

        text_x = self.screen_width // 2 - game_over_text.get_width() // 2
        text_y = self.screen_height // 2 - game_over_text.get_height() // 2

        self.screen.fill((0, 0, 128))  # Navy background color
        self.ui_manager.draw_ui(self.screen)
        # Blit the "Game Over" text onto the screen
        self.screen.blit(game_over_text, (text_x, text_y))

        for i, button_text in enumerate(self.button_list):
            button_rect = pygame.draw.rect(self.screen, self.button_color, (self.button_x, self.button_y + 100 * i, self.button_width, self.button_height))
            text = self.font.render(button_text, True, (255, 255, 255))
            self.screen.blit(text, (self.button_x + 25, self.button_y + 100 * i))


        pygame.display.flip()
    def next_state(self):
        # Determine if the state should change
        return None

    def get_volume(self):
        return self.slider_value