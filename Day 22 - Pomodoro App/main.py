from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
timer= None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global timer
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text=f'00:00')
    timer=None
    global reps
    reps= 0
# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_secs=WORK_MIN*60
    short_break_secs=SHORT_BREAK_MIN*60
    long_break_secs=LONG_BREAK_MIN*60
    if reps%2==1:
        title_label.config(text='Work')
        check_mark_label.config(text='')
        counter(work_secs)
    else:
        if reps%8==0:
            title_label.config(text='Long Break')
            check_mark_label.config(text='✓')
            counter(long_break_secs)
        else:
            title_label.config(text='Short Break')
            check_mark_label.config(text='✓')
            counter(short_break_secs)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def counter(count):
    minutes=math.floor(count/60)
    seconds=count%60
    if seconds<10:
        seconds=f'0{seconds}'
    canvas.itemconfig(timer_text,text=f'{minutes}:{seconds}')
    if count>0:
        global timer
        timer= window.after(1000,counter,count-1)


# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title('Pomodoro')
window.config(padx=30,pady=30)
window.config(bg=YELLOW)


title_label=Label(text='Timer',fg=GREEN,font=('Arial',30,'bold'))
title_label.grid(column='1',row='0')


canvas=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
canvas.grid(column='1',row='1')


tomato_image=PhotoImage(file='tomato.png')
canvas.create_image(100,112,image=tomato_image)
timer_text=canvas.create_text(100,126,text='00:00',fill='white',font=('Arial',35,'bold'))



start_button=Button(width=10,height=2,text='Start',bg='green',highlightthickness=0,command=start_timer)
start_button.grid(column=0,row=2)

stop_button=Button(width=10,height=2,text='Stop',bg='green',highlightthickness=0,command=reset_timer)
stop_button.grid(column=2,row=2)


check_mark_label=Label(text='✓',bg=YELLOW,fg='green',font=('Arial',30,'bold'))
check_mark_label.grid(column=1,row=3)



window.mainloop()