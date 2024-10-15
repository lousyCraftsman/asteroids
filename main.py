from constants import *
from player import *
import pygame

def main():
    # Startup information
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Used to calculate delta time
    clock = pygame.time.Clock()
    dt = 0

    # Used to calculate player position
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    # Instantiate the Player object
    player = Player(x, y)

    # Game loop
    running = True
    while running:
        # This allows us to close the GUI window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear the screen, draw stuff, update display
        screen.fill((0,0,0)) # Fill GUI with black
        player.update(dt)
        player.draw(screen)
        pygame.display.flip()
        
        # Set framerate (60 fps)
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
