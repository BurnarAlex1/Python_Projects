from tkinter import *
import random

BACKGROUND_COLOR = "#B1DDC6"
timer=None
words=None
def reset_timer():
    global timer
    screen.after_cancel(timer)
    timer=None


def flip_card():
    global normal_text_id
    global fr_text_id
    global words

    card_canvas.itemconfig(current_card_image, image=back_card)
    card_canvas.delete(normal_text_id)
    normal_text_id = card_canvas.create_text(400, 263, text=words[1], font=('Arial', 28, 'bold'))
    card_canvas.delete(fr_text_id)
    fr_text_id = card_canvas.create_text(400, 100, text='English', font=('Arial', 30, 'bold'))

def right_button_func():
    global lines
    global timer
    global normal_text_id
    global fr_text_id
    global words




    random_nr=random.randint(0,len(lines)-1)
    words=lines[random_nr].replace('\n','').split(',')
    card_canvas.delete(normal_text_id)
    card_canvas.delete(fr_text_id)
    fr_text_id=card_canvas.create_text(400, 100, text='French', font=('Arial', 30, 'bold'))
    normal_text_id=card_canvas.create_text(400,263,text=words[0],font=('Arial',28,'bold'))

    card_canvas.itemconfig(current_card_image, image=front_card)
    card_canvas.update()
    timer=screen.after(3000,func=flip_card())








french_words_file=open(file='data/french_words.csv',mode='r')
lines=french_words_file.readlines()
lines.pop(0)
fr_eng_dict={}


for line in lines:
    words = line.replace('\n', '').split(',')
    fr_eng_dict[words[0]]=words[1]

screen=Tk()
screen.title('Flash Card App')
screen.configure(bg="#B1DDC6")


back_card=PhotoImage(file="images/card_back.png")
front_card=PhotoImage(file='images/card_front.png')
right_image=PhotoImage(file='images/right.png')
wrong_image=PhotoImage(file='images/wrong.png')

card_canvas=Canvas(screen,height=526,width=800,bg="#B1DDC6",highlightthickness=0)
current_card_image=card_canvas.create_image(400,263,image=front_card)
card_canvas.grid(column=0,row=0,columnspan=3)

normal_text_id=card_canvas.create_text(400,263,text=words[0],font=('Arial',28,'bold'))
fr_text_id=card_canvas.create_text(400,100,text='French',font=('Arial',30,'bold'))

right_button=Button(screen,image=right_image,width=100,height=100,bg="#B1DDC6",highlightthickness=0,command=right_button_func)
right_button.grid(column=0,row=1)

wrong_button=Button(screen,image=wrong_image,width=100,height=100,bg="#B1DDC6",highlightthickness=0,command=reset_timer)
wrong_button.grid(column=2,row=1)


timer=screen.after(3000,func=flip_card)

screen.mainloop()

