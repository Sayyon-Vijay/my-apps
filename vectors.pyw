from tkinter import *
from random import randint
from math import sqrt

# ___Globals___
lit_x = []
lit_y = []
vec_v1 = ''
vec_v2 = ''
vec_v3 = ''
c1 = 'black'
c2 = 'black'
o_x = 960
o_y = 500
colors = ['green', 'blue', 'red', 'orange', 'violet', 'pink', 'indigo', 'yellow']


class Vector(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, b):
        m = self.x + b.x
        n = self.y + b.y
        d = self.z + b.z
        return Vector(m, n, d)

    def __sub__(self, b):
        m = self.x - b.x
        n = self.y - b.y
        d = self.z - b.z
        return Vector(m, n, d)

    def __mul__(self, b):
        m = (self.y * b.z) - (self.z * b.y)
        n = (self.z * b.x) - (self.x * b.z)
        d = (self.x * b.y) - (self.y * b.x)
        return Vector(m, n, d)

    def __rmul__(self, b):
        m = self.x*b
        n = self.y*b
        d = self.z*b
        return Vector(m, n, d)

    def __dmul__(self, b):
        m = (self.x*b.x) + (self.y*b.y) + (self.z*b.z)
        return m

    def return_coords(self):
        return [self.x, self.y, self.z]


v1 = Vector(0, 0, 0)
v2 = Vector(0, 0, 0)
v3 = Vector(0, 0, 0)


class VecFunc(object):
    def make_vec(self):
        global v1, v2, vec_v1, vec_v2, c1, c2
        x1 = float(entry_x1.get())
        y1 = float(entry_y1.get())
        z1 = float(entry_z1.get())
        x2 = float(entry_x2.get())
        y2 = float(entry_y2.get())
        z2 = float(entry_z2.get())

        v1 = Vector(x1, y1, z1)
        v2 = Vector(x2, y2, z2)

        if v1.x < 0:
            graph_x1 = 960 + v1.x*20
        else:
            graph_x1 = 960 + v1.x*20
        if v1.y < 0:
            graph_y1 = 500 - v1.y*20
        else:
            graph_y1 = 500 - v1.y*20

        if v2.x < 0:
            graph_x2 = 960 + v2.x*20
        else:
            graph_x2 = 960 + v2.x*20
        if v2.y < 0:
            graph_y2 = 500 - v2.y*20
        else:
            graph_y2 = 500 - v2.y*20

        if v1.z == 0:
            canvas.delete(vec_v1)
            c1 = colors[randint(0, 7)]
            m.set("(" + c1 + ')')
            vec_v1 = canvas.create_line(960, 500, graph_x1, graph_y1, width=2, fill=c1)

        if v2.z == 0:
            canvas.delete(vec_v2)
            c2 = colors[randint(0, 7)]
            n.set("(" + c2 + ')')
            vec_v2 = canvas.create_line(960, 500, graph_x2, graph_y2, width=2, fill=c2)

    def add(self):
        global vec_v3, v1, v2, v3
        v3 = v1 + v2
        if v3.x < 0:
            graph_x3 = 960 + v3.x*20
        else:
            graph_x3 = 960 + v3.x*20
        if v3.y < 0:
            graph_y3 = 500 - v3.y*20
        else:
            graph_y3 = 500 - v3.y*20

        if v3.z == 0:
            canvas.delete(vec_v3)
            vec_v3 = canvas.create_line(960, 500, graph_x3, graph_y3, width=2)
        add.set(f'Addition:-  vector 3 ({v3.x}, {v3.y}, {v3.z})')

    def sub(self):
        global vec_v3, v1, v2, v3
        v3 = v1 - v2
        if v3.x < 0:
            graph_x3 = 960 + v3.x*20
        else:
            graph_x3 = 960 + v3.x*20
        if v3.y < 0:
            graph_y3 = 500 - v3.y*20
        else:
            graph_y3 = 500 - v3.y*20

        if v3.z == 0:
            canvas.delete(vec_v3)
            vec_v3 = canvas.create_line(960, 500, graph_x3, graph_y3, width=2)
        sub.set(f'Subtraction:- vector 3 ({v3.x}, {v3.y}, {v3.z})')

    def c_mul(self):
        global vec_v3, v1, v2, v3
        v3 = v1 * v2
        if v3.x < 0:
            graph_x3 = 960 + v3.x*20
        else:
            graph_x3 = 960 + v3.x*20
        if v3.y < 0:
            graph_y3 = 500 - v3.y*20
        else:
            graph_y3 = 500 - v3.y*20

        if v3.z == 0:
            canvas.delete(vec_v3)
            vec_v3 = canvas.create_line(960, 500, graph_x3, graph_y3, width=2)
        cross.set(f'Cross Product:-  vector 3 ({v3.x}, {v3.y}, {v3.z})')

    def d_mul(self):
        global vec_v3, v1, v2, v3
        v3 = v1.__dmul__(v2)
        dot.set(f'Dot Product:-  {v3}')

    def determin(self):
        global vec_v3, v1, v2, v3
        v3 = v1 * v2
        d = sqrt((v3.x ** 2) + (v3.y ** 2) + (v3.z ** 2))
        deter.set(f"Determinant:-  {d}")


