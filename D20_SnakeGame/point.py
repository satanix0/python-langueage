from re import S
from turtle import Turtle
import random


class Point(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.pu()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh_point()
    
    def refresh_point(self):
        self.goto(x=random.randint(-280, 280), y=random.randint(-280, 280))