import pgzrun
from random import randint

WIDTH = 600
HEIGHT = 400

score = 0
gameOver = False

ash = Actor("ash")
ash.pos = 100, 100

pikachu = Actor("pikachu")
pikachu.pos = 200, 200

def draw():
    screen.blit("thunder", (0, 0))
    pikachu.draw()
    ash.draw()

    screen.draw.text("Score: " + str(score),
                     color="black",
                     topleft=(10, 10))
    if gameOver:
        screen.fill("lightblue")
        screen.draw.text("Time's Up! Your final score: " + str(score),
                         midtop=(WIDTH/2, 10),
                         fontsize=40,
                         color="darkblue")

def place_pikachu():
    pikachu.x = randint(100, 400)
    pikachu.y = randint(100, 400)


def timeUp():
    global gameOver
    gameOver = True


def update():
    global score
    if gameOver:
        return

    if keyboard.left:
        ash.x -= 3
    if keyboard.right:
        ash.x += 3
    if keyboard.up:
        ash.y -= 3
    if keyboard.down:
        ash.y += 3

    if ash.colliderect(pikachu):
        score += 10
        place_pikachu()

clock.schedule(timeUp, 30.0)
pgzrun.go()
