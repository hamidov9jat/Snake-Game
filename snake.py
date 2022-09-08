import turtle
from turtle import Turtle
from turtle import Screen

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self, sn_screen: Screen):
        self.segments = []
        self.create_snake()
        self.head: Turtle = self.segments[0]
        self.screen = sn_screen
        self.scn_w = sn_screen.window_width()
        self.scn_h = sn_screen.window_height()

    def add_segment(self, position: turtle.Vec2D):
        new_segment = Turtle("square")
        new_segment.color("red")
        new_segment.penup()
        new_segment.speed(0)
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def create_snake(self):
        """Create a snake of length 3 (squares)"""
        for position in STARTING_POSITIONS:
            self.add_segment(position)
            # new_segment = Turtle('square')
            # new_segment.penup()
            # new_segment.goto(position)
            # # new_segment.speed(0)
            # # print(new_segment.get_shapepoly())
            # # new_segment.stamp()
            # # print(f"1.{new_segment.pos()=}")
            # # print(new_segment.shearfactor())
            # # new_segment.color('green')
            # # # new_segment.shearfactor(-1.5)
            # # print(f"{new_segment.pos()=}")
            # # print(new_segment.get_shapepoly())
            # # increase = tuple(2 * num for num in new_segment.turtlesize())
            # # print(new_segment.turtlesize(*increase))
            # new_segment.color('red')
            # self.segments.append(new_segment)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            is_out_horizontally = abs(new_x) > (self.scn_w // 2)
            is_out_vertically = abs(new_y) > (self.scn_h // 2)

            opposite_x = -(self.scn_w // 2) + new_x % (self.scn_w // 2)
            opposite_y = -(self.scn_h // 2) + new_y % (self.scn_h // 2)

            if is_out_horizontally:
                self.segments[seg_num].setx(opposite_x if new_x >= 0 else new_x % (self.scn_w // 2))
            if is_out_vertically:
                self.segments[seg_num].sety(opposite_y if new_y >= 0 else new_y % (self.scn_h // 2))
            if not is_out_horizontally and not is_out_vertically:
                self.segments[seg_num].goto(new_x, new_y)

        # These are the new coordinates for the head block
        new_x = self.head.xcor() + MOVE_DISTANCE
        new_y = self.head.ycor() + MOVE_DISTANCE

        is_out_horizontally = abs(new_x) > (self.scn_w // 2)
        is_out_vertically = abs(new_y) > (self.scn_h // 2)

        # Coordinates of snake block when it passes positive x or y edge of window
        opposite_x = -(self.scn_w // 2) + new_x % (self.scn_w // 2)
        opposite_y = -(self.scn_h // 2) + new_y % (self.scn_h // 2)

        if is_out_horizontally:
            self.head.setx(opposite_x if new_x >= 0 else new_x % (self.scn_w // 2))
        if is_out_vertically:
            self.head.sety(opposite_y if new_y >= 0 else new_y % (self.scn_h // 2))
        if not is_out_horizontally and not is_out_vertically:
            self.head.forward(MOVE_DISTANCE)
        # self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def bite_itself(self):
        # Detect collision with tail.
        for segment in self.segments[1:]:
            if self.head.distance(segment) < 10:
                return True
        return False
        # return any(filter(lambda segment: self.head.distance(segment) < 10, self.segments[1:]))
