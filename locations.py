import pygame
from load_img import load_image
from moving import move_char

gard_border = [(0, 0, 750, 93), (0, 370, 750, 450),
               (0, 0, 20, 370), (695, 93, 750, 450),
               (59, 76, 120, 132), (349, 204, 408, 256),
               (409, 234, 477, 332), (574, 235, 680, 346),
               (663, 90, 750, 155)]

din_border = [(0, 0, 157, 447), (0, 0, 597, 69),
              (0, 407, 750, 450), (576, 0, 750, 450),
              (153, 106, 222, 154), (154, 55, 252, 122),
              (483, 51, 598, 112), (576, 0, 750, 450),
              (308, 145, 421, 345), (181, 209, 262, 334),
              (260, 237, 277, 300), (420, 174, 440, 310)]

hall_border = [(0, 0, 83, 450), (0, 0, 750, 159),
               (0, 375, 83, 450), (650, 0, 750, 450),
               (304, 134, 337, 184), (400, 134, 433, 187),
               (82, 157, 129, 240), (608, 154, 673, 241)]

kit_border = [(0, 0, 157, 450), (0, 0, 750, 90),
              (0, 409, 750, 450), (564, 0, 750, 450),
              (158, 305, 434, 365), (192, 104, 267, 154),
              (267, 31, 429, 128), (465, 66, 561, 163),
              (543, 127, 596, 203)]

under_border = [(0, 0, 168, 450), (0, 0, 750, 102),
                (0, 169, 750, 450), (558, 0, 750, 450),
                (167, 63, 316, 150), (168, 388, 203, 442)]

bed_border = [(0, 0, 80, 450), (0, 0, 750, 102),
              (0, 416, 750, 450), (635, 0, 750, 450),
              (81, 67, 197, 126), (508, 64, 672, 140),
              (549, 142, 670, 161), (179, 315, 267, 386),
              (462, 320, 548, 383), (166, 169, 531, 239),
              (215, 210, 482, 290)]

click = []

fps = 10
clock = pygame.time.Clock()

screen = pygame.display.set_mode((750, 450))

main_sprites1 = pygame.sprite.Group()
main_sprites2 = pygame.sprite.Group()
main_sprites3 = pygame.sprite.Group()
main_sprites4 = pygame.sprite.Group()

all_sprites = pygame.sprite.Group()
sprite = pygame.sprite.Sprite()
sprite.image = load_image("policeman1.png", -1)
sprite.rect = sprite.image.get_rect()
all_sprites.add(sprite)

sprites1 = pygame.sprite.Group()
sprite1 = pygame.sprite.Sprite()
sprite1.image = load_image("standart.png", -1)
sprite1.rect = sprite1.image.get_rect()
sprites1.add(sprite1)


class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, sheet, columns, rows, x, y, n):
        if n == 1:
            super().__init__(main_sprites1)
        elif n == 2:
            super().__init__(main_sprites2)
        elif n == 3:
            super().__init__(main_sprites3)
        elif n == 4:
            super().__init__(main_sprites4)

        self.frames = []
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns, sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(frame_location, self.rect.size)))

    def update(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]


main_char1 = AnimatedSprite(load_image('mainc1.png', -1), 3, 1, 52, 104, 1)
main_char2 = AnimatedSprite(load_image('mainc2.png', -1), 3, 1, 46, 104, 2)
main_char3 = AnimatedSprite(load_image('mainc3.png', -1), 3, 1, 46, 104, 3)
main_char4 = AnimatedSprite(load_image('mainc4.png', -1), 3, 1, 52, 104, 4)

main_char1.rect = main_char1.image.get_rect()
main_char2.rect = main_char2.image.get_rect()
main_char3.rect = main_char3.image.get_rect()
main_char4.rect = main_char4.image.get_rect()


