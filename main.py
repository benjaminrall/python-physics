import pygame, math
from pygame.locals import *
from ball import Ball

# Constants
SCALE_FACTOR = 30

SCREEN_WIDTH = 36 * SCALE_FACTOR
SCREEN_HEIGHT = 28 * SCALE_FACTOR

FRAMERATE = 120

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('PE_TEST')
pygame.init()

clock = pygame.time.Clock()

# Variables
force = 1000
pos = (100, 100)

# Objects
balls = []


def getVelocity(pos, magnitude, mouse_pos, display):
    dx = mouse_pos[0] - pos[0]
    dy = (display.get_size()[1] - mouse_pos[1]) - pos[1]
    dist = math.hypot(dx, dy)
    return (magnitude * (dx / dist)), (magnitude * (dy / dist))


if __name__ == '__main__':
    while True:
        clock.tick(FRAMERATE)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    pass
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    ball = Ball(1, 20, pos, SCREEN)
                    ball.addForceDirection(force, mouse_pos)
                    balls.append(ball)
                elif event.button == 4 and force < 2000:
                    force += 50
                elif event.button == 5 and force > 0:
                    force -= 50

        SCREEN.fill((30, 160, 235))
        for ball in balls:
            ball.simulate()
            ball.draw(SCREEN)

        v = getVelocity(pos, force, pygame.mouse.get_pos(), SCREEN)
        pygame.draw.circle(SCREEN, (0,0,0), (int(v[1]/9.8) + pos[0], SCREEN.get_size()[1] - pos[1]), 10)

        pygame.display.update()
