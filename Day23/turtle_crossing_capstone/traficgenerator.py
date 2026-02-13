from turtle import Turtle
from car import Car
from myturtle import STEP_SIZE
import random
class TraficGenerator:
    def __init__(self):
        self.car_colors =["red", "gray", "blue", "orange", "cyan"]
        self.lines =[[],[],[],[],[],[],[],[],[],[],[],[]]
        self.car_start_positions = range(-500, 501, 20)
        for index, line in enumerate(self.lines):
            car1_x_pos = random.choice(self.car_start_positions)
            car2_x_pos = random.choice(self.car_start_positions)
            while abs(car1_x_pos - car2_x_pos) < 100:
                 car2_x_pos = random.choice(self.car_start_positions)

            car_y_pos = -250 + 20 + index * 40
            is_right = True
            if index >5: is_right = False
            new_car1 = Car(random.choice(self.car_colors), car1_x_pos,car_y_pos, is_right)
            line.append(new_car1)
            new_car2 = Car(random.choice(self.car_colors), car2_x_pos, car_y_pos, is_right)
            line.append(new_car2)
            if index % 2 == 1:
                car3_x_pos = random.choice(self.car_start_positions)
                while abs(car2_x_pos - car3_x_pos) < 100 and abs(car1_x_pos - car2_x_pos) < 100 and abs(car1_x_pos - car3_x_pos) < 120:
                    car3_x_pos = random.choice(self.car_start_positions)
                new_car3 = Car(random.choice(self.car_colors), car3_x_pos, car_y_pos, is_right)
                line.append(new_car3)

    def update(self):
        for index, line in enumerate(self.lines):
            for car in line:
                car.drive(5)
                car.draw_car()

    def colision_detection(self, turtle_step):

        print(self.lines[0][0].position())
        # turtle position collide with line
        turtle_line_collision = [[1,2],[3,4],[4,5],[6,7],[8,9],[9,10],[11,12],[13,14],[14,15],[16,17],[18,19],[19,20]]

        for index, collision_line in enumerate(turtle_line_collision):
            if turtle_step in collision_line:
                for car in self.lines[index]:
                    if -46 < car.xcor() < 46:
                            return True

        return False