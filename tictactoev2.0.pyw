# import random as rn
from tkinter import *

# ___Globals___
game_win = False
game_tie = False

comp = False

line1_1 = ''
line2_1 = ''

line1_2 = ''
line2_2 = ''

line1_3 = ''
line2_3 = ''

line1_4 = ''
line2_4 = ''

line1_5 = ''
line2_5 = ''

line1_6 = ''
line2_6 = ''

line1_7 = ''
line2_7 = ''

line1_8 = ''
line2_8 = ''

line1_9 = ''
line2_9 = ''

state1 = ''
state2 = ''
state3 = ''
state4 = ''
state5 = ''
state6 = ''
state7 = ''
state8 = ''
state9 = ''

o1 = ''
o2 = ''
o3 = ''
o4 = ''
o5 = ''
o6 = ''
o7 = ''
o8 = ''
o9 = ''

n1 = ''
n2 = ''
n3 = ''
n4 = ''
n5 = ''
n6 = ''
n7 = ''
n8 = ''
n9 = ''

score_x_total = ''
score_o_total = ''
x = False
o = False
round_count = 0
play1_name = ''
play2_name = ''


def exit_1():
    win.destroy()


def yes_func():
    global game_win, game_tie, line1_1, line2_1, line1_2, line2_2, line1_3, line2_3, line1_4, line2_4, line1_5, line2_5
    global line1_6, line2_6, line1_7, line2_7, line1_8, line2_8, line1_9, line2_9, state1, state2, state3, state4, n9
    global state5, state6, state7, state8, state9, o1, o2, o3, o4, o5, o6, o7, o8, o9, n1, n2, n3, n4, n5, n6, n7, n8
    game_win = False
    game_tie = False

    line1_1 = ''
    line2_1 = ''

    line1_2 = ''
    line2_2 = ''

    line1_3 = ''
    line2_3 = ''

    line1_4 = ''
    line2_4 = ''

    line1_5 = ''
    line2_5 = ''

    line1_6 = ''
    line2_6 = ''

    line1_7 = ''
    line2_7 = ''

    line1_8 = ''
    line2_8 = ''

    line1_9 = ''
    line2_9 = ''

    state1 = ''
    state2 = ''
    state3 = ''
    state4 = ''
    state5 = ''
    state6 = ''
    state7 = ''
    state8 = ''
    state9 = ''

    o1 = ''
    o2 = ''
    o3 = ''
    o4 = ''
    o5 = ''
    o6 = ''
    o7 = ''
    o8 = ''
    o9 = ''

    n1 = ''
    n2 = ''
    n3 = ''
    n4 = ''
    n5 = ''
    n6 = ''
    n7 = ''
    n8 = ''
    n9 = ''
    canvas1.delete('all')
    canvas2.delete('all')
    canvas3.delete('all')
    canvas4.delete('all')
    canvas5.delete('all')
    canvas6.delete('all')
    canvas7.delete('all')
    canvas8.delete('all')
    canvas9.delete('all')
    txtvar1.set('')
    txtvar2.set('')
    yes.set('')
    no.set('')


def loop_func():
    if not comp:
        global game_win, game_tie
        if game_tie or game_win:
            txtvar2.set("Do you want to play again?")
            yes.set("YES")
            no.set('NO')


