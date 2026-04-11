import pgzrun

WIDTH = 600
HEIGHT = 400

def draw_cloud(x,y):
    screen.draw.filled_circle((x,y),20,(225,255,255))
    screen.draw.filled_circle((x+22,y-10),22,(225,255,255))
    screen.draw.filled_circle((x+45,y),18,(225,255,255))
def draw():
        screen.clear()
        screen.fill((135,206,235))

        screen.draw.filled_circle((500,80),40,(255,232,20))
        draw_cloud(80,80)
        draw_cloud(220,60)
        draw_cloud(350,90)

pgzrun.go()