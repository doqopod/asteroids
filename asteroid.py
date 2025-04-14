import pygame
from circleshape import CircleShape
from constants import *
import random

class Asteroid (CircleShape):
  
  def __init__(self, x, y, radius):
    super().__init__(x, y, radius)

  def draw(self, screen):
    pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius)
  
  def update(self, dt):
    self.position += self.velocity*dt

  def split(self):
    self.kill()
    if self.radius <= ASTEROID_MIN_RADIUS:
      return
    rotation = random.uniform(20, 50)
    new1 = self.velocity.rotate(rotation) * 1.2
    new2 = self.velocity.rotate(-rotation) * 1.2
    new_radius = self.radius - ASTEROID_MIN_RADIUS
    asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
    asteroid1.velocity = new1
    asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
    asteroid2.velocity = new2
