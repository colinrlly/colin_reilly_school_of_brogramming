"""Calculate a given string equation

python assignment7.py "(4+5)*4/6 - 1"

"""
import math
import re
import sys

class Calculator:
    def __init__(self):
        self.OPS = {
            '^': math.pow,
            '/': self.div,
            '*': self.mul,
            '+': self.add,
            '-': self.sub,
        }


    def calculate(self, equation: str) -> float:
        """Calculate a string equation using PEMDAS rule"""
        nq = []
        oq = []

        l = re.split(r'\s|([\/*+\-\(\)\^])', equation)
        eq_arr = [i for i in l if i != '' and i is not None]

        i = 0
        last_op = True
        while i < len(eq_arr):
            # create the equation queue
            x = eq_arr[i]
            if x == '(':
                # process parentheses
                start = i + 1
                end = len(eq_arr) - 1 - eq_arr[::-1].index(')')

                nq.append(self.calculate(' '.join(eq_arr[start:end])))
                i = end
                last_op = False
            elif x not in self.OPS:
                # add number to queue
                nq.append(float(x))
                last_op = False
            elif x in self.OPS:
                # add operator to queue
                if last_op and x == '-':
                    nq.append(-1.0)
                    oq.append('*')
                else:
                    oq.append(x)
                last_op = True
            else:
                raise SyntaxError

            i += 1

        # run equation queue
        for op in self.OPS: # run each op in EMDAS order
            while op in oq: # calc until all instances are complete
                i = oq.index(op) # get index of op
                nq[i] = self.OPS[op](nq[i], nq.pop(i+1)) # calc for the op
                oq.pop(i) # remove the op

        # return result
        if len(nq) == 1:
            return nq[0]
        else:
            raise ArithmeticError


    def add(self, n1: float, n2: float) -> float:
        return n1 + n2


    def mul(self, n1: float, n2: float) -> float:
        return n1 * n2


    def div(self, n1: float, n2: float) -> float:
        return n1 / n2


    def sub(self, n1: float, n2: float) -> float:
        return n1 - n2


if __name__ == "__main__":
    c = Calculator()
    n = len(sys.argv)
    if n == 2:
        s = sys.argv[1]
    elif n == 1:
        # example equation
        s = "-2 * 2 * (4 ^ (3 + 1) -10)"
    else:
        raise SyntaxError

    try:
        r = c.calculate(s)
    except:
        print("oopsie woopsie we had a fucky wucky")
        exit(1)

    print(r)
