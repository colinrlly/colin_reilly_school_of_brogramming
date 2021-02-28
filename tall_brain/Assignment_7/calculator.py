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
        for c1 in parsed_prob[0]:
            if c1.isnumeric():
                c1 = int(c1)
        for c2 in parsed_prob[2]:
            if c2.isnumeric():
                c2 = int(c2)
        for o in parsed_prob[1]:
            if o == "+":
                return self.add(c1, c2)
            elif o == "-":
                return self.sub(c1, c2)
            elif o == "*":
                return self.mul(c1, c2)
            elif o == "/":
                return self.div(c1, c2)


calc = calculator()

result = calc.calculate("2 - 3")

print(result)
