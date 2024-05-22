import pygame
from pygame.locals import *   # brings in keyboard code

pygame.init()

screen = pygame.display.set_mode((500,500), 0, 32)
sprite1 = pygame.image.load('./images/bee.png')     # loads into memory - image size 172 x 180
sprite1 = pygame.transform.scale(sprite1, (86, 90))     # scale sprite to 86 x 90
spriteWidth = sprite1.get_width()
spriteHeight = sprite1.get_height()
screenWidth = screen.get_width()
screenHeight = screen.get_height()
pygame.display.set_caption('Hello Pygame')      #title
screen.fill((0, 0, 0))      # rgb color - this one is black
x, y = (0,0) # initial position of x, y tuple

# main loop
game_over = False
clock = pygame.time.Clock()
while not game_over:
    dt = clock.tick(30)
    for event in pygame.event.get():        # all events in pygame
        if event.type == pygame.QUIT:
            game_over = True

        # see if the mouse has moved
        elif event.type == pygame.MOUSEMOTION:
            x, y = event.pos
            # center the mouse pointer on the center of the sprite
            x -= spriteWidth/2
            y -= spriteHeight/2
    pressed = pygame.key.get_pressed()  # gets the key pressed
    if pressed[K_UP]:
        y -= 0.5 * dt
    if pressed[K_DOWN]:
        y += 0.5 * dt
    if pressed[K_LEFT]:
        x -= 0.5 * dt
    if pressed[K_RIGHT]:
        x += 0.5 * dt
    if pressed[K_SPACE]:
        x = 0
        y = 0

    # keep from going off the screen to the right
    if x > (screenWidth - spriteWidth):
        x = screenWidth - spriteWidth
    # keep from going off the screen to the bottom
    if y > (screenHeight - spriteHeight):
        y = screenHeight - spriteHeight
    # keep from going off the screen to the left
    if x < 0:
        x = 0
    # keep from going off the screen to the top
    if y < 0:
        y = 0


    screen.fill((0, 0, 0))  # rgb color - this one is black
    screen.blit(sprite1, (x,y))     # adds sprite to the screen
    pygame.display.update()     # refreshes the screen and adds the image

pygame.quit()       # closes the window when the user clicks the X button