# ___Secondary game functions___
class CheckWinTie:
    def check_win1(self):
        global game_win, x
        if state1 == state2 == state3 == "X":
            game_win = True
            x = True
            txtvar1.set(f'Player {play1_name} won!')
            if not comp:
                loop_func()
            else:
                next_round()
        if state4 == state5 == state6 == 'X':
            game_win = True
            x = True
            txtvar1.set(f'Player {play1_name} won!')
            if not comp:
                loop_func()
            else:
                next_round()
        if state7 == state8 == state9 == 'X':
            game_win = True
            x = True
            txtvar1.set(f'Player {play1_name} won!')
            if not comp:
                loop_func()
            else:
                next_round()
        if state1 == state4 == state7 == 'X':
            game_win = True
            x = True
            txtvar1.set(f'Player {play1_name} won!')
            if not comp:
                loop_func()
            else:
                next_round()
        if state2 == state5 == state8 == 'X':
            game_win = True
            x = True
            txtvar1.set(f'Player {play1_name} won!')
            if not comp:
                loop_func()
            else:
                next_round()
        if state3 == state6 == state9 == "X":
            game_win = True
            x = True
            txtvar1.set(f'Player {play1_name} won!')
            if not comp:
                loop_func()
            else:
                next_round()
        if state1 == state5 == state9 == "X":
            game_win = True
            x = True
            txtvar1.set(f'Player {play1_name} won!')
            if not comp:
                loop_func()
            else:
                next_round()
        if state3 == state5 == state7 == "X":
            game_win = True
            x = True
            txtvar1.set(f'Player {play1_name} won!')
            if not comp:
                loop_func()
            else:
                next_round()

    def check_win2(self):
        global game_win, o
        if state1 == state2 == state3 == "O":
            game_win = True
            o = True
            txtvar1.set(f'Player {play2_name} won!')
            if not comp:
                loop_func()
            else:
                next_round()
        if state4 == state5 == state6 == 'O':
            game_win = True
            o = True
            txtvar1.set(f'Player {play2_name} won!')
            if not comp:
                loop_func()
            else:
                next_round()
        if state7 == state8 == state9 == 'O':
            game_win = True
            o = True
            txtvar1.set(f'Player {play2_name} won!')
            if not comp:
                loop_func()
            else:
                next_round()
        if state1 == state4 == state7 == 'O':
            game_win = True
            o = True
            txtvar1.set(f'Player {play2_name} won!')
            if not comp:
                loop_func()
            else:
                next_round()
        if state2 == state5 == state8 == 'O':
            game_win = True
            o = True
            txtvar1.set(f'Player {play2_name} won!')
            if not comp:
                loop_func()
            else:
                next_round()
        if state3 == state6 == state9 == "O":
            game_win = True
            o = True
            txtvar1.set(f'Player {play2_name} won!')
            if not comp:
                loop_func()
            else:
                next_round()
        if state1 == state5 == state9 == "O":
            game_win = True
            o = True
            txtvar1.set(f'Player {play2_name} won!')
            if not comp:
                loop_func()
            else:
                next_round()
        if state3 == state5 == state7 == "O":
            game_win = True
            o = True
            txtvar1.set(f'Player {play2_name} won!')
            if not comp:
                loop_func()
            else:
                next_round()

    def check_tie(self):
        global game_tie
        if not game_win and not game_tie:
            if state1 != '' and state2 != '' and state3 != '' and state4 != '' and state5 != '' and state6 != '' and \
               state7 != '' and state8 != '' and state9 != '':
                game_tie = True
                txtvar1.set("TIE!")
                loop_func()


