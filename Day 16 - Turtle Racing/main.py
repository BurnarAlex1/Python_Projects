import turtle
import random

red=turtle.Turtle()
red.color('red')
red.penup()
blue=turtle.Turtle()
blue.color('blue')
blue.penup()
green=turtle.Turtle()
green.color('green')
green.penup()
yellow=turtle.Turtle()
yellow.color('yellow')
yellow.penup()
purple=turtle.Turtle()
purple.color('purple')
purple.penup()

player=input("Choose a turtle(red,blue,green,yellow,purple): ")

turtles=[[red,0],[blue,0],[green,0],[yellow,0],[purple,0]]
turtle_counter=0

for turtle_player,distance in turtles:
    turtle_player.left(90)
    turtle_player.fd(turtle_counter)
    turtle_counter+=20
    turtle_player.left(90)
    turtle_player.fd(200)
    turtle_player.left(180)

while True:
    random_turtle=random.randint(0,4)
    turtles[random_turtle][0].fd(2)
    turtles[random_turtle][1]+=2
    if turtles[random_turtle][1]==500:
        if random_turtle==0:
            print("Red has won!")
            if player=='red':
                print('You have won!!')
        elif random_turtle==1:
            print("Blue has won!")
            if player=='blue':
                print('You have won!!')
        elif random_turtle == 2:
            print("Green has won!")
            if player=='green':
                print('You have won!!')
        elif random_turtle == 3:
            print("Yellow has won!")
            if player=='yellow':
                print('You have won!!')
        elif random_turtle == 4:
            print("Purple has won!")
            if player=='purple':
                print('You have won!!')
        break




red.screen.mainloop()





