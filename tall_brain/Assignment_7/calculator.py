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
        c1 = parsed_prob[0]
        if c1.isnumeric():
            c1 = int(c1)
        c2 = parsed_prob[2]
        if c2.isnumeric():
            c2 = int(c2)
        o = parsed_prob[1]
        if o == "+":
            return self.add(c1, c2)
        elif o == "-":
            return self.sub(c1, c2)
        elif o == "*":
            return self.mul(c1, c2)
        elif o == "/":
            return self.div(c1, c2)


calc = calculator()

result = calc.calculate("422 * 232")

print(result)
