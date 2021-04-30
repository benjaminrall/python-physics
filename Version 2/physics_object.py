from rigibody import Rigidbody
from vector import Vector

class Object:
    def __init__(self, pos, mass, colour, collider = None, active = True):
        self.pos = Vector(pos[0], pos[1])
        self.rotation = 0
        self.mass = mass
        self.colour = colour
        self.collider = collider
        self.active = active
        self.rb = Rigidbody(self, mass, collider)

    def update(self):
        self.pos = self.rb.UpdatePosition()
        self.rotation = self.rb.UpdateRotation()

class Box(Object):
    def __init__(self, pos, dimensions, mass, colour, collider = None, active = True):
        super().__init__(pos, mass, colour, collider, active)
        self.dimensions = dimensions

    def draw(self, cam):
        cam.DrawRect((self.pos.x, self.pos.y, self.dimensions[0], self.dimensions[1]), self.colour)
    
    