from math import *

def setup():
    size(720, 720)
    frameRate(120)

def draw():
    background(0)
    
    a = frameCount * (pi / 240)
    
    def x(p):
        return sin(a + p) * 255
    
    def y(p):
        return cos(a + p) * 255
    
    for i in range(0, 10):
        j = i / (pi * 4)
        stroke(255, x(j), y(j))
        line(360 + x(j), 360 + x(j), 360 - y(j), 360 + y(j))