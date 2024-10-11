#this allows us to use code from the
#open-source pygame library throughout this file
import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for sprite in updatable:
            sprite.update(dt)

        for sprite in asteroids:
            if sprite.is_colliding(player):
                print("Game over!")
                sys.exit()

        screen.fill((0,0,0))
        
        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip()

        # limits the framerate to 60 frames per second
        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()