import turtle as t
import time
from snake import Snake
from point import Point
from scores import Score
screen = t.Screen()
screen.setup(width=600, height=600)
screen.title("The Classic Snake")
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
point = Point()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_on = True
while game_on:
    screen.update()
    time.sleep(0.05)
    snake.move()

    # Detect collision of snake and point
    if snake.snake_head.distance(point) < 15:
        point.refresh_point()
        snake.extend()
        score.increment_score()

    # Detect collision with the wall
    if snake.snake_head.xcor() > 280 or snake.snake_head.xcor() < -280 or snake.snake_head.ycor() > 280 or snake.snake_head.ycor() < -280:
        score.reset()
        snake.reset()

    # Detect collision with tail
    for seg in snake.snake_seg[1:]:
        if snake.snake_head.distance(seg) < 10:
            score.reset()
            snake.reset()
screen.exitonclick()