def kitchen():
    image = load_image('Map3.png')
    image = pygame.transform.scale(image, (450, 450))
    screen.blit(image, (150, 0))
    sprite.rect.x = 478
    sprite.rect.y = 153

    x1, x, sprite1.rect.x, main_char1.rect.x, main_char2.rect.x, \
        main_char3.rect.x, main_char4.rect.x = 513, 513, 513, 513, 513, 513, 513
    y1, y, sprite1.rect.y, main_char1.rect.y, main_char2.rect.y, \
        main_char3.rect.y, main_char4.rect.y = 257, 257, 257, 257, 257, 257, 257

    click.clear()
    click.append(sprite.rect.x)
    click.append(sprite.rect.y)

    sprites1.draw(screen)
    all_sprites.draw(screen)
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                click.clear()
                click.append(event.pos[0])
                click.append(event.pos[1])

        screen.fill((0, 0, 0))
        screen.blit(image, (150, 0))
        all_sprites.draw(screen)
        x, y, side = move_char(x, y, click, kit_border)
        if side == 'влево':

            sprite1.rect.x, main_char1.rect.x, main_char2.rect.x, \
                main_char3.rect.x, main_char4.rect.x = x, x, x, x, x
            sprite1.rect.y, main_char1.rect.y, main_char2.rect.y, \
                main_char3.rect.y, main_char4.rect.y = y, y, y, y, y

            main_sprites3.draw(screen)
            main_sprites3.update()
        elif side == 'вправо':
            sprite1.rect.x, main_char1.rect.x, main_char2.rect.x, \
                main_char3.rect.x, main_char4.rect.x = x, x, x, x, x
            sprite1.rect.y, main_char1.rect.y, main_char2.rect.y, \
                main_char3.rect.y, main_char4.rect.y = y, y, y, y, y

            main_sprites2.draw(screen)
            main_sprites2.update()

        elif side == 'вверх':
            sprite1.rect.x, main_char1.rect.x, main_char2.rect.x, \
                main_char3.rect.x, main_char4.rect.x = x, x, x, x, x
            sprite1.rect.y, main_char1.rect.y, main_char2.rect.y, \
                main_char3.rect.y, main_char4.rect.y = y, y, y, y, y

            main_sprites4.draw(screen)
            main_sprites4.update()

        elif side == 'вниз':
            sprite1.rect.x, main_char1.rect.x, main_char2.rect.x, \
                main_char3.rect.x, main_char4.rect.x = x, x, x, x, x
            sprite1.rect.y, main_char1.rect.y, main_char2.rect.y, \
                main_char3.rect.y, main_char4.rect.y = y, y, y, y, y

            main_sprites1.draw(screen)
            main_sprites1.update()

        elif x1 == x and y1 == y:
            sprites1.draw(screen)

        if (x >= 552) and x <= 593:
            if (y >= 259) and y <= 328:
                dinner()
        elif (x >= 170) and x <= 206:
            if (y >= 110) and y <= 186:
                underground()

        x1, y1 = x, y
        clock.tick(fps)
        pygame.display.flip()

    exit()


def hall():
    image = load_image('Map6.png')
    screen.blit(image, (75, 60))
    sprite.rect.x = 478
    sprite.rect.y = 153

    x1, x, sprite1.rect.x, main_char1.rect.x, main_char2.rect.x, \
        main_char3.rect.x, main_char4.rect.x = 142, 142, 142, 142, 142, 142, 142
    y1, y, sprite1.rect.y, main_char1.rect.y, main_char2.rect.y, \
        main_char3.rect.y, main_char4.rect.y = 273, 273, 273, 273, 273, 273, 273

    click.clear()
    click.append(sprite.rect.x)
    click.append(sprite.rect.y)

    sprites1.draw(screen)
    all_sprites.draw(screen)
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:

                click.clear()
                click.append(event.pos[0])
                click.append(event.pos[1])

        screen.fill((0, 0, 0))
        screen.blit(image, (75, 60))
        all_sprites.draw(screen)
        x, y, side = move_char(x, y, click, hall_border)
        if side == 'влево':

            sprite1.rect.x, main_char1.rect.x, main_char2.rect.x, \
                main_char3.rect.x, main_char4.rect.x = x, x, x, x, x
            sprite1.rect.y, main_char1.rect.y, main_char2.rect.y, \
                main_char3.rect.y, main_char4.rect.y = y, y, y, y, y

            main_sprites3.draw(screen)
            main_sprites3.update()

        elif side == 'вправо':
            sprite1.rect.x, main_char1.rect.x, main_char2.rect.x, \
                main_char3.rect.x, main_char4.rect.x = x, x, x, x, x
            sprite1.rect.y, main_char1.rect.y, main_char2.rect.y, \
                main_char3.rect.y, main_char4.rect.y = y, y, y, y, y

            main_sprites2.draw(screen)
            main_sprites2.update()

        elif side == 'вверх':
            sprite1.rect.x, main_char1.rect.x, main_char2.rect.x, \
                main_char3.rect.x, main_char4.rect.x = x, x, x, x, x
            sprite1.rect.y, main_char1.rect.y, main_char2.rect.y, \
                main_char3.rect.y, main_char4.rect.y = y, y, y, y, y

            main_sprites4.draw(screen)
            main_sprites4.update()

        elif side == 'вниз':
            sprite1.rect.x, main_char1.rect.x, main_char2.rect.x, \
                main_char3.rect.x, main_char4.rect.x = x, x, x, x, x
            sprite1.rect.y, main_char1.rect.y, main_char2.rect.y, \
                main_char3.rect.y, main_char4.rect.y = y, y, y, y, y

            main_sprites1.draw(screen)
            main_sprites1.update()

        elif x1 == x and y1 == y:
            sprites1.draw(screen)

        if (x >= 354) and x <= 394:
            if (y >= 184) and y <= 203:
                bedroom()
        elif (x >= 83) and x <= 129:
            if (y >= 227) and y <= 250:
                dinner()
        elif (x >= 626) and x <= 673:
            if (y >= 225) and y <= 254:
                dinner()

        x1, y1 = x, y
        clock.tick(fps)
        pygame.display.flip()

    exit()


