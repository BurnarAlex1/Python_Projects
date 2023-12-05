import time
import turtle
import snek
import food

turtle.colormode(255)
screen=turtle.Screen()
screen.setup(600,600)
screen.bgcolor('Black')
screen.title('My Snek Game')
screen.tracer(0)


snake=snek.Snek()
screen.listen()
screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_down, "Down")
screen.onkey(snake.move_left, "Left")
screen.onkey(snake.move_right, "Right")

score_board=turtle.Turtle()
score_board.goto(100,250)
score_board.color('white')
score_board.hideturtle()
score_board.write("Score: " + str(snake.score), align='center', font=('Arial', 24, 'normal'))



new_food=food.Food()

game_is_on = True
while game_is_on:
    screen.update()


    time.sleep(0.1)
    snake.move_forward()
    #food collision
    if snake.segments[0].distance(new_food.x_coordinate,new_food.y_coordinate)<15:
        new_food.eatten_food()
        print("Food was eatten")
        snake.eat_food()
        score_board.clear()
        score_board.write("Score: " + str(snake.score), align='center', font=('Arial', 24, 'normal'))

    #wall collisiong
    if snake.segments[0].xcor()>280 or snake.segments[0].xcor()<-280 or snake.segments[0].ycor()>280  or snake.segments[0].ycor()<-280:
        score_board.penup()
        score_board.goto(0,0)
        score_board.write("Game Over", align='center', font=('Arial', 24, 'normal'))
        break

    #snek collision
    for segment_nr in range(1,len(snake.segments)-1):
        if snake.segments[0].distance(snake.segments[segment_nr])<10:
            game_is_on=False
            score_board.penup()
            score_board.goto(0, 0)
            score_board.write("Game Over", align='center', font=('Arial', 24, 'normal'))




screen.exitonclick()



