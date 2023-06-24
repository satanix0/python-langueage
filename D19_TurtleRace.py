import random
import turtle as t

race_mode = False
screen = t.Screen()
screen.setup(width=500, height=400)
user_choice = screen.textinput(
    title="Make Your choice", prompt="Which turtle will win the race ?")

color = ['red', 'green', 'blue', 'yellow', 'orange', 'purple']
turtles = []
y = -100
x = -230
for i in range(0, 6):
    new_turtle = t.Turtle(shape="turtle")
    new_turtle.color(color[i])
    new_turtle.pu()
    new_turtle.goto(x, y)
    y += 50
    turtles.append(new_turtle)

if user_choice:
    race_mode = True

while race_mode:
    for turtle in turtles:
        if turtle.xcor() > 230:
            race_mode = False
            win = turtle.pencolor()
            if win == user_choice:
                print(f"Yay!! Your {win}turtle won the race")
            else:
                print(f"Sorry!! Your turtle lost to {win} turtle")
        distance = random.randint(0, 10)
        turtle.fd(distance)

screen.exitonclick()
