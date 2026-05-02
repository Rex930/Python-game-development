import pgzrun
from random import randint

WIDTH = 400
HEIGHT = 400

r = randint(120,255)
g = randint(120,255)
b = randint(120,255)
center = (200,200)

def draw():
    screen.fill((r,g,b))
    radius=20
    for i in range(15):
        screen.draw.circle(center,radius,(r,g,b))
        radius +=10

def on_mouse_down():
    global r, g, b
    r = randint(120,255)
    g = randint(120,255)
    b = randint(120,255)
        