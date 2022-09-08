from turtle import Turtle, Screen
import random


class Food(Turtle):
    def __init__(self, fd_screen: Screen):
        super().__init__('circle')
        self.penup()
        self.shapesize(stretch_wid=.5, stretch_len=.5)
        self.color('black')
        self.speed(0)
        self.screen = fd_screen
        self.wn_w = fd_screen.window_width()
        self.wn_h = fd_screen.window_height()
        self.refresh()

    def refresh(self):
        random_x = random.randint(-(self.wn_w // 2), self.wn_w // 2)
        random_y = random.randint(-(self.wn_h // 2), self.wn_h // 2)
        self.goto(random_x, random_y)
