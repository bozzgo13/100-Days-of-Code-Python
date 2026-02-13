import turtle


class Car(turtle.Turtle):
    def __init__(self, color="red", my_x=0, my_y=0, is_right=True):
        super().__init__()

        self.car_color = color


        self.is_right = is_right
        self.hideturtle()
        self.car_length = 80
        self.car_width = 32
        self.penup()
        self.goto(my_x, my_y)
        self.pendown()

        self.draw_car()

    def draw_rectangle(self, x, y, w, h, color):
        self.penup()
        self.goto(x, y)
        self.setheading(0)
        self.pendown()
        self.fillcolor(color)
        self.begin_fill()
        for _ in range(2):
            self.forward(w)
            self.left(90)
            self.forward(h)
            self.left(90)
        self.end_fill()

    def draw_car(self):
        old_pos = self.pos()
        old_heading = self.heading()

        self.clear()
        my_x = self.xcor()
        my_y = self.ycor()
        # Center of the car is (0,0)
        # car body: 80 x 32
        self.draw_rectangle(my_x-40, my_y-16, self.car_length, self.car_width, self.car_color)

        # car cabin
        self.draw_rectangle(my_x-25, my_y-12, 50, 24, "darkgrey")

        # wheels
        wheels = [(-30, 16), (10, 16), (-30, -24), (10, -24)]
        for x, y in wheels:
            self.draw_rectangle(my_x+x, my_y+y, 20, 8, "black")

        # lights
        if self.is_right:
            lights = [(30, 6), (30, -12)]
        else:
            lights = [(-30, 6), (-30, -12)]
        for x, y in lights:
            self.draw_rectangle(my_x+x, my_y+y, 10, 6, "yellow")
        self.penup()
        self.goto(old_pos)
        self.setheading(old_heading)

    def drive(self, speed):
        my_x = self.xcor()
        my_y = self.ycor()

        if self.is_right==True and my_x >500:
            self.goto(-500, my_y)
        elif self.is_right == False and my_x < -500:
            self.goto(500, my_y)
        elif self.is_right:
            self.goto(my_x + speed,my_y)
        else:
            self.goto(my_x - speed,my_y)