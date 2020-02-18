from math import *

def setup():
    size(720, 720)
    frameRate(5)
    background(0)

def draw():
    
    a = 360
    b = 360
    c = 360
    d = 360

    for i in range(0, 255):
        n = random(0, 4)
        r = int(n)
        
        if r == 0:
            c = a + 10
        if r == 1:
            d = b - 10
        if r == 2:
            c = a - 10
        if r == 3:
            d = b + 10
            
        if c == 720:
            c -= 10
        if d == 720:
            d -= 10
        if c == 0:
            c += 10
        if d == 0:
            d += 10
            
        stroke(255 - i)
        line(a, b, c, d)
        
        a = c
        b = d
    