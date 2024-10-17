import pygame
from circleshape import CircleShape
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y, direction):
        # initialize the Asteroid using the parent class CircleShape.
        super().__init__(x, y, SHOT_RADIUS)
        self.__width = 2
        self.velocity = direction * PLAYER_SHOOT_SPEED

    def draw(self, screen):
        # Draw the asteroid on the screen
        pygame.draw.circle(screen, (255, 255, 255), (int(self.position.x), int(self.position.y)), SHOT_RADIUS, self.__width)

    def update(self, dt):
        self.position += self.velocity * dt
