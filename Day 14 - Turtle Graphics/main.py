import turtle
import random
timmy=turtle.Turtle()


turtle.colormode(255)
timmy.width(2)
timmy.speed(10.0)
for j in range(10):
    timmy.right(10)
    timmy.pencolor(random.randint(0,255),random.randint(0,255),random.randint(0,255))
    for i in range(360):
        timmy.fd(2)
        timmy.right(1)



timmy.screen.mainloop()
