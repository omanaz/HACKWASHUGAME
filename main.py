import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

# Define button parameters
button_x = 100
button_y = 100
button_width = 200
button_height = 50
button_color = (255, 0, 0)  # Red color for the button
font = pygame.font.Font(None, 36)
button_list = ['New Game', 'Settings', 'Exit Game', 'Instructions']

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 128))  # Navy background color

    # Draw the buttons and check for clicks
    for i, button_text in enumerate(button_list):
        button_rect = pygame.draw.rect(screen, button_color, (button_x, button_y + 100 * i, button_width, button_height))
        text = font.render(button_text, True, (255, 255, 255))
        screen.blit(text, (button_x + 25, button_y + 100 * i))

        # Check for button click
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if button_rect.collidepoint(mouse_x, mouse_y) and pygame.mouse.get_pressed()[0]:  # Left mouse button clicked
            print(f"Button Clicked: {button_text}")

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