def reset():
    global x_axis, y_axis, lit_x, lit_y, v1, v2, v3
    dot.set('Dot Product:- ')
    cross.set('Cross Product:- ')
    add.set('Addition:- ')
    sub.set("Subtraction:- ")
    deter.set('Determinant:- ')
    v1 = Vector(0, 0, 0)
    v2 = Vector(0, 0, 0)
    v3 = Vector(0, 0, 0)
    canvas.delete('all')
    y_axis = canvas.create_line(960, 1000, 960, 0)
    x_axis = canvas.create_line(0, 500, 1920, 500)
    for x in lit_x:
        canvas.create_line(953, x, 967, x)

    for x in lit_y:
        canvas.create_line(x, 493, x, 507)


def exit_():
    win.destroy()


for i in range(0, 1001):
    if i % 20 == 0:
        lit_x.append(i)

for i in range(0, 1921):
    if i % 20 == 0:
        lit_y.append(i)

v = VecFunc()

# ___UI___
win = Tk()
win.wm_attributes('-fullscreen', True)
canvas = Canvas(win, height=1000, width=1920, bg='light blue')
canvas.pack()

# ___lines___
y_axis = canvas.create_line(960, 1000, 960, 0)
x_axis = canvas.create_line(0, 500, 1920, 500)

for i in lit_x:
    canvas.create_line(953, i, 967, i)

for i in lit_y:
    canvas.create_line(i, 493, i, 507)

# ___labels___
label_vec1 = Label(win, text='VECTOR 1:-')
label_vec2 = Label(win, text='VECTOR 2:-')
label_vec1.place(height=25, width=100, x=40, y=1010)
label_vec2.place(height=25, width=100, x=40, y=1040)

label_x1 = Label(win, text='X')
label_x1.place(height=25, width=10, x=130, y=1010)
label_y1 = Label(win, text='Y')
label_y1.place(height=25, width=10, x=200, y=1010)
label_z1 = Label(win, text='Z')
label_z1.place(height=25, width=10, x=270, y=1010)

label_x2 = Label(win, text='X')
label_x2.place(height=25, width=10, x=130, y=1040)
label_y2 = Label(win, text='Y')
label_y2.place(height=25, width=10, x=200, y=1040)
label_z2 = Label(win, text='Z')
label_z2.place(height=25, width=10, x=270, y=1040)
m = StringVar()
n = StringVar()
color_label1 = Label(win, textvariable=m)
color_label1.place(height=25, width=45, x=10, y=1010)
color_label2 = Label(win, textvariable=n)
color_label2.place(height=25, width=45, x=10, y=1040)

dot = StringVar()
dot.set('Dot Product:- ')
label_dot_product = Label(win, textvariable=dot)
label_dot_product.place(height=25, width=120, x=1600, y=1010)

cross = StringVar()
cross.set('Cross Product:- ')
label_cross_product = Label(win, textvariable=cross)
label_cross_product.place(height=25, width=240, x=1540, y=1040)

add = StringVar()
add.set('Addition:- ')
label_add = Label(win, textvariable=add)
label_add.place(height=25, width=190, x=1200, y=1010)

sub = StringVar()
sub.set('Subtraction:- ')
label_sub = Label(win, textvariable=sub)
label_sub.place(height=25, width=240, x=1180, y=1040)

deter = StringVar()
deter.set("Determinant:- ")
label_deter = Label(win, textvariable=deter)
label_deter.place(height=25, width=170, x=960, y=1030)

# ___entries___
entry_x1 = Entry(win)
entry_y1 = Entry(win)
entry_z1 = Entry(win)
entry_x1.place(height=20, width=40, x=150, y=1010)
entry_y1.place(height=20, width=40, x=220, y=1010)
entry_z1.place(height=20, width=40, x=290, y=1010)

entry_x2 = Entry(win)
entry_y2 = Entry(win)
entry_z2 = Entry(win)
entry_x2.place(height=20, width=40, x=150, y=1040)
entry_y2.place(height=20, width=40, x=220, y=1040)
entry_z2.place(height=20, width=40, x=290, y=1040)

# ___Buttons___
vector_fy = Button(win, text='Graph', command=v.make_vec)
vector_fy.place(height=25, width=65, x=360, y=1030)

vec_add = Button(win, text='Add', command=v.add)
vec_add.place(height=25, width=65, x=450, y=1030)

vec_sub = Button(win, text='Subtract', command=v.sub)
vec_sub.place(height=25, width=70, x=540, y=1030)

vec_cmul = Button(win, text='Cross Product', command=v.c_mul)
vec_cmul.place(height=25, width=85, x=640, y=1030)

vec_dmul = Button(win, text='Dot product', command=v.d_mul)
vec_dmul.place(height=25, width=85, x=750, y=1030)

vec_deter = Button(win, text='Determinant', command=v.determin)
vec_deter.place(height=25, width=90, x=860, y=1030)

reset = Button(win, text='Reset', command=reset, bg='light green', fg='blue')
reset.place(height=25, width=65, x=1780, y=1010)

exit_but = Button(win, text='Exit', command=exit_, bg='red', fg='light green')
exit_but.place(height=25, width=65, x=1780, y=1050)
win.mainloop()
