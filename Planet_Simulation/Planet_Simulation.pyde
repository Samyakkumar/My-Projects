from CelestialBody import CelestialBody, Sun
mySun = ''
myCelestialBodies = []

def setup():
    size(600, 600)
    global mySun, myCelestialBodies
    mySun = Sun(PVector(width//2, height//2), 100, 10000)
    rad = 120
    for i in range(4):
        myCelestialBodies.append(CelestialBody(PVector(width//2 - 100, height//2), rad, random(5, 10), 1, 20))
        rad += 40
def draw():
    background(0)
    global mySun, myCelestialBodies
    mySun.show()
    for body in myCelestialBodies:
        body.show()
        body.move(mySun)