# import turtle
import time
from food import Food
from turtle import Screen
from snake import Snake
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(600, 600)
# screen.screensize()
# print(screen.canvwidth, screen.canvheight)
screen.bgcolor('green')
screen.title('Snake Game')
# Turn off tracer
screen.tracer(0)

sn = Snake(screen)
fd = Food(screen)
score_board = ScoreBoard(screen)

screen.listen()
screen.onkey(key='w', fun=sn.up)
screen.onkey(key='s', fun=sn.down)
screen.onkey(key='a', fun=sn.left)
screen.onkey(key='d', fun=sn.right)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.05)
    sn.move()
    if sn.bite_itself():
        game_is_on = False
        score_board.game_over()
    # # Detect collision with tail.
    # for segment in sn.segments[1:]:
    #     if sn.head.distance(segment) < 10:
    #         game_is_on = False
    #         score_board.game_over()

    # Detect collision with wall.
    # if sn.head.xcor() > 280 or sn.head.xcor() < -280 or sn.head.ycor() > 280 or sn.head.ycor() < -280:
    #     game_is_on = False
    #     # scoreboard.game_over()

    # Detect collision with food.
    if sn.head.distance(fd) < 15:
        fd.refresh()
        sn.extend()
        score_board.increase_score()
        if sn.bite_itself():
            game_is_on = False
            score_board.game_over()

screen.exitonclick()

# screen.bye()
# turtle.done()
