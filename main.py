import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player
def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0 # delta time(means change), time between frames
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        log_state()

        screen.fill("black")

        player.draw(screen)
        
        pygame.display.flip()
        milliseconds = clock.tick(60) # 60 frames per second

        dt = milliseconds / 1000

    
    

    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


    


if __name__ == "__main__":
    main()
