from random import seed
from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0, 260)
        self.color("White")
        self.score = 0
        f = open("Projects/D20_SnakeGame/prev_score.txt", 'r')
        self.highscore = int(f.read())
        self.ht()
        self.pu()
        self.scoreupdate()

    def scoreupdate(self):
        
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", False, align="center",
                   font=("Halevatica", 24, "normal"))

    def reset(self):
        # resets the score
        if self.score > self.highscore:
            self.highscore = self.score
        f1 = open("Projects/D20_SnakeGame/prev_score.txt", 'w')
        f1.write(f"{self.score}")
        self.score = 0
        self.scoreupdate()

    def increment_score(self):
        self.score += 1
        self.clear()
        self.scoreupdate()
