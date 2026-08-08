import pgzrun
from random import randint

WIDTH = 400
HEIGHT = 200

score = 0
gameOver = False

snowman = Actor("snowman")
snowman.pos = 100, 100

present = Actor("present")
present.pos = 200, 200

def draw():
    screen.blit("snow", (0, 0))
    snowman.draw()
    present.draw()

    screen.draw.text("Score: " + str(score),
                     color="black",
                     topleft=(10, 10))
    if gameOver:
        screen.fill("lightblue")
        screen.draw.text("Time's Up! Your final score: " + str(score),
                         midtop=(WIDTH/2, 10),
                         fontsize=40,
                         color="darkblue")

def place_present():
    present.x = randint(50, 350)
    present.y = randint(50, 150)


def timeUp():
    global gameOver
    gameOver = True


def update():
    global score
    if gameOver:
        return

    if keyboard.left:
        snowman.x -= 3
    if keyboard.right:
        snowman.x += 3
    if keyboard.up:
        snowman.y -= 3
    if keyboard.down:
        snowman.y += 3

    if snowman.colliderect(present):
        score += 10
        place_present()

clock.schedule(timeUp, 30.0)
pgzrun.go()
