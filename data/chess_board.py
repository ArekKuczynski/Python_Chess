from tkinter import *

class Board():
    def __init__(self, master, menu_obj):
        self.master = master
        self.menu = menu_obj #menu object
        self.build_board()
        self.build_widgets()
        
    def build_board(self):
        self.master.title("Chess")
        self.master.geometry("800x900")
        self.master.resizable(False, False)
        
    def build_widgets(self):
        self.build_frames()
        self.build_buttons()
        #self.build_labels()
        
    def build_frames(self):
        self.frame_top = Frame(self.master, width=800, height=100, background='brown')
        self.frame_top.grid_propagate(0)
        self.frame_top.grid(row=0, column=0) 
        
        self.frame_bot = Frame(self.master, width=800, height=800, background='red')
        self.frame_bot.grid_propagate(0)
        self.frame_bot.grid(row=1, column=0) 
        
        self.frame_num_top = Frame(self.frame_bot, width=720, height=40, background='blue')
        self.frame_num_top.grid_propagate(0)
        self.frame_num_top.grid(row=0, column=0)
        
        self.frame_board = Frame(self.frame_bot, width=800, height=720, background='white')
        self.frame_board.grid_propagate(0)
        self.frame_board.grid(row=1, column=0) 
        
        self.frame_num_bot = Frame(self.frame_bot, width=720, height=40, background='blue')
        self.frame_num_bot.grid_propagate(0)
        self.frame_num_bot.grid(row=2, column=0)
        
        def build_frames_inside():
            self.frame_num_left = Frame(self.frame_board, width=40, height=720, background='blue')
            self.frame_num_left.grid_propagate(0)
            self.frame_num_left.grid(row=0, column=0)
            
            self.frame_main = Frame(self.frame_board, width=720, height=720, background='white')
            self.frame_main.grid_propagate(0)
            self.frame_main.grid(row=0, column=1) 
            
            self.frame_num_right = Frame(self.frame_board, width=40, height=720, background='blue')
            self.frame_num_right.grid_propagate(0)
            self.frame_num_right.grid(row=0, column=2)
            
        build_frames_inside()   

        def build_frames_num():
            list1 = ["a","b","c","d","e","f","g","h"]
            list2 = ["8","7","6","5","4","3","2","1"]
            for i in range(0,8):
                
                self.frame = Frame(self.frame_num_bot, width=90, height=40, background='gray')
                self.frame.grid_propagate(0)
                self.frame.grid(row=0, column=i)

                self.label = Label(self.frame, text=list1[i])
                self.label.grid_propagate(0)
                self.label.grid(row=0, column=0)
            for i in range(0,8):
                
                self.frame = Frame(self.frame_num_left, width=40, height=90, background='gray')
                self.frame.grid_propagate(0)
                self.frame.grid(row=i, column=0)

                self.label = Label(self.frame, text=list2[i])
                self.label.grid_propagate(0)
                self.label.grid(row=0, column=0)
                
        build_frames_num()
        
    def back_menu(self):
        self.master.destroy()
        self.menu.deiconify()
        
    def build_buttons(self):
        self.button_exit = Button(self.frame_top, text='Back to menu', width=16, command=self.back_menu)
        self.button_exit.grid(row=0, column=0, padx=40, pady=30)
        