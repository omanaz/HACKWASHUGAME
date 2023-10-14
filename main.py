import pygame
from game import Game
from menu import Menu
from settings import Settings

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

# Initialize the different game states
game = Game(screen)
settings = Settings(screen)
current_state = Menu(screen)
state_name = 'menu'


while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        
    event_return = current_state.handle_events(event)

    if state_name == 'menu':
            if event_return:
                if event_return == "game":
                    current_state = game
                    state_name = 'game'
                    pass
                elif event_return == "settings":
                    current_state = settings
                    state_name = 'settings'

    current_state.update()
    current_state.draw()
    # Draw the buttons and check for clicks
    

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
