from tkinter import *


window = Tk()

window.minsize(height=408,width=417)

input_box = Entry(window, width = 40,borderwidth = 5)
input_box.pack(pady = 30)


def click(num):
    input_box.insert("end",str(num))


# Button:

button_1 = Button(text = "1", width = 10,command = lambda:click(1))
button_1.place(x= 10,y= 100)

button_2 = Button(text = "2", width = 10,command = lambda:click(2))
button_2.place(x= 140,y= 100)

button_3 = Button(text = "3", width = 10,command = lambda:click(3))
button_3.place(x= 270,y= 100)

button_4 = Button(text = "4", width = 10,command = lambda:click(4))
button_4.place(x= 10,y= 140)

button_5 = Button(text = "5", width = 10,command = lambda:click(5))
button_5.place(x= 140,y= 140)

button_6 = Button(text = "6", width = 10,command = lambda:click(6))
button_6.place(x= 270,y= 140)

button_7 = Button(text = "7", width = 10,command = lambda:click(7))
button_7.place(x= 10,y= 180)

button_8 = Button(text = "8", width = 10,command = lambda:click(8))
button_8.place(x= 140,y= 180)

button_9 = Button(text = "9", width = 10,command = lambda:click(9))
button_9.place(x= 270,y= 180)

button_0 = Button(text = "0", width = 10,command = lambda:click(0))
button_0.place(x= 10,y= 220)

def add():
   global n1 
   n1 = input_box.get()
   global math
   math = "addition"
   input_box.delete(0,END)

button_add = Button(text = "+", width = 10,command = add)
button_add.place(x= 140,y= 220)



def subs():
   global n1 
   n1 = input_box.get()
   global math
   math = "subtraction"
   input_box.delete(0,END)


button_subs = Button(text = "-", width = 10,command = subs)
button_subs.place(x= 270,y= 220)

def mult():
   global n1 
   n1 = input_box.get()
   global math
   math = "multiplication"
   input_box.delete(0,END)


button_mult = Button(text = "*", width = 10,command = mult)
button_mult.place(x= 10,y= 260)

def div():
   global n1 
   n1 = input_box.get()
   global math
   math = "division"
   input_box.delete(0,END)



button_div = Button(text = "/", width = 10,command = div)
button_div.place(x= 140,y= 260)

def equal():
    
    n2 = input_box.get()
    input_box.delete(0,END)
    
    if math == "addition":
        input_box.delete(0,END)
        input_box.insert(0, int(n1) + int(n2))
    elif math == "subtraction":
        input_box.insert(0, int(n1) - int(n2))
    elif math == "multiplication":
        input_box.insert(0, int(n1) * int(n2))
    elif math == "division":
        if int(n2) == 0:
            input_box.insert(0,"Zero Division Error")
        else:
            input_box.insert(0, int(n1) / int(n2))
    else:
        input_box.insert("invalid input")

button_edual = Button(text = "=", width = 10,command = equal)
button_edual.place(x= 270,y= 260)

button_clear = Button(text = "clear", width = 10,command = lambda:input_box.delete(0, "end"))
button_clear.place(x= 270,y= 300)

quit_button = Button(window,text = "Quit", width = 14,command = window.destroy)
quit_button.place(x= 120,y= 350)
 
window.mainloop()