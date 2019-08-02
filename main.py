import pygame as pg
import sys
import random
import math
import os
# init
pg.init()
pg.font.init()

# font
title_font = pg.font.SysFont('MalgumGothic', 96)
block_font1 = pg.font.SysFont('MalgunGothic', 72)
block_font2 = pg.font.SysFont('MalgunGothic', 55)
block_font3 = pg.font.SysFont('MalgunGothic', 32)

# clock
clock = pg.time.Clock()

# color
COLOR_YELLOW = pg.Color(255, 255, 0)
COLOR_WHITE = pg.Color(255, 255, 255)
COLOR_BLACK = pg.Color(0, 0, 0)
COLOR_BLOCK = [pg.Color(244, 203, 255), pg.Color(234, 193, 255), pg.Color(204, 153, 255), pg.Color(163, 112, 214),
               pg.Color(102, 21, 153), pg.Color(51, 0, 102),
               pg.Color(random.randint(0,256), random.randint(0,256), random.randint(0,256)),
               pg.Color(random.randint(0,256), random.randint(0,256), random.randint(0,256)),
               pg.Color(random.randint(0,256), random.randint(0,256), random.randint(0,256)),
               pg.Color(random.randint(0,256), random.randint(0,256), random.randint(0,256)),
               pg.Color(random.randint(0,256), random.randint(0,256), random.randint(0,256)),
               pg.Color(random.randint(0,256), random.randint(0,256), random.randint(0,256))]

# block
block_location = [[102, 251, 401, 549], [202, 351, 501, 649]]
block_value = [[0, 0, 0, 0],
               [0, 0, 0, 0],
               [0, 0, 0, 0],
               [0, 0, 0, 0]]

# SCREEN
os.environ['SDL_VIDEO_WINDOW_POS'] = "{},{}".format(400, 50)
SCREEN = pg.display.set_mode((650, 750))


def block_make():
    blank = False
    for i in block_value:
        for j in i:
            if j == 0:
                blank = True
    if blank != True:
        print("Fail")
        pg.quit()
        sys.exit()
    a = random.randint(0, 3)
    b = random.randint(0, 3)

    while block_value[a][b] != 0:
        a = random.randint(0, 3)
        b = random.randint(0, 3)
    block_value[a][b] = random.choice([2, 2, 2, 4])


def block_draw(value, location):
    if value == 0:
        return
    block_surface = pg.Surface((130, 130))
    block_rect = block_surface.fill(COLOR_BLOCK[int(math.log(value, 2) - 1)])
    #block_rect = block_surface.fill(COLOR_BLOCK[6])
    block_rect.center = (block_location[0][location[0]], block_location[1][location[1]])
    if value < 99:
        block_text_surface = block_font1.render("%d" % value, True, COLOR_BLACK)
    elif value < 9999:
        block_text_surface = block_font2.render("%d" % value, True, COLOR_BLACK)
    else:
        block_text_surface = block_font3.render("%d" % value, True, COLOR_BLACK)
    block_text_rect = block_text_surface.get_rect()
    block_text_rect.center = (block_location[0][location[0]], block_location[1][location[1]])

    SCREEN.blit(block_surface, block_rect)
    SCREEN.blit(block_text_surface, block_text_rect)


def block_down():
    for i in range(4):
        a = [0]
        for j in range(4):
            if block_value[j][i] != 0:
                a.append(block_value[j][i])
                block_value[j][i] = 0
        a.reverse()
        j = 0
        while j < len(a) - 1:
            if a[j] == a[j + 1]:
                a[j + 1] = 0
                a[j] = a[j] * 2
                j += 1
            j += 1
        k = 0
        for j in range(len(a) - 1):
            if a[j] != 0:
                block_value[3 - k][i] = a[j]
                k += 1

def block_up():
    for i in range(4):
        a = []
        for j in range(4):
            if block_value[j][i] != 0:
                a.append(block_value[j][i])
                block_value[j][i] = 0
        a.append(0)
        j = 0
        while j < len(a) - 1:
            if a[j] == a[j + 1]:
                a[j + 1] = 0
                a[j] = a[j] * 2
                j += 1
            j += 1
        k = 0
        for j in range(len(a) - 1):
            if a[j] != 0:
                block_value[k][i] = a[j]
                k += 1


def block_left():
    for i in block_value:
        a = []
        for j in range(4):
            if i[j] != 0:
                a.append(i[j])
                i[j] = 0
        a.append(0)
        j = 0
        while j < len(a) - 1:
            if a[j] == a[j + 1]:
                a[j + 1] = 0
                a[j] = a[j] * 2
                j += 1
            j += 1
        k = 0
        for j in range(len(a) - 1):
            if a[j] != 0:
                i[k] = a[j]
                k += 1


def block_right():
    for i in block_value:
        a = [0]
        for j in range(4):
            if i[j] != 0:
                a.append(i[j])
                i[j] = 0
        a.reverse()
        j = 0
        while j < len(a) - 1:
            if a[j] == a[j + 1]:
                a[j + 1] = 0
                a[j] = a[j] * 2
                j += 1
            j += 1
        k = 0
        for j in range(len(a) - 1):
            if a[j] != 0:
                i[3 - k] = a[j]
                k += 1

# surface, rect
title_text_surface = title_font.render("2048", True, COLOR_WHITE)
title_text_rect = title_text_surface.get_rect()
title_text_rect.center = (100, 50)

# loop
start = True
while True:
    if start:
        block_make()
        start = False

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

        if event.type == pg.KEYDOWN:
            if pg.key.get_pressed()[pg.K_DOWN]:
                block_down()
                block_make()
            if pg.key.get_pressed()[pg.K_UP]:
                block_up()
                block_make()
            if pg.key.get_pressed()[pg.K_LEFT]:
                block_left()
                block_make()
            if pg.key.get_pressed()[pg.K_RIGHT]:
                block_right()
                block_make()

    SCREEN.fill(COLOR_BLACK)

    for i in range(1, 4):
        pg.draw.line(SCREEN, (100, 100, 100), [25 + 150 * i, 125], [25 + 150 * i, 725], 5)
        pg.draw.line(SCREEN, (100, 100, 100), [25, 125 + 150 * i], [625, 125 + 150 * i], 5)
    pg.draw.rect(SCREEN, COLOR_WHITE, [25, 125, 600, 600], 10)

    SCREEN.blit(title_text_surface, title_text_rect)

    y = 0
    for i in block_value:
        x = 0
        for j in i:
            block_draw(j, [x, y])
            x += 1
        y += 1

    pg.display.flip()

    clock.tick(30)