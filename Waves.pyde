from math import *

def setup():
    size(900, 540)
    frameRate(30)
    colorMode(RGB, 720)

def draw():
    background(0)
    
    x = frameCount
    y = (sin(x * 2 * pi / 90) + 1) * 360
    
    for i in range(0, 720):
        stroke(y, i, x)
        point(i + 90, 270 + sin(i * mouseX / 60) * 90)