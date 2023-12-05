import turtle
import colorgram
import random

rgb_colors=[]

colors=colorgram.extract('image.jpg',30)
for color in colors:
    r=color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_colors.append((r,g,b))

timmy=turtle.Turtle()
timmy.penup()
timmy.width(20)
turtle.colormode(255)
for i in range(10):
    if i%2==0:
        timmy.left(90)
        timmy.fd(50)
        timmy.left(90)
        timmy.fd(50)
    else:
        timmy.right(90)
        timmy.fd(50)
        timmy.right(90)
        timmy.fd(50)
    for j in range(10):
        random_color=random.randint(0,29)
        timmy.color(rgb_colors[random_color][0],rgb_colors[random_color][1],rgb_colors[random_color][2])
        timmy.pendown()
        timmy.fd(1)
        timmy.penup()
        timmy.fd(50)

timmy.screen.mainloop()

print(rgb_colors)