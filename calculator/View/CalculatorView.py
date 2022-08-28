from ast import operator
from multiprocessing.dummy import active_children
from tkinter import *
from tkinter import ttk
from VO import NumberVO
from VO.OperatorVO import OperatorVO
from Business import Calculator

class CalculatorView():
    NUM_START_ROW = 4
    
    def __init__(self):
        print('CalculatorView.__init__()')
        self._init_default_value()
        self._render_calculator()

    def _init_default_value(self):
        print('CalculatorView._init_default_value()')
        self.passiveNum = ''
        self.operator = ''
        self.activeNum = ''
        self.result = ''
        self.numberBtnList = []
        self.numberList = []
        self.operator = None
        self.operator_click = False
        self.calc = Calculator.Calculator()

    def _render_calculator(self):
        root = Tk()
        frame = ttk.Frame(root, padding=10)
        frame.grid()
        
        self._make_calculator_frame(frame)
        self._make_number_btn(frame)
        self._make_operator_btn(frame)
        
        frame.focus_set()
        root.mainloop()

    def _make_calculator_frame(self, frame):
        self.displayRecordEntry = ttk.Entry(frame)
        self.displayRecordEntry.grid(row=1, column=2, columnspan=3)
        self.displayInputEntry = ttk.Entry(frame)
        self.displayInputEntry.grid(row=2, column=2, columnspan=3)
        returnBtn = ttk.Button(
            frame, text='=',
            command=lambda: self._on_return_pressed()
        )
        returnBtn.grid(row=8, column=3)
        
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
        print('_make_operand_list()')
        self.numberList.append(number)
    
    def _allocate_number_variable(self, number):
        print('_allocate_number_variabel()')
        if self.operator_click:
            self.activeNum = number
        else:
            self.passiveNum = number

    def _allocate_operator_variable(self, operator):
        self.operator = OperatorVO(operator = operator).getOperator()

    def _on_number_selected_event(self, number):
        print('_on_number_selected_event()')
        if number == str(0) and (len(self.numberList) == 0 or len(self.numberList) == 0):
            return
        self._make_operand_list(number)
        strNum = self._change_list_to_number(self.numberList)
        self._allocate_number_variable(strNum)
        self._display_selected_btn()
        
    def _on_operator_selected_event(self, operator):
        self.operator_click = True
        self._allocate_operator_variable(operator)
        self.numberList = []
        endNumIndex = self.displayInputEntry.get()
        recordStr = f"{self.displayInputEntry.get()} {self.operator}"
        self.displayRecordEntry.insert(0, recordStr)
        self.displayInputEntry.delete(0, len(self.displayInputEntry.get()))
        
    def _on_key_press(self, event):
        operatorList = ('+', '-', '*', '/')
        pressed_key = event.char
        if event.keysym == 'Return':
            self._on_return_pressed()
        elif pressed_key not in operatorList:
            self._on_number_selected_event(pressed_key)
        else:
            self._on_operator_selected_event(pressed_key)

    def _display_selected_btn(self):
        print('_display_selected_btn()')
        if self.operator_click:
            displayNum = self.activeNum
        else:
            displayNum = self.passiveNum

        print(f"displayNum: {displayNum}")
        self.displayInputEntry.delete(0, len(self.displayInputEntry.get()))
        self.displayInputEntry.insert(0, displayNum)
        
    def _change_list_to_number(self, list):
        result = ''
        for char in list:
            result += str(char)
        return result
    
    def _on_return_pressed(self):
        self._calc_result()
    
    def _calc_result(self):
        self.result = self.calc.calculate(
            passiveNum = self.passiveNum,
            activeNum = self.activeNum,
            operator = self.operator
        )
        print(self.result)