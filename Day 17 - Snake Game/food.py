import turtle
import random

class Food(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.coordinates=0
        self.shapesize(0.5)
        self.color('green')
        self.speed('fastest')
        self.x_coordinate=random.randint(-280, 280)
        self.y_coordinate=random.randint(-280, 280)
        self.goto(self.x_coordinate, self.y_coordinate)

    def eatten_food(self):
        self.x_coordinate = random.randint(-280, 280)
        self.y_coordinate = random.randint(-280, 280)
        self.goto(self.x_coordinate, self.y_coordinate)