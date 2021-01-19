import pygame
from load_img import load_image
import locations as loc


def menu():
    screen = pygame.display.set_mode((750, 450))
    menu_image = load_image('menu.png')
    screen.blit(menu_image, (0, 0))
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if (event.pos[0] > 263) and event.pos[0] < 466:
                    if (event.pos[1] > 121) and event.pos[1] < 191:
                        loc.garden_loc()
                    elif (event.pos[1] > 224) and event.pos[1] < 296:
                        exit()
        pygame.display.flip()

    pygame.quit()
