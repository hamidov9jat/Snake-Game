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

    # Detect collision with tail.
    for segment in sn.segments:
        if segment == sn.head:
            continue
        elif sn.head.distance(segment) < 10:
            game_is_on = False
            # scoreboard.game_over()

        # Detect collision with wall.
        # if sn.head.xcor() > 280 or sn.head.xcor() < -280 or sn.head.ycor() > 280 or sn.head.ycor() < -280:
        #     game_is_on = False
        #     # scoreboard.game_over()

    # Detect collision with food.
    if sn.head.distance(fd) < 15:
        fd.refresh()
        sn.extend()
        # scoreboard.increase_score()

screen.exitonclick()

# screen.bye()
# turtle.done()
