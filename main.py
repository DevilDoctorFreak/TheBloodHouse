import pygame
from menu import menu

fps = 15

if __name__ == '__main__':
    pygame.init()

    screen = pygame.display.set_mode((750, 450))
    pygame.display.set_caption('TheBloodHouse')
    screen.fill((0, 0, 0))
    menu()
    pygame.quit()
