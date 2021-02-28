import re
import sys

class Calculator:
    OPS = ()
    def __init__(self):
        self.OPS = {
            '/': self.div,
            '*': self.mul,
            '-': self.sub,
            '+': self.add
        }


    def calculate(self, equation: str) -> float:
        nq = []
        oq = []

        ops = ''.join(self.OPS.keys())
        l = re.split(r'\s|([\/*+\-\(\)])', equation)
        eq_arr = [i for i in l if i != '' and i is not None]

        i = 0
        while i < len(eq_arr):
            x = eq_arr[i]
            # process parentheses
            if x == '(':
                start = i+1
                end = eq_arr.index(')', start)

                nq.append(self.calculate(' '.join(eq_arr[start:end])))
                i = end
            elif x not in self.OPS:
                nq.append(float(x))
            elif x in self.OPS:
                oq.append(x)

            i += 1
        
        for op in self.OPS:
            for i in range(len(oq)):
                try:
                    if oq[i] == op:
                        nq[i] = self.OPS[op](nq[i], nq.pop(i+1))
                        oq.pop(i)
                except IndexError:
                    continue
        
        if len(nq) == 1:
            return nq[0]
        else:
            raise ArithmeticError            


    def add(self, n1: float, n2: float) -> float:
        return n1 + n2


    def mul(self, n1: float, n2: float) -> float:
        return n1 * n2


    def div(self, n1: float, n2: float) -> float:
        try:
            return n1 / n2
        except ZeroDivisionError:
            return NaN


    def sub(self, n1: float, n2: float) -> float:
        return n1 - n2


if __name__ == "__main__":
    c = Calculator()
    n = len(sys.argv)
    if n == 2:
        s = sys.argv[1]
    elif n == 1:
        s = '4 + 5 * 4 - ( 3 * 3 )'
    else:
        raise SyntaxError
    r = c.calculate(s)

    print(r)