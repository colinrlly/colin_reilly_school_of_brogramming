
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

calc =  calculator()

print(calc.add(4, 5))
print(calc.sub(4, 5))
print(calc.mul(4, 5))
print(calc.div(4, 5))
