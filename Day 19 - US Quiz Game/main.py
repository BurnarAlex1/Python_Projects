import turtle

screen=turtle.Screen()
writer=turtle.Turtle()
writer.color('black')
writer.hideturtle()
writer.penup()

score_writer=turtle.Turtle()
score_writer.color('black')
score_writer.hideturtle()
score_writer.penup()
score_writer.goto(-150,200)


screen.bgpic('blank_states_img.gif')

file=open('50_states.csv','r')
rows=[]
for row in file.readlines():
    rows.append(row.replace('\n','').split(','))

rows.pop(0)

score=0
score_writer.write("Score: " + str(score),font=('Arial',20,'normal'))

game_is_on=True
while game_is_on==True:
    text_from_user = screen.textinput('Type state or Exit:', 'State')
    if text_from_user=='Exit':
        game_is_on=False
    for i in range(0,len(rows)):
        if text_from_user==rows[i][0]:
            writer.goto(int(rows[i][1]),int(rows[i][2]))
            writer.write(rows[i][0],font=('Arial',10,'normal'))
            rows.pop(i)
            score=score+1
            break

    if score==50:
        print("You got all the states!! Congratulations!")
        game_is_on=False

    score_writer.clear()
    score_writer.write("Score: " + str(score), font=('Arial', 20, 'normal'))


screen.mainloop()