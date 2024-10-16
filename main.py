from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *
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
    
    # Add the groups
    shots = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    # Assign containers to the Asteroid class
    Asteroid.containers = (asteroids, updatable, drawable)

    # Assign containers to the Shot class
    Shot.containers = (shots, updatable, drawable)

    # Assign container to the AsteroidField class
    AsteroidField.containers = (updatable,)  # tuple
    
    # Add the player to the groups
    updatable.add(player)
    drawable.add(player)

    # Create the AsteroidField
    asteroid_field = AsteroidField()

    # Debug print statements
    print(f"Updatable group has {len(updatable)} sprites")
    print(f"Drawable group has {len(drawable)} sprites")

    # Game loop
    running = True
    while running:
        # This allows us to close the GUI window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear the screen
        screen.fill((0,0,0)) # Fill GUI with black

        # Update all sprites
        for sprite in updatable:
            if sprite == player:
                new_shot = sprite.update(dt)
                if new_shot:
                    shots.add(new_shot)
                    updatable.add(new_shot)
                    drawable.add(new_shot)
            else: 
                sprite.update(dt)

        for asteroid in asteroids:
            if player.collision(asteroid):
                print ("Game over!")
                running = False
    
        # Draw all sprites
        for sprite in drawable:
            sprite.draw(screen)

        # Update display
        pygame.display.flip()

        # Set framerate (60 fps)
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
