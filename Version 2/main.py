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
                    pass

        win.fill((0, 0, 0))
        for obj in objects:
            obj.draw(cam)
            obj.update()
        pygame.display.update()

        print(len(objects))

        clock.tick(FRAMERATE)