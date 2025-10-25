import pygame
from constants import *
from player import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    newPlayer = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("green")
        newPlayer.draw(screen)
        pygame.display.flip()

        returnTime = clock.tick(60)
        dt = returnTime / 1000
        


if __name__ == "__main__":
    main()


