import pygame, math

class Ball():
    def __init__(self, mass, radius, pos, display, colour = (255, 255, 255)):
        self.mass = mass
        self.radius = radius
        self.colour = colour
        self.x = pos[0]
        self.y = pos[1]
        self.xVelocity = 0
        self.yVelocity = 0
        self.forceVectors = []
        self.display = display

    def simulate(self):
        ax = 0
        ay = -9.8
        for vector in self.forceVectors:
            ax += vector[0] / self.mass
            ay += vector[1] / self.mass
        self.forceVectors = []
        self.xVelocity += ax / 120
        self.yVelocity += ay / 120
        self.x += self.xVelocity
        self.y += self.yVelocity

    def addForceVector(self, force):
        self.forceVectors.append(force)

    def addForceDirection(self, magnitude, mouse_pos):
        dx = mouse_pos[0] - self.x
        dy = (self.display.get_size()[1] - mouse_pos[1]) - self.y
        dist = math.hypot(dx, dy)
        self.forceVectors.append(((magnitude * (dx / dist)), (magnitude * (dy / dist))))

    def draw(self, win):
        pygame.draw.circle(win, self.colour, (int(self.x), int(self.display.get_size()[1] - self.y)), self.radius)
