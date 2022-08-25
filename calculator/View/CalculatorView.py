from tkinter import *
from tkinter import ttk
from VO import NumberVO
from VO.OperatorVO import OperatorVO

class CalculatorView():
    NUM_START_ROW = 4
    
    def __init__(self):
        print('CalculatorView.__init__()')
        self._init_default_value()
        self._render_calculator()

    def _init_default_value(self):
        self.passiveNum = ''
        self.operator = ''
        self.activeNum = ''
        self.numberBtnList = []
        self.passiveNumList = []
        self.activeNumList = []
        self.operator = None
        self.operator_click = False

    def _render_calculator(self):
        root = Tk()
        frame = ttk.Frame(root, padding=10)
        frame.grid()
        
        self._make_calculator_frame(root, frame)
        self._make_number_btn(frame)
        self._make_operator_btn(frame)
        
        frame.focus_set()
        root.mainloop()
    

    def _make_calculator_frame(self, root, frame):
        self.displayRecordEntry = ttk.Entry(frame)
        self.displayRecordEntry.grid(row=1, column=2, columnspan=3)
        self.displayInputEntry = ttk.Entry(frame)
        self.displayInputEntry.grid(row=2, column=2, columnspan=3)
        closeBtn = ttk.Button(frame, text='Close', command = root.destroy)
        closeBtn.grid(row=8, column=3)
        
        self._bind_event(frame)

    def _bind_event(self, frame):
        frame.bind('<Key>', self._on_key_press)
        
    def _make_number_btn(self, frame):
        for number in range(0, 9):
            globals()[f"numberBtn{number + 1}"] = None
            self.numberBtnList.append(f"numberBtn{number + 1}")
            self._make_1_to_9_btn(frame, self.numberBtnList[number], number)
                        
        zeroBtn = ttk.Button(
            frame, text = 0,
            command=lambda: self._on_number_selected_event(0)
        )
        zeroBtn.grid(row = 7, column = 2)
        # zeroBtn.bind('<Button-1>',lambda: self._on_number_selected_event(0))

    def _make_1_to_9_btn(self, frame, btn, number):
        btn = ttk.Button(
            frame, text=number + 1,
            command=lambda: self._on_number_selected_event(number + 1)
        )
        btn.grid(
            row=int(number / 3) + self.NUM_START_ROW, column=(number % 3)
        )

    def _make_operator_btn(self, frame):
        divideBtn = ttk.Button(
            frame, text = '/',
            command=lambda: self._on_operator_selected_event('/')
        )
        divideBtn.grid(row=self.NUM_START_ROW - 1, column=3)
        
        multiflyBtn = ttk.Button(
            frame, text = 'X',
            command=lambda: self._on_operator_selected_event('X')
        )
        multiflyBtn.grid(row=self.NUM_START_ROW, column=3)
        
        plusBtn = ttk.Button(
            frame, text = '+',
            command=lambda: self._on_operator_selected_event('+')
        )
        plusBtn.grid(row=self.NUM_START_ROW + 1, column=3)
        
        minusBtn = ttk.Button(
            frame, text = '-',
            command=lambda: self._on_operator_selected_event('-')
        )
        minusBtn.grid(row=self.NUM_START_ROW + 2, column=3)
        
        # braketBtn = ttk.Button(
        #     frame, text = '()',
        #     command=lambda: self._on_operator_btn_click_event('()')
        # )
        # braketBtn.grid(row=self.NUM_START_ROW - 1, column=2)
        
    def _make_operand_list(self, number):
        if self.operator_click is False:
            self.passiveNumList.append(number)
        else:
            self.activeNumList.append(number)

    def _allocate_operator_variable(self, operator):
        self.operator = OperatorVO(operator = operator).getOperator()

    def _on_number_selected_event(self, number):
        self._make_operand_list(number)
        self._display_selected_btn()
        
    def _on_operator_selected_event(self, operator):
        self.operator_click = True
        self._allocate_operator_variable(operator)
        endNumIndex = self.displayInputEntry.get()
        recordStr = f"{self.displayInputEntry.get()} {self.operator}"
        self.displayRecordEntry.insert(0, recordStr)
        self.displayInputEntry.delete(0, len(self.displayInputEntry.get()))
        
    def _on_key_press(self, event):
        operatorList = ('+', '-', '*', '/')
        pressed_key = event.char
        if pressed_key not in operatorList:
            self._on_number_selected_event(pressed_key)
        else:
            self._on_operator_selected_event(pressed_key)

    def _display_selected_btn(self):
        if self.operator_click == False:
            displayNum = self._change_list_to_number(self.passiveNumList)
        else:
            displayNum = self._change_list_to_number(self.activeNumList)

        print(f"displayNum: {displayNum}")
        self.displayInputEntry.delete(0, len(self.displayInputEntry.get()))
        self.displayInputEntry.insert(0, displayNum)
        
    def _change_list_to_number(self, list):
        result = self.passiveNum if self.operator_click is False else self.activeNum
        for char in list:
            result += str(char)
        return result
    