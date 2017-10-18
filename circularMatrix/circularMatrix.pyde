import random as rs
import math
class WordString(object):
    def __init__(self, location, stringLength, col, radius, direc):
        self.location = location
        self.stringLength = stringLength
        self.startFrom = int(random(97, 122 - self.stringLength))
        self.alphaBetsToUse = [chr(i) for i in range(self.startFrom, self.startFrom + self.stringLength)]
        self.vel = PVector(0, map(radius, 50, width, 0.01, 0.05))
        self.startAngle = 0
        self.radius = radius
        self.col = col
        self.direc = direc
    
    def move(self):
        self.startAngle += self.vel.y * self.direc
    
    def show(self):
        pushMatrix()
        textSize(map(self.radius, 50, width, 2, 18))
        fill(self.col)
        pi = PI
        startAngle = self.startAngle
        perIncrement = 2 * pi / (self.stringLength)
        for alphabet in self.alphaBetsToUse:
            loc = PVector.fromAngle(startAngle).setMag(self.radius).add(self.location)
            text(alphabet, loc.x, loc.y)
            startAngle += perIncrement
        popMatrix()
            
            
    
    def isOffScreen(self):
        return self.location.y >= height
myWord = []
def setup():
    global myWord
    size(600, 600)
    startRadius = 10
    for i in range(100):
        direction = 1 if rs.uniform(0, 1) < 0.5 else -1
        myWord.append(WordString(PVector(width//2, height//2), 18, color(0, 255, 0), startRadius, direction))
        startRadius += 5
        
def draw():
    global myWord
    background(0)
    for word in myWord:
        word.show()
        word.move()
        
    