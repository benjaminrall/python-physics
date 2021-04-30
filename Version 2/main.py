import pygame
import random
import os
from physics_object import *
from camera import Camera

# Constants
WIN_WIDTH = 1920
WIN_HEIGHT = 1080
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
                    
        objects.append(Box((random.randrange(-960, 961), -540), (random.randrange(5,151), random.randrange(5,151)), 10, (random.randrange(1,256), random.randrange(1,256), random.randrange(1,256))))

        win.fill((0, 0, 0))
        for obj in objects:
            obj.update()
            if not obj.draw(cam):
                objects.remove(obj)
                del(obj)
        pygame.display.update()

        print(len(objects))

        clock.tick(FRAMERATE)