import pygame
import random
from player import Player

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.screen_width, self.screen_height = pygame.display.get_surface().get_size()
        self.player = Player(10,screen)
        self.turn_count = 1


    def handle_events(self, event):

        # if event.type == pygame.KEYDOWN:
        #     self.player.move(event)

        if event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the mouse click occurred within the "End Turn" button

            if event.button == 1:  # Left mouse button
                mouse_x, mouse_y = pygame.mouse.get_pos()
                end_turn_button_rect = pygame.Rect(self.screen_width - 150, 10, 140, 40)

                if end_turn_button_rect.collidepoint(mouse_x, mouse_y):
                    # The mouse click occurred within the "End Turn" button
                    print("End Turn")
                    self.turn_count += 1
        #add function to handle end turn button click
        # Handle game-specific events
        pass
    def update(self):
        self.player.update()
    
        pass
    def draw(self):#, turn_count):
        # Draw the game-specific elements
        black = (0, 0, 0)
        white = (255, 255, 255)

        self.screen.fill(black)

        # Draw stars in the night sky
        for _ in range(100):
            x = random.randint(0, self.screen_width)
            y = random.randint(0, self.screen_height)
            pygame.draw.circle(self.screen, white, (x, y), 2)

        moon_fn = r"C:\Users\o.a.reinhart\Desktop\HACKWASHU\HACKWASHUGAME\data\moon.png"  # Replace with the path to your image
        moon = pygame.image.load(moon_fn)
        moon = pygame.transform.scale(moon, (self.screen_width, self.screen_height))
        self.screen.blit(moon, (0, 0))

        # Draw "End Turn" button in the top right
        end_turn_button = pygame.draw.rect(self.screen, (0, 128, 0), (self.screen_width - 150, 10, 140, 40))
        font = pygame.font.Font(None, 36)
        text = font.render("End Turn", True, white)
        text_rect = text.get_rect(center=end_turn_button.center)
        self.screen.blit(text, text_rect)

        # Draw turn counter to the left of the "End Turn" button
        turn_counter_text = font.render(f"Turn: {self.turn_count}", True, white)
        self.screen.blit(turn_counter_text, (self.screen_width - 300, 10))

        self.player.draw()
        pygame.display.flip()


    def next_state(self):
        # Determine if the state should change
        return None
