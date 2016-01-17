class Sudoku_Gui(object):
    """docstring for SudokuGui"""
    def __init__(self, arg):
        super(SudokuGui, self).__init__()
        self.arg = arg
  
# import sys
# import os.path

# sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


import tkinter as tk
import Sudoku_Player as sp
root = tk.Tk()

table = sp.Sudoku_Table(root)
table.grid()
table.set_visibility(True)


vsblty_btn = tk.Button

root.mainloop()
