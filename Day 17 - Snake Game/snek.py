import turtle

STARTING_POSITIONS=[(0,0),(-20,0),(-40,0)]

class Snek:
    def __init__(self):
        self.score=0
        segments=[]
        for position in range(0, 3):
            new_segment = turtle.Turtle('square')
            new_segment.color('white')
            new_segment.penup()
            new_segment.goto(STARTING_POSITIONS[position][0], STARTING_POSITIONS[position][1])
            segments.append(new_segment)
        self.segments=segments



    def move_forward(self):
        for segment in range(len(self.segments)-1,0,-1):
            new_x = self.segments[segment-1].xcor()
            new_y = self.segments[segment-1].ycor()
            self.segments[segment].goto(new_x,new_y)

        self.segments[0].forward(20)




    def move_up(self):
        if self.segments[0].heading()!=270:
            self.segments[0].setheading(90)



    def move_left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)

    def move_right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)

    def move_down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)

    def eat_food(self):
        self.score=self.score+1
        new_segment = turtle.Turtle('square')
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(-1000,-1000)
        self.segments.append(new_segment)

