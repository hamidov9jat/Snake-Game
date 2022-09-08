from turtle import Turtle, Screen


class ScoreBoard(Turtle):

    def __init__(self, screen: Screen):
        super().__init__()
        self.hideturtle()
        self.penup()
        self._screen = screen
        self.sety(screen.window_height() / 2 - 30)
        self.score = 0
        # self.stamp()
        self.write(f"Your score: {self.score}", align='center', font=('Times New Roman', 20, 'normal'))

    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(f"Your score: {self.score}", align='center', font=('Times New Roman', 20, 'normal'))

    def game_over(self):
        self.clear()
        self.home()
        self.write(f"Game Over! Score: {self.score}", align='center', font=('Times New Roman', 30, 'normal'))
