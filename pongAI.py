"""
created by Mason Greseth
last edited 7/2/2022
"""

import pygame
import os
import random

win_height = 500
win_width = 800
window = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Pong vs. AI")
white = (255, 255, 255)
black = (0, 0, 0)
fps = 60 # fps remains constant no matter speed of computer
paddle_width = 30
paddle_height = 60
start_y = win_height / 2 - paddle_width / 2
player_start_x = 0
comp_start_x = win_width - paddle_width
vel = 5
ball_length = 10

player_image = pygame.image.load(os.path.join('Assets', 'paddle.png'))
player = pygame.transform.scale(player_image, (paddle_width, paddle_height))
computer_image = pygame.image.load(os.path.join('Assets', 'paddle.png'))
computer = pygame.transform.scale(computer_image, (paddle_width, paddle_height))
ball_image = pygame.image.load(os.path.join('Assets', 'ball.png'))
ball = pygame.transform.scale(ball_image, (ball_length, ball_length))

def draw_window(player_rect, comp_rect, ball_rect):
    window.fill(white)
    window.blit(player, (player_rect.x, player_rect.y))
    window.blit(computer, (comp_rect.x, comp_rect.y))
    window.blit(ball, (ball_rect.x, ball_rect.y))
    #pygame.draw.rect(window, black, ball_rect)
    pygame.display.update()

def move_paddle(keys_pressed, player_rect):
    if keys_pressed[pygame.K_UP] and player_rect.y > 0:
        player_rect.y -= vel
    if keys_pressed[pygame.K_DOWN] and player_rect.y < win_height - paddle_height:
        player_rect.y += vel

def move_ball(ball_rect, ball_x_vel, ball_y_vel):
    ball_rect.x -= ball_x_vel
    ball_rect.y -= ball_y_vel

def check_hit(ball_rect, player_rect, comp_rect):
    if ball_rect.colliderect(player_rect) or ball_rect.colliderect(comp_rect):
        return True
    return False

def check_miss(ball_rect):
    if ball_rect.x < paddle_width - 5 or ball_rect.x > win_width - paddle_width + 5:
        return True

def check_bounds(ball_rect):
    if ball_rect.y >= win_height - ball_length or ball_rect.y <= 0:
        return True
    return False

def move_comp(comp_rect, ball_rect, ball_x_vel):
    if ball_x_vel < 0 and ball_rect.x > win_width / 2:
        comp_vel = 0
        if ball_rect.y - comp_rect.y > paddle_height / 2:
            comp_vel = 3
        elif ball_rect.y - comp_rect.y < paddle_height / 2:
            comp_vel = -3
        comp_rect.y += comp_vel

def serve(ball_rect, comp_rect, player_rect):
    comp_rect.x = comp_start_x
    comp_rect.y = start_y
    player_rect.x = player_start_x
    player_rect.y = start_y
    ball_rect.x = win_width / 2
    ball_rect.y = win_height / 2
    pygame.time.delay(1000)

def main():
    player_rect = pygame.Rect(player_start_x, start_y, paddle_width, paddle_height)
    comp_rect = pygame.Rect(comp_start_x, start_y, paddle_width, paddle_height)
    ball_rect = pygame.Rect(win_width / 2, win_height / 2, ball_length, ball_length)
    ball_x_vel = 6
    ball_y_vel = random.randint(-4, 4)
    clock = pygame.time.Clock()
    pygame.font.init()
    font = pygame.font.SysFont(None, 40)
    img = font.render('PRESS ANY BUTTON TO START', True, black)
    window.fill(white)
    window.blit(img, (185, 210))
    pygame.display.update()
    start = True
    quit = False
    while start and not quit:
        clock.tick(fps)  # speed of while loop
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                start = False
            if event.type == pygame.QUIT:
                quit = True
    if quit:
        pygame.quit()
        return

    pygame.time.delay(500)
    run = True
    while run:
        clock.tick(fps) # speed of while loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys_pressed = pygame.key.get_pressed()
        move_paddle(keys_pressed, player_rect)
        if check_hit(ball_rect, player_rect, comp_rect):
            ball_x_vel *= -1
            ball_y_vel = random.randint(-3, 3)
        if check_miss(ball_rect):
            serve(ball_rect, comp_rect, player_rect)
            ball_y_vel = random.randint(-3, 3)
        if check_bounds(ball_rect):
            ball_y_vel *= -1
        move_ball(ball_rect, ball_x_vel, ball_y_vel)
        move_comp(comp_rect, ball_rect, ball_x_vel)
        draw_window(player_rect, comp_rect, ball_rect)
    pygame.quit()

if __name__ == "__main__":
    main()