# ___Primary game functions___
class CreateDelete:
    def create_func1(self):
        global n1, line1_1, line2_1, o1, state1
        if not game_win and not game_tie:
            if n1 == 1:
                line1_1 = canvas1.create_line(0, 0, 245, 245, width=4)
                line2_1 = canvas1.create_line(245, 0, 0, 245, width=4)
                state1 = 'X'
            if n1 == 2:
                o1 = canvas1.create_oval(240, 240, 3, 3, width=4)
                state1 = "O"
            if n1 == 3:
                pass
            a = CheckWinTie()
            a.check_win1()
            a.check_win2()
            a.check_tie()

    def create_x1(self, event):
        global n1
        if n1 != 2:
            n1 = 1
        CreateDelete.create_func1(self)

    def create_o1(self, event):
        global n1
        if n1 != 1:
            n1 = 2
        CreateDelete.create_func1(self)

    def create_func2(self):
        global n2, line1_2, line2_2, o2, state2
        if not game_win and not game_tie:
            if n2 == 1:
                line1_2 = canvas2.create_line(0, 0, 245, 245, width=4)
                line2_2 = canvas2.create_line(245, 0, 0, 245, width=4)
                state2 = 'X'
            if n2 == 2:
                o2 = canvas2.create_oval(240, 240, 3, 3, width=4)
                state2 = "O"
            if n2 == 3:
                pass
            a = CheckWinTie()
            a.check_win1()
            a.check_win2()
            a.check_tie()

    def create_x2(self, event):
        global n2
        if n2 != 2:
            n2 = 1
        CreateDelete.create_func2(self)

    def create_o2(self, event):
        global n2
        if n2 != 1:
            n2 = 2
        CreateDelete.create_func2(self)

    def create_func3(self):
        global n3, line1_3, line2_3, o3, state3
        if not game_win and not game_tie:
            if n3 == 1:
                line1_3 = canvas3.create_line(0, 0, 245, 245, width=4)
                line2_3 = canvas3.create_line(245, 0, 0, 245, width=4)
                state3 = 'X'
            if n3 == 2:
                o3 = canvas3.create_oval(240, 240, 3, 3, width=4)
                state3 = "O"
            if n3 == 3:
                pass
            a = CheckWinTie()
            a.check_win1()
            a.check_win2()
            a.check_tie()

    def create_x3(self, event):
        global n3
        if n3 != 2:
            n3 = 1
        CreateDelete.create_func3(self)

    def create_o3(self, event):
        global n3
        if n3 != 1:
            n3 = 2
        CreateDelete.create_func3(self)

    def create_func4(self):
        global n4, line1_4, line2_4, o4, state4
        if not game_win and not game_tie:
            if n4 == 1:
                line1_4 = canvas4.create_line(0, 0, 245, 245, width=4)
                line2_4 = canvas4.create_line(245, 0, 0, 245, width=4)
                state4 = 'X'
            if n4 == 2:
                o4 = canvas4.create_oval(240, 240, 3, 3, width=4)
                state4 = "O"
            if n4 == 3:
                pass
            a = CheckWinTie()
            a.check_win1()
            a.check_win2()
            a.check_tie()

    def create_x4(self, event):
        global n4
        if n4 != 2:
            n4 = 1
        CreateDelete.create_func4(self)

    def create_o4(self, event):
        global n4
        if n4 != 1:
            n4 = 2
        CreateDelete.create_func4(self)

    def create_func5(self):
        global n5, line1_5, line2_5, o5, state5
        if not game_win and not game_tie:
            if n5 == 1:
                line1_5 = canvas5.create_line(0, 0, 245, 245, width=4)
                line2_5 = canvas5.create_line(245, 0, 0, 245, width=4)
                state5 = 'X'
            if n5 == 2:
                o5 = canvas5.create_oval(240, 240, 3, 3, width=4)
                state5 = "O"
            if n5 == 3:
                pass
            a = CheckWinTie()
            a.check_win1()
            a.check_win2()
            a.check_tie()

    def create_x5(self, event):
        global n5
        if n5 != 2:
            n5 = 1
        CreateDelete.create_func5(self)

    def create_o5(self, event):
        global n5
        if n5 != 1:
            n5 = 2
        CreateDelete.create_func5(self)

    def create_func6(self):
        global n6, line1_6, line2_6, o6, state6
        if not game_win and not game_tie:
            if n6 == 1:
                line1_6 = canvas6.create_line(0, 0, 245, 245, width=4)
                line2_6 = canvas6.create_line(245, 0, 0, 245, width=4)
                state6 = 'X'
            if n6 == 2:
                o6 = canvas6.create_oval(240, 240, 3, 3, width=4)
                state6 = "O"
            if n6 == 3:
                pass
            a = CheckWinTie()
            a.check_win1()
            a.check_win2()
            a.check_tie()

    def create_x6(self, event):
        global n6
        if n6 != 2:
            n6 = 1
        CreateDelete.create_func6(self)

    def create_o6(self, event):
        global n6
        if n6 != 1:
            n6 = 2
        CreateDelete.create_func6(self)

    def create_func7(self):
        global n7, line1_7, line2_7, o7, state7
        if not game_win and not game_tie:
            if n7 == 1:
                line1_7 = canvas7.create_line(0, 0, 245, 245, width=4)
                line2_7 = canvas7.create_line(245, 0, 0, 245, width=4)
                state7 = 'X'
            if n7 == 2:
                o7 = canvas7.create_oval(240, 240, 3, 3, width=4)
                state7 = "O"
            if n7 == 3:
                pass
            a = CheckWinTie()
            a.check_win1()
            a.check_win2()
            a.check_tie()

    def create_x7(self, event):
        global n7
        if n7 != 2:
            n7 = 1
        CreateDelete.create_func7(self)

    def create_o7(self, event):
        global n7
        if n7 != 1:
            n7 = 2
        CreateDelete.create_func7(self)

    def create_func8(self):
        global n8, line1_8, line2_8, o8, state8
        if not game_win and not game_tie:
            if n8 == 1:
                line1_8 = canvas8.create_line(0, 0, 245, 245, width=4)
                line2_8 = canvas8.create_line(245, 0, 0, 245, width=4)
                state8 = 'X'
            if n8 == 2:
                o8 = canvas8.create_oval(240, 240, 3, 3, width=4)
                state8 = "O"
            if n8 == 3:
                pass
            a = CheckWinTie()
            a.check_win1()
            a.check_win2()
            a.check_tie()

    def create_x8(self, event):
        global n8
        if n8 != 2:
            n8 = 1
        CreateDelete.create_func8(self)

    def create_o8(self, event):
        global n8
        if n8 != 1:
            n8 = 2
        CreateDelete.create_func8(self)

    def create_func9(self):
        global n9, line1_9, line2_9, o9, state9
        if not game_win and not game_tie:
            if n9 == 1:
                line1_9 = canvas9.create_line(0, 0, 245, 245, width=4)
                line2_9 = canvas9.create_line(245, 0, 0, 245, width=4)
                state9 = 'X'
            if n9 == 2:
                o9 = canvas9.create_oval(240, 240, 3, 3, width=4)
                state9 = 'O'
            if n9 == 3:
                pass
            a = CheckWinTie()
            a.check_win1()
            a.check_win2()
            a.check_tie()

    def create_x9(self, event):
        global n9
        if n9 != 2:
            n9 = 1
        CreateDelete.create_func9(self)

    def create_o9(self, event):
        global n9
        if n9 != 1:
            n9 = 2
        CreateDelete.create_func9(self)


