from circleshape import CircleShape
import pygame

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        # initialize the Asteroid using the parent class CircleShape.
        super().__init__(x, y, radius)
        self.__width = 2
        self.velocity = pygame.Vector2(1, 0)  # Default velocity

    def draw(self, screen):
        # Draw the asteroid on the screen
        pygame.draw.circle(screen, (255, 255, 255), (int(self.position.x), int(self.position.y)), self.radius, self.__width)

    def update(self, dt):
        # Update position based on velocity and dt
        self.position += (self.velocity * dt)