def dinner():
    image = load_image('Map2.png')
    image = pygame.transform.scale(image, (450, 450))
    screen.blit(image, (150, 0))

    sprite.rect.x = 548
    sprite.rect.y = 340

    x1, x, sprite1.rect.x, main_char1.rect.x, main_char2.rect.x, \
        main_char3.rect.x, main_char4.rect.x = 305, 305, 305, 305, 305, 305, 305
    y1, y, sprite1.rect.y, main_char1.rect.y, main_char2.rect.y, \
        main_char3.rect.y, main_char4.rect.y = 348, 348, 348, 348, 348, 348, 348

    click.clear()
    click.append(sprite.rect.x)
    click.append(sprite.rect.y)

    sprites1.draw(screen)
    all_sprites.draw(screen)
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:

                click.clear()
                click.append(event.pos[0])
                click.append(event.pos[1])

        screen.fill((0, 0, 0))
        screen.blit(image, (150, 0))
        all_sprites.draw(screen)
        x, y, side = move_char(x, y, click, din_border)
        if side == 'влево':

            sprite1.rect.x, main_char1.rect.x, main_char2.rect.x, \
                main_char3.rect.x, main_char4.rect.x = x, x, x, x, x
            sprite1.rect.y, main_char1.rect.y, main_char2.rect.y, \
                main_char3.rect.y, main_char4.rect.y = y, y, y, y, y

            main_sprites3.draw(screen)
            main_sprites3.update()

        elif side == 'вправо':
            sprite1.rect.x, main_char1.rect.x, main_char2.rect.x, \
                main_char3.rect.x, main_char4.rect.x = x, x, x, x, x
            sprite1.rect.y, main_char1.rect.y, main_char2.rect.y, \
                main_char3.rect.y, main_char4.rect.y = y, y, y, y, y

            main_sprites2.draw(screen)
            main_sprites2.update()

        elif side == 'вверх':
            sprite1.rect.x, main_char1.rect.x, main_char2.rect.x, \
                main_char3.rect.x, main_char4.rect.x = x, x, x, x, x
            sprite1.rect.y, main_char1.rect.y, main_char2.rect.y, \
                main_char3.rect.y, main_char4.rect.y = y, y, y, y, y

            main_sprites4.draw(screen)
            main_sprites4.update()

        elif side == 'вниз':
            sprite1.rect.x, main_char1.rect.x, main_char2.rect.x, \
                main_char3.rect.x, main_char4.rect.x = x, x, x, x, x
            sprite1.rect.y, main_char1.rect.y, main_char2.rect.y, \
                main_char3.rect.y, main_char4.rect.y = y, y, y, y, y

            main_sprites1.draw(screen)
            main_sprites1.update()

        elif x1 == x and y1 == y:
            sprites1.draw(screen)

        if (x >= 241) and x <= 260:
            if (y >= 105) and y <= 136:
                hall()
        elif (x >= 492) and x <= 510:
            if (y >= 105) and y <= 136:
                hall()
        elif (x >= 153) and x <= 168:
            if (y >= 322) and y <= 362:
                kitchen()
        elif (x >= 207) and x <= 250:
            if (y >= 388) and y <= 447:
                garden_loc()

        x1, y1 = x, y
        clock.tick(fps)
        pygame.display.flip()

    exit()


