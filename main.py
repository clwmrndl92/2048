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

#key
Key_up = False
Key_down = False
Key_right = False
Key_left = False


class Block(pg.sprite.Sprite):
    block_location = [[102, 251, 401, 549], [202, 351, 501, 649]]
    
    def __init__(self, value, location):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((130, 130))
        self.value = value
        block_value[location[1]][location[0]] = self.value
        self.locationx = location[0]
        self.locationy = location[1]
        #self.rect = self.surface.fill(COLOR_BLOCK[int(math.log(self.value, 2) - 1)])
        self.rect = self.image.fill(COLOR_WHITE)
        self.rect.center = (block_location[0][location[0]], block_location[1][location[1]])
        self.mask = pg.mask.from_surface(self.image)

    #def update(self):

#group
block_Group = pg.sprite.Group()

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
    block_Group.add(Block(random.choice([2, 2, 2, 2, 4]), [a,b]))


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
                block_make()
            '''if pg.key.get_pressed()[pg.K_UP]:
            if pg.key.get_pressed()[pg.K_LEFT]:
            if pg.key.get_pressed()[pg.K_RIGHT]:'''

    SCREEN.fill(COLOR_BLACK)

    for i in range(1, 4):
        pg.draw.line(SCREEN, (100, 100, 100), [25 + 150 * i, 125], [25 + 150 * i, 725], 5)
        pg.draw.line(SCREEN, (100, 100, 100), [25, 125 + 150 * i], [625, 125 + 150 * i], 5)
    pg.draw.rect(SCREEN, COLOR_WHITE, [25, 125, 600, 600], 10)

    SCREEN.blit(title_text_surface, title_text_rect)

    block_Group.draw(SCREEN)

    pg.display.flip()

    clock.tick(30)