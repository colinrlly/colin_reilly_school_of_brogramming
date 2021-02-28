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
                c_1 = int(c)
                c_2 = int(c)
#get variables into proper locations (they get overwritten -> 5 fills both then 4 replaces 5 in both)
            else:
                if c == "+":
                    return self.add(c_1, c_2)
                elif c == "-":
                    return self.sub(c_1, c_2)
                elif c == "*":
                    return self.mul(c_1, c_2)
                elif c == "/":
                    return self.div(c_1, c_2)
                    
        
#c_1 and c_2 do not contain proper information (4 and 5) when self.add are called
#return statement is scuffed



calc = calculator()

result = calc.calculate("5 + 4")

print(result)

# print(calc.add(4, 5))
# print(calc.sub(4, 5))
# print(calc.mul(4, 5))
# print(calc.div(4, 5))
