#panggil semua library yang dibutuhin
from tkinter import *
import tkinter.messagebox

#deklarasi tkinter
tk = Tk()
tk.title("Tic Tac Toe")

pa = StringVar()
pb = StringVar()
p1 = StringVar()
p2 = StringVar()

player1_nama = Entry(tk,font = "Times 20 bold", textvariable=p1, bd=5)
player1_nama.grid(row = 1, column = 1, columnspan = 8)
player2_nama = Entry(tk,font = "Times 20 bold", textvariable=p2, bd=5)
player2_nama.grid(row = 2, column = 1, columnspan = 8)

bClick = True
flag = 0

def disableButton():
    button1.configure(state = DISABLED)
    button2.configure(state = DISABLED)
    button3.configure(state = DISABLED)
    button4.configure(state = DISABLED)
    button5.configure(state = DISABLED)
    button6.configure(state = DISABLED)
    button7.configure(state = DISABLED)
    button8.configure(state = DISABLED)
    button9.configure(state = DISABLED)

def btnClick(buttons):
    global bClick, flag, player1_nama, player2_nama, pa, pb
    if buttons["text"] == " " and bClick == True :
        buttons["text"] = "X"
        bClick = False
        pa = p1.get() + "Menang !"
        pb = p2.get() + "Menang !"
        checkWin()
        flag += 1

    elif buttons["text"] == " " and bClick == False :
        buttons["text"] = "O"
        bClick = True
        checkWin()
        flag += 1

    else :
        tkinter.messagebox.showinfo("Tic Tac Toe", "Kotak Sudah Terisi!!")

def checkWin():
    if (button1["text"] == "X" and button2["text"] == "X" and button3["text"] == "X" or
        button4["text"] == "X" and button5["text"] == "X" and button6["text"] == "X" or
        button7["text"] == "X" and button8["text"] == "X" and button9["text"] == "X" or
        button1["text"] == "X" and button4["text"] == "X" and button7["text"] == "X" or
        button2["text"] == "X" and button5["text"] == "X" and button8["text"] == "X" or
        button3["text"] == "X" and button6["text"] == "X" and button9["text"] == "X" or
        button1["text"] == "X" and button5["text"] == "X" and button9["text"] == "X" or
        button3["text"] == "X" and button5["text"] == "X" and button7["text"] == "X" ):
        disableButton()
        tkinter.messagebox.showinfo("Tic Tac Toe", pa)

    elif (button1["text"] == "O" and button2["text"] == "O" and button3["text"] == "O" or
        button4["text"] == "O" and button5["text"] == "O" and button6["text"] == "O" or
        button7["text"] == "O" and button8["text"] == "O" and button9["text"] == "O" or
        button1["text"] == "O" and button4["text"] == "O" and button7["text"] == "O" or
        button2["text"] == "O" and button5["text"] == "O" and button8["text"] == "O" or
        button3["text"] == "O" and button6["text"] == "O" and button9["text"] == "O" or
        button1["text"] == "O" and button5["text"] == "O" and button9["text"] == "O" or
        button3["text"] == "O" and button5["text"] == "O" and button7["text"] == "O" ):
        disableButton()
        tkinter.messagebox.showinfo("Tic Tac Toe", pb)

    elif (flag == 8):
        tkinter.messagebox.showinfo("Tic Tac Toe", "Game Seri!")

buttons = StringVar()

label = Label(tk, text = "Player 1", font = "Times 20 bold", bg = "white", fg = "black", height = 1, width = 8)
label.grid(row = 1, column = 0)

label = Label(tk, text = "Player 2", font = "Times 20 bold", bg = "white", fg = "black", height = 1, width = 8)
label.grid(row = 2, column = 0)

button1 = Button(tk, text = " ", font = "Times 20 bold", bg = "grey", fg = "white", height = 4, width = 8, command = lambda:btnClick(button1))
button1.grid(row = 3, column = 0)

button2 = Button(tk, text = " ", font = "Times 20 bold", bg = "grey", fg = "white", height = 4, width = 8, command = lambda:btnClick(button2))
button2.grid(row = 3, column = 1)

button3 = Button(tk, text = " ", font = "Times 20 bold", bg = "grey", fg = "white", height = 4, width = 8, command = lambda:btnClick(button3))
button3.grid(row = 3, column = 2)

button4 = Button(tk, text = " ", font = "Times 20 bold", bg = "grey", fg = "white", height = 4, width = 8, command = lambda:btnClick(button4))
button4.grid(row = 4, column = 0)

button5 = Button(tk, text = " ", font = "Times 20 bold", bg = "grey", fg = "white", height = 4, width = 8, command = lambda:btnClick(button5))
button5.grid(row = 4, column = 1)

button6 = Button(tk, text = " ", font = "Times 20 bold", bg = "grey", fg = "white", height = 4, width = 8, command = lambda:btnClick(button6))
button6.grid(row = 4, column = 2)

button7 = Button(tk, text = " ", font = "Times 20 bold", bg = "grey", fg = "white", height = 4, width = 8, command = lambda:btnClick(button7))
button7.grid(row = 5, column = 0)

button8 = Button(tk, text = " ", font = "Times 20 bold", bg = "grey", fg = "white", height = 4, width = 8, command = lambda:btnClick(button8))
button8.grid(row = 5, column = 1)

button9 = Button(tk, text = " ", font = "Times 20 bold", bg = "grey", fg = "white", height = 4, width = 8, command = lambda:btnClick(button9))
button9.grid(row = 5, column = 2)

#menampilkan hasil GUI di Desktop
tk.mainloop()