def competitive():
    global comp, play1_name, play2_name
    play1_name = player_1_name.get()
    play2_name = player_2_name.get()
    comp = True
    new_win.destroy()


def next_round():
    global score_x_total, score_x1, score_x2, score_x3, score_x4, score_x5, x, round_count
    global score_o_total, score_o1, score_o2, score_o3, score_o4, score_o5, o
    if game_win:
        round_count += 1
        if x:
            if round_count == 1:
                score_x1.set(1)
                score_o1.set(0)
            if round_count == 2:
                score_x2.set(1)
                score_o2.set(0)
            if round_count == 3:
                score_x3.set(1)
                score_o3.set(0)
            if round_count == 4:
                score_x4.set(1)
                score_o4.set(0)
            if round_count == 5:
                score_x5.set(1)
                score_o5.set(0)
        if o:
            if round_count == 1:
                score_o1.set(1)
                score_x1.set(0)
            if round_count == 2:
                score_o2.set(1)
                score_x2.set(0)
            if round_count == 3:
                score_o3.set(1)
                score_x3.set(0)
            if round_count == 4:
                score_o4.set(1)
                score_x4.set(0)
            if round_count == 5:
                score_o5.set(1)
                score_x5.set(0)
        x = False
        o = False
        txtvar2.set("Do you want to go to the next round?")
        yes.set("YES")
        no.set('NO')
    if game_tie:
        txtvar2.set("Do you want to go to the next round?")
        yes.set("YES")
        no.set('NO')


def casual():
    global play1_name, play2_name
    new_win.destroy()
    play1_name = 'X'
    play2_name = "O"


