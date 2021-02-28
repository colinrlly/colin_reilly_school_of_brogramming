class Calculator:
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

calc = Calculator()
num1 = 3
num2 = 4

print(calc.summ(num1, num2))
print(calc.diff(num1, num2))
print(calc.prod(num1, num2))
print(calc.quot(num1, num2))
