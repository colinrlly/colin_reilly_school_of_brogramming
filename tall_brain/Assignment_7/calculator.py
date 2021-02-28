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
        for c1 in parsed_prob[0:2]:
            if c1.isnumeric():
                c1 = int(c1)
        for c2 in parsed_prob[2:5]:
            if c2.isnumeric():
                c2 = int(c2)
        for o in parsed_prob[2:3]:
            if o == "+":
                return self.add(c1, c2)
            elif o == "-":
                return self.sub(c1, c2)
            elif o == "*":
                return self.mul(c1, c2)
            elif o == "/":
                return self.div(c1, c2)

                

# #get variables into proper locations (they get overwritten -> 5 fills both then 4 replaces 5 in both)
#             else:
#                 
                    
        
#c_1 and c_2 do not contain proper information (4 and 5) when self.add are called
#return statement is scuffed



calc = calculator()

result = calc.calculate("5 + 4")

print(result)

# print(calc.add(4, 5))
# print(calc.sub(4, 5))
# print(calc.mul(4, 5))
# print(calc.div(4, 5))
