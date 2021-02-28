class calculator:
    def add(self, x, y):
        ans = x + y
        return ans

    def sub(self, x, y):
        ans = x - y
        return ans

    def mul(self, x, y):
        ans = x * y
        return ans

    def div(self, x, y):
        ans = x / y
        return ans

    def calculate(self, prob):
        parsed_prob = prob.split()
        for c in parsed_prob:
            if c.isnumeric():
                int(c)
            else:
                if c == "+":
                    self.add(int(c))
                elif c == "-":
                    self.sub(int())
                elif c == "*":
                    self.mul(int())
                elif c == "/":
                    self.div(int())




calc = calculator()

calc.calculate("5 + 4")


# print(calc.add(4, 5))
# print(calc.sub(4, 5))
# print(calc.mul(4, 5))
# print(calc.div(4, 5))
