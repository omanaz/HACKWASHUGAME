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
menu_active = False

pygame.mixer.init()
pygame.mixer.music.load("data//SONG.mp3")
pygame.mixer.music.play(-1)  # The "-1" argument makes the music loop indefinitely.


while running:
    pygame.mixer.music.set_volume(settings.get_volume())
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        
        if state_name == 'game':
            game_over = game.handle_events(event)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_i:
                    menu_active = not menu_active
                    game.player.set_menu(menu_active)
            if game_over:
                current_state = menu
                state_name = 'menu'
        else:
            event_return = current_state.handle_events(event)

            if event_return:
                if event_return == "game":
                    current_state = game
                    game.draw()
                    state_name = 'game'
                    pass
                elif event_return == "settings":
                    current_state = settings
                elif event_return =='menu':
                    current_state = menu
    if state_name == 'game':
        keys = pygame.key.get_pressed()  # Get the current keyboard state
        game.player.move(keys)
        game.player.plant(keys)
        
    current_state.update()
    current_state.draw()
    # Draw the buttons and check for clicks
    

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
