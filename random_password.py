from tkinter import *
import random as rnd
length = 0
password = []
usr_password = ''
ne = ''


def get_enter():
    global length
    length = int(pass_len.get())


def func():
    win.destroy()


def generator():
    global length, password, usr_password, a, label2
    random_pass = ["'", 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                   't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                   'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7',
                   '8', '9', '0', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '=', '{', '}', '[', ']',
                   '|', ':', ';', "'", '>', '<', '/', '?', ',', '.', '~', '`']
    print(len(random_pass))	
    n = 0
    while n != length:
        password.append(random_pass[rnd.randint(0, 91)])
        n += 1
    for i in password:
        usr_password += i
    a.set(usr_password)
    label2 = Label(win, textvariable=a)
    usr_password = ''
    password = []


def one():
    get_enter()
    generator()


win = Tk()
# win.wm_attributes("-fullscreen", True)
win.title("RANDOM PASSWORD GENERATOR")
frame = Frame(win, height=800, width=1000, bg='light blue')
frame.pack()
label1 = Label(frame, text="How long do you want your password to be?")
label1.place(x=433, y=200)
a = StringVar()
label2 = Label(win, textvariable=a)
label2.place(x=445, y=295)
label3 = Label(win, text='Your password is:- ')
label3.place(anchor='ne', x=440, y=295)
pass_len = Entry(frame)
pass_len.place(width=170, x=470, y=250)
pass_button = Button(frame, text='Generate', command=one)
pass_button.place(x=490, y=340)
exit_button = Button(frame, text='Exit', command=func)
exit_button.place(height=25, width=40, x=570, y=340)
win.mainloop()
# 64087