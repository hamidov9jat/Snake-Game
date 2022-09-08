# import turtle
import time
from food import Food
from turtle import Screen
from snake import Snake

screen = Screen()
screen.setup(600, 600)
# screen.screensize()
print(screen.canvwidth, screen.canvheight)
screen.bgcolor('green')
screen.title('Snake Game')
screen.tracer(0)

sn = Snake(screen)
fd = Food(screen)

screen.listen()
screen.onkey(key='Up', fun=sn.up)
screen.onkey(key='Down', fun=sn.down)
screen.onkey(key='Left', fun=sn.left)
screen.onkey(key='Right', fun=sn.right)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    sn.move()

screen.exitonclick()


# screen.bye()
# turtle.done()
