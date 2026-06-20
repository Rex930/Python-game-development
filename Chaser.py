import pgzrun
from random import randint

WIDTH = 600
HEIGHT = 500

SCORE = 0
gameOver = False

bee = Actor("bee")
bee.pos = 100, 100

flower= Actor("flower") 
flower.pos = 200, 200

def draw():
    screen.blit("bg", (0, 0))
    flower.draw()
    bee.draw()

    screen.draw.text("Score: " + str(SCORE),color = "black", topleft = (10, 10))
    
    if gameOver:
                screen.fill("pink")
                screen.draw.text("Time's Up! Your final score: " + str(SCORE),
                                                 midtop=(WIDTH/2, 10),
                                                 fontsize=40,
                                                 color="red")
def place_flower():
    flower.x = (randint(70, (WIDTH-70)))
    flower.y = (randint(70, (HEIGHT-70)))

def  timeUp():
    global gameOver
    gameOver = True

def update():
    global SCORE

    if keyboard.left:
        bee.x = bee.x -2

    if keyboard.right:
        bee.x = bee.x + 2

    if keyboard.up:
        bee.y = bee.y - 2

    if keyboard.down:
        bee.y = bee.y + 2

    flowerCollected = bee.colliderect(flower)

    if flowerCollected:
        SCORE = SCORE + 10
        sounds.collect.play()
        place_flower()

clock.schedule(timeUp, 60.0)
pgzrun.go()
