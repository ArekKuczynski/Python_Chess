from tkinter import *

import data.chess_board as board_module

class MainApp(Frame):
    def __init__(self, main_menu):
        self.main_menu = main_menu
        #Frame.__init__(self, self.master)
        
        self.build_menu()
        self.build_widgets()

    def build_menu(self):
        self.main_menu.title('Chess Menu')
        self.main_menu.geometry('300x600')
        self.main_menu.resizable(False, False)

    def build_widgets(self):
        self.build_frames()
        self.build_buttons()

    def build_frames(self):
        self.frame1 = Frame(self.main_menu, width=300, height=600, background='red')
        self.frame1.grid_propagate(0)
        self.frame1.grid(row=0, column=0)
        
        self.frame = Frame(self.frame1, width=200, height=600, background='brown')
        self.frame.grid_propagate(0)
        self.frame.grid(row=0, column=0, padx=50) 

    def build_buttons(self):
        self.build_frame_buttons()       

    def move_to_board(self):
        menu.withdraw()
        
        board = Tk()
        b = board_module.Board(board,menu)
        board.mainloop()
        
    def build_frame_buttons(self):
        self.button1 = Button(self.frame, text='Play Chess', command=self.move_to_board, width=16)      
        self.button1.grid(row=0, column=0, padx=40, pady=30)

        self.button2 = Button(self.frame, text='Exit game', command=menu.destroy ,width=16)       
        self.button2.grid(row=1, column=0, padx=40, pady=30)       


if __name__ == '__main__':
    menu = Tk()
    main_app = MainApp(menu)
    menu.mainloop()