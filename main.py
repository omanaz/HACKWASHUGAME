import pygame
from game import Game
from menu import Menu
from settings import Settings

pygame.init()
screen = pygame.display.set_mode()
clock = pygame.time.Clock()
running = True

# Initialize the different game states
game = Game(screen)
settings = Settings(screen)
menu = Menu(screen)
current_state = Menu(screen)
state_name = 'menu'


while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        
    event_return = current_state.handle_events(event)

    if event_return:
        if event_return == "game":
            current_state = game
            game.set_scene()
            # state_name = 'game'
            pass
        elif event_return == "settings":
            current_state = settings
            # state_name = 'settings'
        elif event_return =='menu':
            current_state = menu


    current_state.update()
    current_state.draw()
    # Draw the buttons and check for clicks
    

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