def garden_loc():
    image = load_image('Map1.png')
    screen.blit(image, (0, 0))

    sprite.rect.x = 244
    sprite.rect.y = 128
    x1, x, sprite1.rect.x, main_char1.rect.x, main_char2.rect.x, \
        main_char3.rect.x, main_char4.rect.x = 159, 159, 159, 159, 159, 159, 159
    y1, y, sprite1.rect.y, main_char1.rect.y, main_char2.rect.y, \
        main_char3.rect.y, main_char4.rect.y = 300, 300, 300, 300, 300, 300, 300

    click.clear()
    click.append(sprite.rect.x)
    click.append(sprite.rect.y)

    sprites1.draw(screen)
    all_sprites.draw(screen)
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                click.clear()
                click.append(event.pos[0])
                click.append(event.pos[1])

        screen.fill((0, 0, 0))
        screen.blit(image, (0, 0))
        all_sprites.draw(screen)
        x, y, side = move_char(x, y, click, gard_border)
        if side == 'влево':

            sprite1.rect.x, main_char1.rect.x, main_char2.rect.x, \
                main_char3.rect.x, main_char4.rect.x = x, x, x, x, x
            sprite1.rect.y, main_char1.rect.y, main_char2.rect.y, \
                main_char3.rect.y, main_char4.rect.y = y, y, y, y, y

            main_sprites3.draw(screen)
            main_sprites3.update()

        elif side == 'вправо':
            sprite1.rect.x, main_char1.rect.x, main_char2.rect.x, \
                main_char3.rect.x, main_char4.rect.x = x, x, x, x, x
            sprite1.rect.y, main_char1.rect.y, main_char2.rect.y, \
                main_char3.rect.y, main_char4.rect.y = y, y, y, y, y

            main_sprites2.draw(screen)
            main_sprites2.update()

        elif side == 'вверх':
            sprite1.rect.x, main_char1.rect.x, main_char2.rect.x, \
                main_char3.rect.x, main_char4.rect.x = x, x, x, x, x
            sprite1.rect.y, main_char1.rect.y, main_char2.rect.y, \
                main_char3.rect.y, main_char4.rect.y = y, y, y, y, y

            main_sprites4.draw(screen)
            main_sprites4.update()

        elif side == 'вниз':
            sprite1.rect.x, main_char1.rect.x, main_char2.rect.x, \
                main_char3.rect.x, main_char4.rect.x = x, x, x, x, x
            sprite1.rect.y, main_char1.rect.y, main_char2.rect.y, \
                main_char3.rect.y, main_char4.rect.y = y, y, y, y, y

            main_sprites1.draw(screen)
            main_sprites1.update()

        elif x1 == x and y1 == y:
            sprites1.draw(screen)

        if (x >= 145) and x <= 199:
            if (y >= 109) and y <= 126:
                dinner()

        x1, y1 = x, y
        clock.tick(fps)
        pygame.display.flip()

    exit()


