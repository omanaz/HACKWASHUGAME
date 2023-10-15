import pygame

class Instructions:
    def __init__(self, screen):
        self.screen = screen
        self.nstate = None
        self.font = pygame.font.Font(None, 36)
        self.button_font = pygame.font.Font(None, 24)
        self.button_color = (255, 0, 0)
        self.button_rect = pygame.Rect(screen.get_width() // 2 - 75, 450, 150, 50) 

    def handle_events(self, event):
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Check for left mouse button click
            if self.button_rect.collidepoint(event.pos):
                self.nstate = 'menu'

    def update(self):
        pass

    def draw(self):
        # Clear the screen
        self.screen.fill((0, 0, 128))  # Navy background color

        # Create a "Instructions" text surface
        instructions_text = self.font.render("Instructions", True, (255, 255, 255))  # White text
        instructions_rect = instructions_text.get_rect()
        instructions_rect.center = (self.screen.get_width() // 2, 100)  # Position the text

        # Create a "Lorem Ipsum" text surface
        lorem_text = self.font.render("Lorem Ipsum", True, (255, 255, 255))  # White text
        lorem_rect = lorem_text.get_rect()
        lorem_rect.center = (self.screen.get_width() // 2, 200)  # Position the text

        pygame.draw.rect(self.screen, self.button_color, self.button_rect)  # Green button
        button_text = self.button_font.render("Menu", True, (255, 255, 255))
        button_rect = button_text.get_rect(center=self.button_rect.center)

        # Draw the text surfaces on the screen
        self.screen.blit(instructions_text, instructions_rect)
        self.screen.blit(lorem_text, lorem_rect)
        self.screen.blit(button_text, button_rect)

    def next_state(self):
        return self.nstate