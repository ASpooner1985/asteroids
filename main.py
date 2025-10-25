import pygame
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("green")
        pygame.display.flip()
        clock = pygame.time.Clock()
        dt = 0
        returnTime = clock.tick(3600)
        dt = returnTime / 1000
        


if __name__ == "__main__":
    main()