# ___Option window___
new_win = Tk()
frame_top = Canvas(new_win, width=400, height=250, bg='light green')
frame_top.pack()
text_ask = Label(frame_top, text='Do you want to play competitively or casually?', bg='light green')
text_ask.place(anchor='n', width=250, height=30, x=200, y=40)
player_1_name = Entry(frame_top)
player_2_name = Entry(frame_top)
player_1_name.place(anchor='n', height=20, width=140, x=200, y=70)
player_2_name.place(anchor='n', height=20, width=140, x=200, y=100)
labe1 = Label(frame_top, text='Player X name:-', bg='light green')
labe2 = Label(frame_top, text='Player O name:-', bg='light green')
labe1.place(anchor='n', height=20, width=90, x=75, y=70)
labe2.place(anchor='n', height=20, width=90, x=75, y=100)
ask_button1 = Button(frame_top, text='Competitive', command=competitive)
ask_button2 = Button(frame_top, text='Casual', command=casual)
ask_button1.place(anchor='n', width=80, height=25, x=120, y=140)
ask_button2.place(anchor='n', width=80, height=25, x=280, y=140)

new_win.mainloop()
# ___Option window___


# ___main window start___
win = Tk()
win.title("TIC TAC TOE")
win.wm_attributes('-fullscreen', True)
frame1 = Frame(win, height=1080, width=1920, bg='light blue')
frame1.pack()
label1_ = Label(frame1, text="TIC TAC TOE", bg='light green')
label1_.place(anchor='e', height=100, width=200, x=1050, y=100)
txtvar1 = StringVar()
label2_ = Label(frame1, textvariable=txtvar1)
label2_.place(anchor='e', height=30, width=200, x=1050, y=970)
txtvar2 = StringVar()
label3_ = Label(frame1, textvariable=txtvar2, bg='light blue')
label3_.place(anchor='e', height=30, width=200, x=1700, y=500)

button_exit = Button(frame1, text='Exit', command=exit_1, bg='crimson', fg='light blue')
button_exit.place(height=25, width=65, x=1700, y=990)
yes = StringVar()
no = StringVar()
button_repeat1 = Button(frame1, textvariable=yes, relief='flat', bg='light blue', command=yes_func)
button_repeat1.place(anchor='e', height=25, width=65, x=1570, y=550)
button_repeat2 = Button(frame1, textvariable=no, relief='flat', bg='light blue')
button_repeat2.place(anchor='e', height=25, width=65, x=1695, y=550)

player1_var = StringVar()
player2_var = StringVar()
player1_var.set(play1_name + ' (X)')
player2_var.set(play2_name + ' (O)')

score_x1 = StringVar()
score_x2 = StringVar()
score_x3 = StringVar()
score_x4 = StringVar()
score_x5 = StringVar()

score_o1 = StringVar()
score_o2 = StringVar()
score_o3 = StringVar()
score_o4 = StringVar()
score_o5 = StringVar()

p = CreateDelete()

# ___ spots ___
canvas = Canvas(frame1, bg='red')
canvas.place(anchor='n', width=735, height=735, x=960, y=200)

canvas1 = Canvas(frame1, bg='grey')
canvas1.place(anchor='n', width=245, height=245, x=715, y=200)
canvas1.bind('<Button-1>', p.create_x1)
canvas1.bind('<Button-3>', p.create_o1)

canvas2 = Canvas(frame1, bg='grey')
canvas2.place(anchor='n', width=245, height=245, x=960, y=200)
canvas2.bind('<Button-1>', p.create_x2)
canvas2.bind('<Button-3>', p.create_o2)

canvas3 = Canvas(frame1, bg='grey')
canvas3.place(anchor='n', width=245, height=245, x=1205, y=200)
canvas3.bind('<Button-1>', p.create_x3)
canvas3.bind('<Button-3>', p.create_o3)

canvas4 = Canvas(frame1, bg='grey')
canvas4.place(anchor='n', width=245, height=245, x=715, y=445)
canvas4.bind('<Button-1>', p.create_x4)
canvas4.bind('<Button-3>', p.create_o4)

