from tkinter import *

m = Tk()
m.title("Labels Grid")

lab1 = Label(m, bg="red", fg="white", text="Red", width=20, height=3)
lab2 = Label(m, bg="green", fg="white", text="Green", width=20, height=3)
lab3 = Label(m, bg="blue", fg="white", text="Blue", width=20, height=3)

lab1.grid(row=0, column=0)
lab2.grid(row=0, column=1)
lab3.grid(row=1, columnspan=2, sticky=E+W)

m.mainloop()