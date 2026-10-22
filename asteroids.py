import pygame
import random

from logger import log_event
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "brown", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += dt*self.velocity

    def split(self):
        self.kill()
        if self.radius == ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        angle = random.uniform(20, 50)
        new_direction1 = self.velocity.rotate(angle)
        new_direction2 = -self.velocity.rotate(angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = new_direction1 * 1.2
        asteroid2.velocity = new_direction2 * 1.2
