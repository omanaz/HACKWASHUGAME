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
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    current_state.draw()
    # Draw the buttons and check for clicks
    

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