def bedroom():
    image = load_image('Map5.png')
    screen.blit(image, (78, 0))

    sprite.rect.x = 244
    sprite.rect.y = 128

    x1, x, sprite1.rect.x, main_char1.rect.x, main_char2.rect.x, \
        main_char3.rect.x, main_char4.rect.x = 358, 358, 358, 358, 358, 358, 358
    y1, y, sprite1.rect.y, main_char1.rect.y, main_char2.rect.y, \
        main_char3.rect.y, main_char4.rect.y = 322, 322, 322, 322, 322, 322, 322

    click.clear()
    click.append(sprite.rect.x)
    click.append(sprite.rect.y)

    all_sprites.draw(screen)
    sprites1.draw(screen)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                click.clear()
                click.append(event.pos[0])
                click.append(event.pos[1])

        screen.fill((0, 0, 0))
        screen.blit(image, (78, 0))
        x, y, side = move_char(x, y, click, bed_border)
        if side == 'влево':

            sprite1.rect.x, main_char1.rect.x, main_char2.rect.x, \
                main_char3.rect.x, main_char4.rect.x = x, x, x, x, x
            sprite1.rect.y, main_char1.rect.y, main_char2.rect.y, \
                main_char3.rect.y, main_char4.rect.y = y, y, y, y, y

            main_sprites3.draw(screen)
            main_sprites3.update()
        elif side == 'вправо':
            sprite1.rect.x, main_char1.rect.x, main_char2.rect.x, \
                main_char3.rect.x, main_char4.rect.x = x, x, x, x, x
            sprite1.rect.y, main_char1.rect.y, main_char2.rect.y, \
                main_char3.rect.y, main_char4.rect.y = y, y, y, y, y

            main_sprites2.draw(screen)
            main_sprites2.update()

        elif side == 'вверх':
            sprite1.rect.x, main_char1.rect.x, main_char2.rect.x, \
                main_char3.rect.x, main_char4.rect.x = x, x, x, x, x
            sprite1.rect.y, main_char1.rect.y, main_char2.rect.y, \
                main_char3.rect.y, main_char4.rect.y = y, y, y, y, y

            main_sprites4.draw(screen)
            main_sprites4.update()

        elif side == 'вниз':
            sprite1.rect.x, main_char1.rect.x, main_char2.rect.x, \
                main_char3.rect.x, main_char4.rect.x = x, x, x, x, x
            sprite1.rect.y, main_char1.rect.y, main_char2.rect.y, \
                main_char3.rect.y, main_char4.rect.y = y, y, y, y, y

            main_sprites1.draw(screen)
            main_sprites1.update()

        elif x1 == x and y1 == y:
            sprites1.draw(screen)

        if (x >= 345) and x <= 400:
            if (y >= 379) and y <= 428:
                hall()

        x1, y1 = x, y
        clock.tick(fps)
        pygame.display.flip()

    exit()


def underground():
    image = load_image('Map4.png')
    image = pygame.transform.scale(image, (450, 450))
    screen.blit(image, (150, 0))
    x1, x, sprite1.rect.x, main_char1.rect.x, main_char2.rect.x, \
        main_char3.rect.x, main_char4.rect.x = 311, 311, 311, 311, 311, 311, 311
    y1, y, sprite1.rect.y, main_char1.rect.y, main_char2.rect.y, \
        main_char3.rect.y, main_char4.rect.y = 184, 184, 184, 184, 184, 184, 184

    click.clear()
    click.append(sprite.rect.x)
    click.append(sprite.rect.y)

    sprites1.draw(screen)
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print(event.pos)
                click.clear()
                click.append(event.pos[0])
                click.append(event.pos[1])

        screen.fill((0, 0, 0))
        screen.blit(image, (150, 0))
        x, y, side = move_char(x, y, click, under_border)
        if side == 'влево':

            sprite1.rect.x, main_char1.rect.x, main_char2.rect.x, \
                main_char3.rect.x, main_char4.rect.x = x, x, x, x, x
            sprite1.rect.y, main_char1.rect.y, main_char2.rect.y, \
                main_char3.rect.y, main_char4.rect.y = y, y, y, y, y

            main_sprites3.draw(screen)
            main_sprites3.update()
        elif side == 'вправо':
            sprite1.rect.x, main_char1.rect.x, main_char2.rect.x, \
                main_char3.rect.x, main_char4.rect.x = x, x, x, x, x
            sprite1.rect.y, main_char1.rect.y, main_char2.rect.y, \
                main_char3.rect.y, main_char4.rect.y = y, y, y, y, y

            main_sprites2.draw(screen)
            main_sprites2.update()

        elif side == 'вверх':
            sprite1.rect.x, main_char1.rect.x, main_char2.rect.x, \
                main_char3.rect.x, main_char4.rect.x = x, x, x, x, x
            sprite1.rect.y, main_char1.rect.y, main_char2.rect.y, \
                main_char3.rect.y, main_char4.rect.y = y, y, y, y, y

            main_sprites4.draw(screen)
            main_sprites4.update()

        elif side == 'вниз':
            sprite1.rect.x, main_char1.rect.x, main_char2.rect.x, \
                main_char3.rect.x, main_char4.rect.x = x, x, x, x, x
            sprite1.rect.y, main_char1.rect.y, main_char2.rect.y, \
                main_char3.rect.y, main_char4.rect.y = y, y, y, y, y

            main_sprites1.draw(screen)
            main_sprites1.update()

        elif x1 == x and y1 == y:
            sprites1.draw(screen)

        if (x >= 306) and x <= 334:
            if (y >= 121) and y <= 157:
                kitchen()

        x1, y1 = x, y
        clock.tick(fps)
        pygame.display.flip()

    exit()
