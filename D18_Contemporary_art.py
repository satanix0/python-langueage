import random
import turtle as t
t.colormode(255)
tim = t.Turtle()
tim.speed("fastest")


rgb_color = [(253, 252, 241), (238, 250, 244), (188, 19, 46), (244, 233, 64),
             (252, 232, 237), (217, 239, 245), (195, 76, 34), (218, 66, 106),
             (13, 143, 89), (18, 125, 173), (196, 176, 17), (1, 154, 91),
             (238, 232, 3), (25, 40, 75), (36, 43, 111), (78, 175, 96),
             (181, 44, 65), (217, 67, 47), (217, 129, 153), (125, 185, 120),
             (238, 161, 180), (7, 61, 38), (147, 209, 220), (8, 91, 52),
             (5, 86, 109), (160, 30, 27), (237, 170, 163), (158, 211, 188)]

tim.pu()
tim.seth(225)
tim.fd(300)
tim.seth(0)


def paint(dots):
    for i in range(1, dots):
        tim.dot(20, random.choice(rgb_color))
        # tim.penup()
        tim.fd(50)
        # tim.pd()
        if(i % 10 == 0):
            tim.setheading(90)
            tim.fd(50)
            tim.setheading(180)
            tim.fd(500)
            tim.setheading(0)


paint(100)
# for _ in range(10):
#
#     tim.penup()
#     tim.lt(90)
#     tim.fd(50)
#     tim.rt(90)
#     tim.bk(500)


my_screen = t.Screen()
my_screen.exitonclick()
