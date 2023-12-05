from tkinter import *


def miles_to_kilo():
    miles=float(miles_input.get())
    kilos=round(miles*1.6,2)
    kilo_result_label.config(text=str(kilos))

window=Tk()
window.title("Miles to Kilometer Converter")
window.minsize(300,300)

miles_input = Entry()
miles_input.grid(column=1,row=0)

miles_label=Label(text='Miles')
miles_label.grid(column=2,row=0)

kilos_label=Label(text='Kilometers')
kilos_label.grid(column=2,row=1)

is_equal_to_label=Label(text="Is equal to:")
is_equal_to_label.grid(column=0,row=1)

kilo_result_label=Label(text="0")
kilo_result_label.grid(column=1,row=1)

calculate_button=Button(text='Calculate',command=miles_to_kilo)
calculate_button.grid(column=1,row=2)

window.mainloop()

