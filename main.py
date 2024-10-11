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

        # Call update on all sprites
        for sprite in updatable:
            sprite.update(dt)

        # Check for collisions between asteroids and player
        for sprite in asteroids:
            if sprite.is_colliding(player):
                print("Game over!")
                sys.exit()

        # Check collision between asteroids and bullets
        for asteroid in asteroids:
            for bullet in shots:
                if bullet.is_colliding(asteroid):
                    asteroid.split()
                    bullet.kill()

        # Fill in Background Colour
        screen.fill((0,0,0))
        
        # call draw on all sprites drawable
        for sprite in drawable:
            sprite.draw(screen)

        # Change the screen to show new drawables
        pygame.display.flip()

        # limits the framerate to 60 frames per second
        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()