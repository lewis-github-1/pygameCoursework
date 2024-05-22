import pygame

pygame.init()

screen = pygame.display.set_mode((640,480), 0, 32)

pygame.display.set_caption('Hello Pygame')      #title
screen.fill((0, 0, 0))      # rgb color - this one is black

# main loop
game_over = False

while not game_over:
    for event in pygame.event.get():        # all events in pygame
        if event.type == pygame.QUIT:
            game_over = True

pygame.quit()       # closes the window when the user clicks the X button







