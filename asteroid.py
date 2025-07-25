from circleshape import CircleShape
import pygame
from constants import ASTEROID_MIN_RADIUS
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.position.x, self.position.y), self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        elif self.radius > ASTEROID_MIN_RADIUS:
            random_angle = random.uniform(20, 50)
            Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS).velocity = (self.velocity.rotate(random_angle) * 1.2)
            Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS).velocity = (self.velocity.rotate(-random_angle) * 1.2)