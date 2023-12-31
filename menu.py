import pygame
from instructions import Instructions
class Menu:
    def __init__(self, screen):
        self.screen = screen
        #self.surface.fill(51, 0, 102)
        self.screen_width, self.screen_height = pygame.display.get_surface().get_size()
        font_path = r'data\LycheeSoda.ttf'
        self.font = pygame.font.Font(font_path, 36)
        self.button_y = 400
        self.button_width = 300
        self.button_height = 75
        self.button_color = (255, 0, 0)  # Red color for the button
        self.button_list = ['New Game', 'Settings', 'Exit Game', 'Instructions']
        self.button_x = self.screen_width/2 - (self.button_width/2)
        self.nstate = None


    def handle_events(self, event):
        # Handle menu-specific events
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Check for left mouse button click
                mouse_x, mouse_y = event.pos
                for i, button_text in enumerate(self.button_list):
                    button_rect = pygame.Rect(self.button_x, self.button_y + 100 * i, self.button_width, self.button_height)
                    if button_rect.collidepoint(mouse_x, mouse_y):
                        if button_text == 'New Game':
                            self.nstate = 'game'
                            # return "game"  # Transition to the game state
                        elif button_text == 'Settings':
                            self.nstate = 'settings'
                            # return "settings"  # Transition to the settings state
                        elif button_text == 'Instructions':
                            self.nstate = Instructions(self.screen)
                            # return "instructions"  # Transition to the settings state
                        # elif button_text == 'Shop':
                        #     self.nstate = 'shop'
                            # return "shop"  # Transition to the settings state
                        elif button_text == 'Exit Game':
                            pygame.quit()
                            return None

    def update(self):
        # Update menu-specific logic
        pass

    def draw(self):
        # Draw the menu-specific elements
        self.screen.fill((0, 0, 128))  # Navy background color
        title = pygame.font.Font(r'data\LycheeSoda.ttf', 100).render('Asteroid Arboretum', True, (255, 255, 255) )
        self.screen.blit( title, (self.button_x- title.get_width()/4, 150))
        for i, button_text in enumerate(self.button_list):
            button_rect = pygame.draw.rect(self.screen, self.button_color, (self.button_x, self.button_y + 100 * i, self.button_width, self.button_height))
            text = self.font.render(button_text, True, (255, 255, 255))
            self.screen.blit(text, (self.button_x + 25, self.button_y + 100 * i))

    def next_state(self):
        # Determine if the state should change
        print(self.nstate)
        return self.nstate
