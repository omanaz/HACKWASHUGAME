import pygame
from game import Game
from menu import Menu
from settings import Settings
from game_over import GameOver

pygame.init()
screen = pygame.display.set_mode()
clock = pygame.time.Clock()
running = True

# Initialize the different game states
# game = Game(screen)
settings = Settings(screen)
current_state = Menu(screen)
menu_active = False
matt = 'matt'

pygame.mixer.init()
pygame.mixer.music.load("data//SONG.mp3")
pygame.mixer.music.play(-1)  # The "-1" argument makes the music loop indefinitely.


while running:
    pygame.mixer.music.set_volume(settings.get_volume())
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        
        if type(current_state) == Game:
            current_state.handle_events(event)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_i:
                    menu_active = not menu_active
                    current_state.player.set_menu(menu_active)
            # if game_over:
            #     current_state = menu
            #     state_name = 'menu'
        else:
            current_state.handle_events(event)
    if type(current_state) == Game:
        keys = pygame.key.get_pressed()  # Get the current keyboard state
        current_state.player.move(keys)
        current_state.player.plant(keys)
        
    current_state.update()
    current_state.draw()
    if current_state.next_state():
        current_state = current_state.next_state()
        if current_state == "game":
            current_state = Game(screen, matt)
            current_state.draw()
            state_name = 'game'
            pass
        elif current_state == "settings":
            current_state = settings
        elif current_state =='menu':
            current_state = Menu(screen)
        elif type(current_state) == GameOver:
            pass
    # Draw the buttons and check for clicks
    

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
