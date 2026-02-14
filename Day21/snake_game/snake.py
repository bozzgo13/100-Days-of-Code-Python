from turtle import Turtle
MOVE_DISTANCE = 10
UP=90
DOWN=270
RIGHT=0
LEFT=180
class Snake:


    def __init__(self,):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]


    def create_snake(self):
        for i in range(3):
            segment = Turtle(shape="square")
            segment.color("white")
            segment.penup()
            segment.goto(-20 * i, 0)
            self.segments.append(segment)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            front_seg = self.segments[seg_num - 1]
            new_x = front_seg.xcor()
            new_y = front_seg.ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def right(self):
        if self.head.heading()!=LEFT:
            self.head.setheading(RIGHT)
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def grow(self):
        segment = Turtle(shape="square")
        segment.color("white")
        segment.penup()
        last_segment = self.segments[-1]
        segment.goto(x=last_segment.xcor(), y=last_segment.ycor())
        self.segments.append(segment)

    def reset(self):
        # remove all elements but first
        while len(self.segments) > 3:
            segment = self.segments.pop()
            segment.hideturtle()
            segment.clear()



        self.head.goto(0, 0)
