import pygame

pygame.init()

screen = pygame.display.set_mode((800,600), 0, 32)
sprite1 = pygame.image.load('./images/bee.png')     # loads into memory

pygame.display.set_caption('Hello Pygame')      #title
screen.fill((0, 0, 0))      # rgb color - this one is black

# main loop
game_over = False

while not game_over:
    for event in pygame.event.get():        # all events in pygame
        if event.type == pygame.QUIT:
            game_over = True
    screen.blit(sprite1, (314,210))     # adds sprite to the screen
    pygame.display.update()     # refreshes the screen and adds the image

pygame.quit()       # closes the window when the user clicks the X button







