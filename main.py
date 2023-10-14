import pygame
# from game import Game
from menu import Menu
from settings import Settings

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

# Initialize the different game states
# game = Game(screen)
settings = Settings(screen)
current_state = Menu(screen)



while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        state_transition = current_state.handle_events(event)
        if state_transition:
            print('click')
            if state_transition == "game":
                # current_state = game
                pass
            elif state_transition == "settings":
                current_state = settings
    current_state.update()
    current_state.draw()
    # Draw the buttons and check for clicks
    

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
