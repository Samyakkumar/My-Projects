import random as rs
class WordString(object):
    def __init__(self, location, stringLength, col):
        self.location = location
        self.stringLength = stringLength
        self.startFrom = int(random(97, 122 - self.stringLength))
        self.alphaBetsToUse = [chr(i) for i in range(self.startFrom, self.startFrom + self.stringLength)]
        self.vel = PVector(0, random(2, 7))
        self.col = col
    
    def move(self):
        self.location.add(self.vel)
    
    def show(self):
        pushMatrix()
        
        tSize = map(self.vel.y, 2, 7, 9, 16)
        textSize(tSize)
        startPoint = self.location.y
        for i in range(len(self.alphaBetsToUse)):
            if i != len(self.alphaBetsToUse):
                fill(self.col)
            else:
                fill(255)
            alphabet = self.alphaBetsToUse[i]
            if rs.uniform(0, 1) < 0.1:
                self.alphaBetsToUse[i] = chr(rs.randint(self.startFrom, 128))
            text((alphabet), self.location.x, startPoint)
            startPoint += map(tSize,5, 16, 6, 11)
        popMatrix()
    
    def isOffScreen(self):
        return self.location.y >= height

myWord = []
def setup():
    global myWord
    for i in range(100):
        myWord.append(WordString(PVector(random(width), random(-450, -50)), 15, color(0, 255, 0)))
    fullScreen()
    # size(600,600)

def draw():
    global myWord
    background(0)
    for ws in myWord:
        ws.show()
        ws.move()
        if ws.isOffScreen():
            myWord.remove(ws)
            myWord.append(WordString(PVector(random(width), random(-200, -150)), 15, color(random(255), random(255), random(255))))
    