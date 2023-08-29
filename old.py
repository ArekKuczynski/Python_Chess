from tkinter import *

import data.chess_board as board


def build_menu():
    menu = Tk()
    menu.title("Chess")
    menu.geometry("300x600")
    
    frame = Frame(menu,width=200,height=400,bg="blue").pack()
    
    def move_to_board():
        menu.withdraw()
        board.build()
    
    play = Button(frame, text="Play Chess", command=move_to_board, fg="black").pack()
    exit = Button(frame, text="Exit game", command=menu.destroy, fg="black").pack()

    menu.mainloop()
build_menu()