from tkinter import *
window = Tk()
window.title('Mile to KM Convertor')
window.minsize(width=300, height=300)


user_val = Entry(width='15')
user_val.grid(row=0, column=1)


def convertor():
    miles = float(user_val.get())
    km = miles*1.609
    answer.config(text=km)


l0 = Label(text="Mile(s)")
l0.grid(row=0, column=3)
l0.config(padx=5, pady=5)

l1 = Label(text='are Equal to ')
l1.grid(row=1, column=0)
l1.config(padx=5, pady=5)

answer = Label(text='')
answer.grid(row=1, column=1)
answer.config(padx=5, pady=5)

l2 = Label(text='KM')
l2.grid(row=1, column=2)
l2.config(padx=5, pady=5)

b1 = Button(text='Calculate', bg='red', fg='white', command=convertor)
b1.grid(row=2, column=1)
b1.config(padx=5, pady=5)

window.mainloop()
