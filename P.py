import pygame
import random
import time
import math

from pygame.examples.moveit import GameObject


class Button(GameObject):
    def __init__(self,
                 x,
                 y,
                 w,
                 h,
                 text,
                 on_click=lambda x: None,
                 padding=0):
        super().__init__(x, y, w, h)
        self.state = 'normal'
        self.on_click = on_click

        self.text = TextObject(x + padding,
                               y + padding, lambda: text,
                               c.button_text_color,
                               c.font_name,
                               c.font_size)


def inp(**kwargs):
    return kwargs.keys()


clock = pygame.time.Clock()
FPS = 30
WIDTH = 800
HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (168, 66, 50)
GREEN = (64, 168, 50)
GRAY = (69, 58, 56)
snake = []
length = 1
direct = ""
pause = 0
pygame.init()
bg = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.update()

k1 = 0
k2 = 0
x = 0
y = 0
size = 10
health = 0
move = 10
x_speed = 0
y_speed = 0
x_coin = -20
y_coin = -20
x_mina = -20
y_mina = -20
attack = 0
mina = [[1, 1]]
countMina = 5

while 1:
    bg.fill(GREEN)
    clock.tick(FPS)
    # if y + size >= 600:
    #     flag = 0
    #     x -= 5
    #     y -= 5
    # elif y <= 0:
    #     flag = 1
    #     x += 5
    #     y += 5
    # elif flag == 0:
    #     x -= 5
    #     y -= 5
    # elif flag == 1:
    #     x += 5
    #     y += 5
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_LEFT:
                if direct != "right":
                    x_speed = -move
                    y_speed = 0
                    direct = "left"
            elif i.key == pygame.K_RIGHT:
                if direct != "left":
                    x_speed = move
                    y_speed = 0
                    direct = "right"
            elif i.key == pygame.K_DOWN:
                if direct != "up":
                    x_speed = 0
                    y_speed = move
                    direct = "down"
            elif i.key == pygame.K_UP:
                if direct != "down":
                    x_speed = 0
                    y_speed = -move
                    direct = "up"
            elif i.key == pygame.K_ESCAPE:
                pygame.display.set_caption("ESCAPE")
                pause = 1
                # if pause == 0:
                #     pause = 1
                #     while pause == 1:
                #         time.sleep(5)
                # else:
                #     pause = 0

    while pause == 1:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause = 0

    if x + size > WIDTH:
        x = 0
    elif y + size > HEIGHT:
        y = 0
    elif x < 0:
        x = WIDTH-size
    elif y < 0:
        y = HEIGHT-size

    x += x_speed
    y += y_speed

    if abs(x-x_coin) < size and abs(y-y_coin) < size:
        health = 0
        if direct == "right":
            snake.append([snake[length-1][0]-size, y])
        if direct == "left":
            snake.append([snake[length-1][0]+size, y])
        if direct == "down":
            snake.append([x, snake[length-1][1]-size])
        if direct == "up":
            snake.append([x, snake[length-1][1]+size])
        length += 1

    if not health:
        health = 1
        x_coin = random.random() * float(WIDTH-size)
        y_coin = random.random() * float(HEIGHT-size)

    # j = 0
    # while j < countMina:
    #     mina.append([random.random() * float(WIDTH - size), random.random() * float(HEIGHT - size)])
    #     pygame.draw.rect(bg, BLACK, (mina[j][0], mina[j][1], size, size))
    #     j += 1
    #
    # j = 0
    # while j < countMina:
    #     if abs(x-mina[j][0]) < size and abs(y-mina[j][1]) < size:
    #         attack = 1
    #     j += 1
    #
    # if attack:
    #     attack = 0
    #     length -= 1
    #     if length != 0:
    #         snake.pop()

    if length > 1:
        i = length-1
        while i > 0:
            snake[i][0] = snake[i - 1][0]
            snake[i][1] = snake[i - 1][1]
            if i == 1:
                snake[0][0] = x
                snake[0][1] = y
                pygame.draw.rect(bg, GRAY, (snake[0][0], snake[0][1], size, size), 2)
                pygame.draw.rect(bg, WHITE, (snake[i][0], snake[i][1], size, size), 2)
            else:
                pygame.draw.rect(bg, WHITE, (snake[i][0], snake[i][1], size, size), 2)
            i -= 1
    else:
        snake.append([x, y])
        # snake[0][0] = x
        # snake[0][1] = y
        pygame.draw.rect(bg, GRAY, (x, y, size, size), 2)

    pygame.draw.rect(bg, RED, (x_coin, y_coin, size, size))
    pygame.display.update()