canvas5 = Canvas(frame1, bg='grey')
canvas5.place(anchor='n', width=245, height=245, x=960, y=445)
canvas5.bind('<Button-1>', p.create_x5)
canvas5.bind('<Button-3>', p.create_o5)

canvas6 = Canvas(frame1, bg='grey')
canvas6.place(anchor='n', width=245, height=245, x=1205, y=445)
canvas6.bind('<Button-1>', p.create_x6)
canvas6.bind('<Button-3>', p.create_o6)

canvas7 = Canvas(frame1, bg='grey')
canvas7.place(anchor='n', width=245, height=245, x=715, y=690)
canvas7.bind('<Button-1>', p.create_x7)
canvas7.bind('<Button-3>', p.create_o7)

canvas8 = Canvas(frame1, bg='grey')
canvas8.place(anchor='n', width=245, height=245, x=960, y=690)
canvas8.bind('<Button-1>', p.create_x8)
canvas8.bind('<Button-3>', p.create_o8)

canvas9 = Canvas(frame1, bg='grey')
canvas9.place(anchor='n', width=245, height=245, x=1205, y=690)
canvas9.bind("<Button-3>", p.create_o9)
canvas9.bind('<Button-1>', p.create_x9)


def score_board_func():
    global comp
    if comp:
        comp = True
        # ___Score Board___
        score_board_can = Canvas(frame1, bg='light blue')
        score_board_can.place(anchor='n', width=200, height=510, x=300, y=250)
        player_name_rect = score_board_can.create_rectangle(3, 3, 197, 57)
        player_divider = score_board_can.create_line(100, 0, 100, 600)
        score_divider1 = score_board_can.create_line(0, 150, 200, 150)
        score_divider2 = score_board_can.create_line(0, 240, 200, 240)
        score_divider3 = score_board_can.create_line(0, 330, 200, 330)
        score_divider4 = score_board_can.create_line(0, 420, 200, 420)

        player_1 = Label(score_board_can, textvariable=player1_var, bg='light blue')
        player_2 = Label(score_board_can, textvariable=player2_var, bg='light blue')

        player_1.place(anchor='n', height=30, width=90, x=50, y=15)
        player_2.place(anchor='n', height=30, width=90, x=150, y=15)

        sc_x1 = Label(score_board_can, bg='light blue', textvariable=score_x1)
        sc_x2 = Label(score_board_can, bg='light blue', textvariable=score_x2)
        sc_x3 = Label(score_board_can, bg='light blue', textvariable=score_x3)
        sc_x4 = Label(score_board_can, bg='light blue', textvariable=score_x4)
        sc_x5 = Label(score_board_can, bg='light blue', textvariable=score_x5)

        sc_x1.place(anchor='n', height=30, width=90, x=50, y=90)
        sc_x2.place(anchor='n', height=30, width=90, x=50, y=180)
        sc_x3.place(anchor='n', height=30, width=90, x=50, y=270)
        sc_x4.place(anchor='n', height=30, width=90, x=50, y=360)
        sc_x5.place(anchor='n', height=30, width=90, x=50, y=450)

        sc_o1 = Label(score_board_can, bg='light blue', textvariable=score_o1)
        sc_o2 = Label(score_board_can, bg='light blue', textvariable=score_o2)
        sc_o3 = Label(score_board_can, bg='light blue', textvariable=score_o3)
        sc_o4 = Label(score_board_can, bg='light blue', textvariable=score_o4)
        sc_o5 = Label(score_board_can, bg='light blue', textvariable=score_o5)

        sc_o1.place(anchor='n', height=30, width=90, x=150, y=90)
        sc_o2.place(anchor='n', height=30, width=90, x=150, y=180)
        sc_o3.place(anchor='n', height=30, width=90, x=150, y=270)
        sc_o4.place(anchor='n', height=30, width=90, x=150, y=360)
        sc_o5.place(anchor='n', height=30, width=90, x=150, y=450)


score_board_func()

win.mainloop()
# ___main window end___
