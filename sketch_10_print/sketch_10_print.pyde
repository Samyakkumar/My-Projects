startX = 0
startY = 0
slashHeight = 30
import random
def setup():
    size(600, 600)
    background(51)

def draw():
    stroke(255)
    if random.uniform(0, 1) < 0.5:
        leftSlash(startX, startY)
    else:
        rightSlash(startX, startY)

def leftSlash(x, y):
    global startX, startY, slashHeight
    startX += slashHeight
    if startX >= width:
        startX = 0
        startY += slashHeight
    line(x, y, x + slashHeight, y + slashHeight)

def rightSlash(x, y):
    global startX, startY, slashHeight
    startX += 10
    if (startX >= width):
        startX = 0
        startY += slashHeight
    line(x, y + slashHeight, x + slashHeight, y)