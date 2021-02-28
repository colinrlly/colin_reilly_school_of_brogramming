class Calculator:
    numBuffer = []
    symBuffer = []
    validSymbols = {"+", "-", "*", "/"}

    def __init__(self):
        pass

    def summ(self, a, b):
        return a + b

    def diff(self, a, b):
        return a - b

    def prod(self, a, b):
        return a * b

    def quot(self, a, b):
        if b == 0:
            return "undefined"
        return a / b
    
    def clearBuffers(self):
        self.numBuffer.clear()
        self.symBuffer.clear()

    def calculate(self, inputStr=""):
        # Print error if no input provided
        if inputStr == "":
            print("ERROR: no input provided")
            return

        # Add all numbers to `numBuffer` and symbols to `symBuffer`
        for char in inputStr:
            if char.isnumeric():
                self.numBuffer.append(char)
                continue
            if char in self.validSymbols:
                self.symBuffer.append(char)

        # If invalid quantity of numbers or symbols, print error
        if len(self.numBuffer) != 2:
            print("ERROR: invalid quantity of numbers provided")
            self.clearBuffers()
            return
        if len(self.symBuffer) != 1:
            print("ERROR: invalid quantity of symbols provided")
            self.clearBuffers()
            return

        # Map each valid symbol to a respective Calculator function
        symbolToFuncMap = {
            "+": self.summ,
            "-": self.diff,
            "*": self.prod,
            "/": self.quot,
        }

        # Call the symBuffer's mapped function with the contents of numBuffer
        ret = symbolToFuncMap[self.symBuffer[0]](
            int(self.numBuffer[0]), int(self.numBuffer[1])
        )

        self.clearBuffers()
        return ret


calc = Calculator()

print(calc.calculate("4 + 5"))
print(calc.calculate("4- 5"))
print(calc.calculate("4 *5"))
print(calc.calculate("4/5"))
