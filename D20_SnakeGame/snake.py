import turtle as t

POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
FD_DIST = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake_seg = []
        self.create_snake()
        self.snake_head = self.snake_seg[0]

    def add_segment(self, pos):
        snake_part = t.Turtle(shape="square")
        snake_part.color("white")
        snake_part.pu()
        snake_part.goto(pos)
        self.snake_seg.append(snake_part)

    def create_snake(self):
        for pos in POSITIONS:
            self.add_segment(pos)

    def reset(self):
        for seg in self.snake_seg:
            seg.goto(1000, 1000)
        self.snake_seg.clear()
        self.create_snake()
        self.snake_head = self.snake_seg[0]

    def extend(self):
        # adds a new segment to the end of the snake
        self.add_segment(self.snake_seg[-1].position())

    def move(self):
        for seg_num in range(len(self.snake_seg)-1, 0, -1):
            new_x = self.snake_seg[seg_num-1].xcor()
            new_y = self.snake_seg[seg_num-1].ycor()
            self.snake_seg[seg_num].goto(new_x, new_y)
        self.snake_head.fd(FD_DIST)

    def up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.seth(UP)

    def down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.seth(DOWN)

    def right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.seth(RIGHT)

    def left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.seth(LEFT)
