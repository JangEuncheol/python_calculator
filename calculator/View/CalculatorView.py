from tkinter import *
from tkinter import ttk

class CalculatorView():
    def __init__(self):
        print('CalculatorView.__init__()')
        self._render_calculator()

    def _render_calculator(self):
        root = Tk()
        frame = ttk.Frame(root, padding=10)
        frame.grid()
        
        titleLabel = ttk.Label(frame, text='PyCalc')
        titleLabel.grid(row=0, column=0)
        
        closeBtn = ttk.Button(frame, text='Close', command = root.destroy)
        closeBtn.grid(row = 10, column = 4)
        
        root.mainloop()

    def _display_selected_number(self):
        pass


    