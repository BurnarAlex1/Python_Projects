import requests
from tkinter import *

def get_quote():
    global kanye_text
    my_req = requests.get(url='https://api.kanye.rest')
    my_req.raise_for_status()

    data = my_req.json()

    canvas.delete(kanye_text)
    kanye_text=canvas.create_text(150,207,width=250,text=data['quote'],font=('Arial',20,'normal'))
    print(data)

screen=Tk()
screen.title('Kanye quote app')
screen.config(padx=20,pady=20)



canvas=Canvas(master=screen,height=414, width=300)
filename=PhotoImage(file='background.png')
canvas_image=canvas.create_image(150,207,image=filename)
canvas.grid(row=0,column=0)
kanye_text=canvas.create_text(150,207,width=250,text='Press my face for a quote',font=('Arial',20,'normal'))
Kanye_Photo=PhotoImage(file='kanye.png')
button=Button(master=screen,image=Kanye_Photo, command = get_quote)
button.grid(row=1,column=0)


screen.mainloop()




