import pygame, random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", center=self.position, radius=self.radius, width=2)
    
    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        if self.radius > ASTEROID_MIN_RADIUS:
            rand_angle = random.uniform(20, 50)
            rand_angle_a = self.velocity.rotate(rand_angle)
            rand_angle_b = self.velocity.rotate(-rand_angle)
            new_asteroid_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid_a = Asteroid(self.position.x, self.position.y, new_asteroid_radius)
            asteroid_b = Asteroid(self.position.x, self.position.y, new_asteroid_radius)
            asteroid_a.velocity = rand_angle_a * 1.2
            asteroid_b.velocity = rand_angle_b * 1.2
        self.kill()