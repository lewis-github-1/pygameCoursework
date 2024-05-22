import pygame

pygame.init()

screen = pygame.display.set_mode((800,600), 0, 32)
sprite1 = pygame.image.load('./images/bee.png')     # loads into memory - image size 172 x 180
sprite1 = pygame.transform.scale(sprite1, (86, 90))     # scale sprite to 86 x 90
spriteWidth = sprite1.get_width()
spriteHeight = sprite1.get_height()
screenWidth = screen.get_width()
screenHeight = screen.get_height()

pygame.display.set_caption('Hello Pygame')      #title
screen.fill((0, 0, 0))      # rgb color - this one is black

# main loop
game_over = False

while not game_over:
    for event in pygame.event.get():        # all events in pygame
        if event.type == pygame.QUIT:
            game_over = True
    screen.blit(sprite1, (screenWidth/2 - spriteWidth/2, screenHeight/2 - spriteHeight/2))     # adds sprite to the screen
    pygame.display.update()     # refreshes the screen and adds the image

pygame.quit()       # closes the window when the user clicks the X button







