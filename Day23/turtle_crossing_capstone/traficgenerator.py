from turtle import Turtle
from car import Car
import random
class TraficGenerator:
    def __init__(self):
        self.car_colors =["red", "gray", "blue", "orange", "cyan"]
        self.lines =[[],[],[],[],[],[],[],[],[],[],[],[]]
        self.car_start_positions = range(-270, 271, 20)
        for index, line in enumerate(self.lines):
            car_x_pos = random.choice(self.car_start_positions)
            car_y_pos = -250 + 20 + index * 40
            new_car = Car(random.choice(self.car_colors), car_x_pos,car_y_pos)
            line.append(new_car)