# My Brickbreaker game
# By: Lewis T
# Summer 2023

import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Breaking Bricks")

# paddle
paddle = pygame.image.load('paddle.png')
paddle = paddle.convert_alpha()
paddle_rect = paddle.get_rect()
paddle_rect[1] = screen.get_height() - 65

# brick
brick = pygame.image.load('brick.png')
brick = brick.convert_alpha()
brick_rect = brick.get_rect()
bricks = []
brick_rows = 5
brick_gap = 10
brick_cols = screen.get_width() // (brick_rect[2] + brick_gap)
side_gap = (screen.get_width() - (brick_rect[2] + brick_gap) * brick_cols + brick_gap) // 2

for y in range(brick_rows):
    brickY = y * (brick_rect[3] + brick_gap)
    for x in range(brick_cols):
        brickX = x * (brick_rect[2] + brick_gap) + side_gap
        bricks.append((brickX, brickY))

# ball
ball = pygame.image.load('ball.png')
ball = ball.convert_alpha()
ball_rect = ball.get_rect()
ball_start = (200, 200)     # starting position for the ball
ball_speed = (3.0, 3.0)    # initial speed
ball_served = False         # starts off static and not moving
sx, sy = ball_speed
ball_rect.topleft = ball_start


clock = pygame.time.Clock()
game_over = False
x = 0
while not game_over:
    dt = clock.tick(50)
    screen.fill((0, 0, 0))

    for bc in bricks:
        screen.blit(brick, bc)

    screen.blit(paddle, paddle_rect)
    screen.blit(ball, ball_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    pressed = pygame.key.get_pressed()
    if pressed[K_LEFT]:
        x -= 0.5 * dt
    if pressed[K_RIGHT]:
        x += 0.5 * dt
    if pressed[K_SPACE]:
        ball_served = True

    # if ball is within the left and right edges of the paddle
    # and the ball's bottom is at the same y position as the top of the paddle
    # and the direction of the ball is going down (sy > 0)
    if ball_rect[0] >= paddle_rect[0] and \
        ball_rect[0] <= paddle_rect[0] + paddle_rect.width and \
        ball_rect[1] + ball_rect.height >= paddle_rect[1] and  \
        sy > 0:
        sy *= -1
        sx *= 1.01      #increase the difficulty
        sy *= 1.01
        continue

    delete_brick = None

    for b in bricks:
        bx, by = b
        # if the x of the ball is within the left and right edge of the brick (x coordinate) and
        # if the y of the ball is within the top and bottom edge of the brick (y coordinate) ---> break (delete)
        if bx <= ball_rect[0] <= bx + brick_rect.width and \
            by <= ball_rect[1] <= by + brick_rect.height:
                delete_brick = b

                if ball_rect[0] <= bx + 2:
                    sx *= -1
                elif ball_rect[0] >= bx + brick_rect.width - 2:
                    sx *= -1

                if ball_rect[1] <= by + 2:
                    sy *= -1
                elif ball_rect[1] > by + brick_rect.height - 2:
                    sy *= -1
                break

    if delete_brick is not None:
        bricks.remove(delete_brick)

    # top
    if ball_rect[1] <= 0:
        ball_rect[1] = 0
        sy *= -1
    # right
    if ball_rect[0] >= screen.get_width() - ball_rect.width:
        ball_rect[0] = screen.get_width() - ball_rect.width
        sx *= -1
    # bottom
    if ball_rect[1] >= screen.get_height() - ball_rect.height:
        ball_served = False
        ball_rect.topleft = ball_start
    # left
    if ball_rect[0] <= 0:
        ball_rect[0] = 0
        sx *= -1


    paddle_rect[0] = x
    if ball_served:
        ball_rect[0] += sx
        ball_rect[1] += sy

    pygame.display.update()

pygame.quit()








