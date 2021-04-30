from vector import Vector

class Rigidbody:

    gravity = 9.8 / 120

    def __init__(self, obj, mass, collider):
        self.mass = mass
        self.velocity = Vector(0, 0)
        self.acceleration = Vector(0, self.gravity)
        self.rotationalVelocity = 0
        self.rotationAcceleration = 0
        self.maxRotationalVelocity = 7
        self.position = obj.pos
        self.rotation = obj.rotation
        self.centreOfMass = ()
        self.collider = collider

    def AddForce(self):
        pass

    def AddForceAtPosition(self):
        pass

    def AddRotationalForce(self):
        pass

    def UpdatePosition(self):
        self.velocity = Vector.Add(self.velocity, self.acceleration)
        self.position = Vector.Add(self.position, self.velocity)
        return self.position

    def UpdateRotation(self):
        self.rotationalVelocity = min(self.rotationalVelocity + self.rotationAcceleration, self.maxRotationalVelocity)
        self.rotation += self.rotationalVelocity
        return self.rotation