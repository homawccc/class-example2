from tkinter import *
import csv

m = Tk()
m.title("Running Pace")
m.configure(bg="#CCEECC", padx=16, pady=16)

#Labels
labt=Label(m, text='Running Pace Calculator', 
fg='#0000AA', bg="#CCEECC", pady=6, font=('Cambria', 24, 'bold'))
lab1=Label(m, text='Minutes ', bg="#CCEECC", font=('none', 14), pady=4)
lab2=Label(m, text='Seconds ', bg="#CCEECC", font=('none', 14), pady=4)
lab3=Label(m, text='Miles ', bg="#CCEECC", font=('none', 14), pady=4)
lab4=Label(m, text='Date ', bg="#CCEECC", font=('none', 14), pady=4)
lab5=Label(m, text='Or Enter Past Date: ', bg="#CCEECC", font=('none', 12), pady=4)
btn1=Button(m, text='USE TODAY', font=("none", 12))
lab6=Label(m, text='Month:   Day:   Year:', bg="#CCEECC",
 font=('none', 14), pady=4)
ent1 = Entry(m, font=("none", 14))
ent2 = Entry(m, font=("none", 14))
ent3 = Entry(m, font=("none", 14))
fr1 = Frame(m)
ent4 = Entry(fr1, font=("none", 14), width=3)
ent5 = Entry(fr1, font=("none", 14), width=3)
ent6 = Entry(fr1, font=("none", 14), width=3)

#grid layout
labt.grid(row=0, columnspan=2)
lab1.grid(row=1, column=0, sticky=E)
lab2.grid(row=2, column=0, sticky=E)
lab3.grid(row=3, column=0, sticky=E)
lab4.grid(row=4, column=0, sticky=E)
lab5.grid(row=5, column=1, sticky=W)
lab6.grid(row=6, column=1, sticky=W)
ent1.grid(row=1, column=1, sticky=W)
ent2.grid(row=2, column=1, sticky=W)
ent3.grid(row=3, column=1, sticky=W)
btn1.grid(row=4, column=1, sticky=W)
fr1.grid(row=7, column=1, sticky=W)
ent4.grid(row=0, column=0, sticky=W)
ent5.grid(row=0, column=1, sticky=W)
ent6.grid(row=0, column=2, sticky=W)


m.mainloop()