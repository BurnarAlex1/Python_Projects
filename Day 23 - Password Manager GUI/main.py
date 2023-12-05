import tkinter.messagebox
from tkinter import *
import random


def generate_password():
    password=''
    for i in range(0,10):
        ascii_code=random.randint(33,126)
        letter=chr(ascii_code)
        password=password+letter
    password_text_field.delete(0,END)
    password_text_field.insert(END,password)


def search_data():
    web_aux=website_text_field.get()
    pass_aux=''
    email_aux=''
    if web_aux=='':
        message.show(title='Input error',message='Website input is worng')
    else:
        lines=[]
        with open('data_file.txt') as f:
            lines = f.readlines()
        for line in lines:
            if web_aux in line:
                message.show(title='Data found!',
                             message=line)







def assign_data():
    data_file = open('data_file.txt', 'a+')

    web_aux=website_text_field.get()
    pass_aux=password_text_field.get()
    email_aux=email_text_field.get()
    if web_aux=='':
        message.show(title='Inputs Error', message='Wrong inputs')
        return 0
    data_file.write('Website: '+ web_aux +' Email: '+ email_aux + ' Password: '+pass_aux+'\n')

    data_file.close()



screen=Tk()
screen.title('Password Manager')
screen.minsize(300,350)



image_canvas=Canvas(screen,height=356,width=356)
lock_photo = PhotoImage(file='lock2.png')
image_canvas.create_image(206,206,image=lock_photo)
image_canvas.config(highlightthickness=0)
image_canvas.grid(row=0,column=1,columnspan=3)

password_label=Label(text='Password:')
password_label.grid(row=1,column=1)

email_label=Label(text='Email:')
email_label.grid(row=2,column=1)

website_label=Label(text='Website:')
website_label.grid(row=3,column=1)

email_text_field=Entry(width=40)
email_text_field.grid(row=2,column=2,columnspan=2)

password_text_field=Entry()
password_text_field.grid(row=1,column=2)

website_text_field=Entry()
website_text_field.grid(row=3,column=2)

search_button=Button(height=1,width=10,text='Search',command=search_data)
search_button.grid(row=3,column=3)

generate_button=Button(height=1,width=10,text='Generate',command=generate_password)
generate_button.grid(row=1,column=3)

assign_button=Button(height=1,width=40,text='Assign',command=assign_data)
assign_button.grid(row=4,column=1,columnspan=3)

message=tkinter.messagebox.Message(screen)




screen.mainloop()