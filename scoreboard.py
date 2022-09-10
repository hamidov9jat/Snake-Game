from turtle import Turtle, Screen


class ScoreBoard(Turtle):

    def __init__(self, screen: Screen):
        super().__init__()
        self.score = 0
        with open('data.txt') as f:
            self._high_score = int(f.read().strip())
        self.hideturtle()
        self.color('white')
        self.penup()
        self._screen = screen
        self.sety(screen.window_height() / 2 - 30)
        # self.stamp()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Your score: {self.score} High Score: {self._high_score}", align='center',
                   font=('Times New Roman', 20, 'normal'))

    def reset(self) -> None:
        if self.score > self._high_score:
            self._high_score = self.score
        with open('data.txt', mode='w') as f:
            f.write(f'{self._high_score}')

        self.score = 0
        self.update_score()

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_score()

    def game_over(self):
        self.clear()
        self.home()
        self.write(f"Game Over!", align='center', font=('Times New Roman', 30, 'normal'))
