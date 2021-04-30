import pygame
import math
import random
import os
from physics_object import *
from camera import Camera

# Constants
WIN_WIDTH = 800
WIN_HEIGHT = 800
FRAMERATE = 120
ICON_IMG = pygame.image.load(os.path.join("imgs", "icon.png"))

# Pygame Setup
pygame.init()
win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Python Physics")
pygame.display.set_icon(ICON_IMG)
clock = pygame.time.Clock()

# Objects
cam = Camera(win, 0, 0, 1)
objects = []


# Variables
running = True

if __name__ == '__main__':
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    objects.append(Box((-50, -600), (100, 100), 10, (255, 255, 255)))
                    
        objects.append(Box((random.randrange(-400, 401), -400), (10, 10), 10, (255, 255, 255)))

        win.fill((30, 160, 235))
        for obj in objects:
            obj.draw(cam)
            obj.update()
        pygame.display.update()

        print(len(objects))

        clock.tick(FRAMERATE)