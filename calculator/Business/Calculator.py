class Calculator():
    def __init__(self):
        print('Calculator.__init__()')
        self.passiveNumber = None
        self.activeNumber = None
        self.operator = None
        self.result = None
        self.operateDict = {
            'add':self._operate_add,
            'minus':self._opearate_minus,
            'multiply':self._operate_multiply,
            'divide':self._operate_divide
        }
    
    def _set_data(self, param):
        print('Calculator._set_data()')
        self.passiveNumber = param.get('passiveNum')
        self.activeNumber = param.get('activeNum')
        self.operator = self._change_symbol_to_string(param.get('operator'))

    def calculate(self, **param):
        print('Calculator.calculate()')
        self._set_data(param)
        return self.operateDict(self.operator)
        
    def _operate_add(self):
        return self.passiveNumber + self.activeNumber

    def _opearate_minus(self):
        return self.passiveNumber - self.activeNumber
    
    def _operate_multiply(self):
        return self.passiveNumber * self.activeNumber
    
    def _operate_divide(self):
        return self.passiveNumber / self.activeNumber
    
    def _change_symbol_to_string(self, symbol):
        if symbol == '+':
            return 'add'
        elif symbol == '-':
            return 'minus'
        elif symbol == '*':
            return 'multiply'
        else:
            return 'divide'