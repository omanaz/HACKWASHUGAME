import pygame

class Instructions:
    def __init__(self, screen):
        self.screen = screen
        self.nstate = None
        self.font = pygame.font.Font(None, 36)
        self.button_font = pygame.font.Font(None, 24)
        self.button_color = (255, 0, 0)
        self.button_rect = pygame.Rect(screen.get_width() // 2 - 75, 850, 150, 50) 

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
        instructions_rect.center = (self.screen.get_width() // 2, 80)  # Position the text

        # Create a "Lorem Ipsum" text surface
        in_text ="""
        You are trapped on the asteroid and have to survive for ten days until you’re rescued.\n
        Grow and harvest as many plants as possible under the planting and watering constraints. \n 
        Increase each plant’s chances of growing by adding water. Don’t wait too long to water each plant or they’ll die :( \n
        \n
        Controls: \n
        \n
        Up, Down, Left, and Right arrows: move\n
        Enter: dig hole \n
        I: See plant menu. Click to make plant selection.\n
        Shift: Plant current plant selection, (must be in a dug hole)\n
        W: water plant \n
        """
        lorem_text = self.font.render(in_text, True, (255, 255, 255))  # White text
        lorem_rect = lorem_text.get_rect()
        lorem_rect.center = (self.screen.get_width() // 2, 400)  # Position the text

        pygame.draw.rect(self.screen, self.button_color, self.button_rect)  # Green button
        button_text = self.button_font.render("Menu", True, (255, 255, 255))
        button_rect = button_text.get_rect(center=self.button_rect.center)

        # Draw the text surfaces on the screen
        self.screen.blit(instructions_text, instructions_rect)
        self.screen.blit(lorem_text, lorem_rect)
        self.screen.blit(button_text, button_rect)

    def next_state(self):
        return self.nstate