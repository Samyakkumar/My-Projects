import random as rs
class CelestialBody(object):
    def __init__(self, location, radius, velocity, mass, sizeBody):
        self.radius = radius
        self.location = location
        self.velocity = velocity
        self.mass = mass
        self.startAngle = 0
        self.incrementMy = 2*PI/random(100, 200)
        self.incrementMy *= -1 if rs.uniform(0, 1) < 0.5 else 1
        self.sizeBody = sizeBody
    
    def show(self):
        pushMatrix()
        translate(width//2, height//2)
        fill(51)
        noStroke()
        ellipse(self.location.x, self.location.y, self.sizeBody, self.sizeBody)
        popMatrix()
    
    def move(self, sun):
        newPos = PVector.fromAngle(self.startAngle).setMag(self.radius)
        self.location = newPos
        self.startAngle += self.incrementMy
        
        



class Sun(CelestialBody):
    def __init__(self, location, radius, mass):
        self.location = location
        self.radius = radius
        self.mass = mass
    
    def show(self):
        pushMatrix()
        fill(51)
        noStroke()
        ellipse(self.location.x, self.location.y, self.radius, self.radius)
        popMatrix()
    