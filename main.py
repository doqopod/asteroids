import pygame 
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
  pygame.init()
  updatable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  asteroids = pygame.sprite.Group()
  shot = pygame.sprite.Group()
  AsteroidField.containers = (updatable)
  Player.containers = (updatable, drawable)
  Asteroid.containers = (updatable, drawable, asteroids)
  Shot.containers = (updatable, drawable, shot)
  clock = pygame.time.Clock()
  dt = 0
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
  asteroid_field = AsteroidField()
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return
    screen.fill((0, 0, 0))
    updatable.update(dt)
    for asteroid in asteroids:
      if player.collision(asteroid):
        print("Game over!")
        return
    for asteroid in asteroids:
      for bullet in shot:
        if bullet.collision(asteroid):
          bullet.kill()
          asteroid.split()
    for draw in drawable:
      draw.draw(screen)
    pygame.display.flip()
    dt = clock.tick(60) / 1000

if __name__ == "__main__":
  main()