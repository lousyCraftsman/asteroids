import pygame
import random
from circleshape import CircleShape
from constants import *
import math

def generate_lumpy_shape(center, num_points, radius, lumpiness):
    points = []
    for i in range(num_points):
        angle = i * (2 * math.pi / num_points)  # Spread points equally around the center
        random_offset = random.uniform(-lumpiness, lumpiness)  # Random offset for lumpiness
        distance = radius + random_offset
        x = center[0] + math.cos(angle) * distance
        y = center[1] + math.sin(angle) * distance
        points.append((x, y))
    return points

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        # initialize the Asteroid using the parent class CircleShape.
        super().__init__(x, y, radius)
        self.__width = 2
        self.velocity = pygame.Vector2(1, 0)  # Default velocity
        self.shape = generate_lumpy_shape((0,0), 8, self.radius, 10)
    


    def draw(self, screen):
        # Draw the asteroid on the screen
        #pygame.draw.circle(screen, (255, 255, 255), (int(self.position.x), int(self.position.y)), self.radius, self.__width
        absolute_points = [(self.position.x + point[0], self.position.y + point[1]) for point in self.shape]
        pygame.draw.polygon(screen, (255, 255, 255), absolute_points, self.__width)

    def update(self, dt):
        # Update position based on velocity and dt
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        # randomize the angle of the split
        random_angle = random.uniform(20, 50)

        a = self.velocity.rotate(random_angle)
        b = self.velocity.rotate(-random_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = a * 1.2
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = b * 1.2