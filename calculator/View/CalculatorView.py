from tkinter import *
from tkinter import ttk
from VO import NumberVO
from VO.OperatorVO import OperatorVO

class CalculatorView():
    NUM_START_ROW = 3
    
    def __init__(self):
        print('CalculatorView.__init__()')
        self._init_default_value()
        self._render_calculator()

    def _init_default_value(self):
        self.passiveNum = None
        self.operator = None
        self.activeNum = None
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
        
        root.mainloop()
    
    def _make_calculator_frame(self, root, frame):
        displayRecordEntry = ttk.Entry(frame)
        displayRecordEntry.grid(row=1, column=2, columnspan=2)
        displayInputEntry = ttk.Entry(frame)
        displayInputEntry.grid(row=2, column=2, columnspan=2)
        closeBtn = ttk.Button(frame, text='Close', command = root.destroy)
        closeBtn.grid(row=11, column=3)
        
    def _make_number_btn(self, frame):
        for number in range(0, 9):
            globals()[f"numberBtn{number + 1}"] = None
            self.numberBtnList.append(f"numberBtn{number + 1}")
            self._make_1_to_9_btn(frame, self.numberBtnList[number], number)
                        
        zeroBtn = ttk.Button(
            frame, text = 0,
            command=lambda: self._on_number_btn_click_event(0)
        )
        zeroBtn.grid(row = 5, column = 2)

    def _make_1_to_9_btn(self, frame, btn, number):
        btn = ttk.Button(
            frame, text=number + 1,
            command=lambda: self._on_number_btn_click_event(number + 1)
        )
        btn.grid(
            row=int(number / 3) + self.NUM_START_ROW, column=(number % 3)
        )

    def _make_operator_btn(self, frame):
        divideBtn = ttk.Button(
            frame, text = '/',
            command=lambda: self._on_operator_btn_click_event('/')
        )
        divideBtn.grid(row=self.NUM_START_ROW - 1, column=3)
        
        multiflyBtn = ttk.Button(
            frame, text = 'X',
            command=lambda: self._on_operator_btn_click_event('X')
        )
        multiflyBtn.grid(row=self.NUM_START_ROW, column=3)
        
        plusBtn = ttk.Button(
            frame, text = '+',
            command=lambda: self._on_operator_btn_click_event('+')
        )
        plusBtn.grid(row=self.NUM_START_ROW + 1, column=3)
        
        minusBtn = ttk.Button(
            frame, text = '-',
            command=lambda: self._on_operator_btn_click_event('-')
        )
        minusBtn.grid(row=self.NUM_START_ROW + 2, column=3)
        
        braketBtn = ttk.Button(
            frame, text = '()',
            command=lambda: self._on_operator_btn_click_event('()')
        )
        braketBtn.grid(row=self.NUM_START_ROW - 1, column=2)
        
    def _make_operand_list(self, number):
        if self.operator_click is False:
            self.passiveNumList.append(number)
        else:
            self.activeNumList.append(number)
        print(f"self.passiveNumList: {self.passiveNumList}")
        print(f"self.activeNumList:  {self.activeNumList}")

    def _allocate_operator_variable(self, operator):
        self.operator = OperatorVO(operator = operator).getOperator()

    def _on_number_btn_click_event(self, number):
        self._make_operand_list(number)
        self._display_selected_btn(number)
        
    def _on_operator_btn_click_event(self, operator):
        self.operator_click = True
        self._allocate_operator_variable(operator)
        self._display_selected_btn(operator)

    def _display_selected_btn(self, btnText):
        print(f"displayBtn: {btnText}")
        
        