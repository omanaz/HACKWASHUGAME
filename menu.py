import pygame

class Menu:
    def __init__(self, screen):
        self.screen = screen

    def handle_events(self, event):
        # Handle menu-specific events
        pass

    def update(self):
        # Update menu-specific logic
        pass

    def draw(self):
        # Draw the menu-specific elements
        # Define button parameters
        self.screen.fill((0, 0, 128))  # Navy background color

        button_x = 100
        button_y = 100
        button_width = 200
        button_height = 50
        button_color = (255, 0, 0)  # Red color for the button
        font = pygame.font.Font(None, 36)
        button_list = ['New Game', 'Settings', 'Exit Game', 'Instructions']
        for i, button_text in enumerate(button_list):
            button_rect = pygame.draw.rect(self.screen, button_color, (button_x, button_y + 100 * i, button_width, button_height))
            text = font.render(button_text, True, (255, 255, 255))
            self.screen.blit(text, (button_x + 25, button_y + 100 * i))

        # Check for button click
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if button_rect.collidepoint(mouse_x, mouse_y) and pygame.mouse.get_pressed()[0]:  # Left mouse button clicked
            print(f"Button Clicked: {button_text}")

    def next_state(self):
        # Determine if the state should change
        return None
