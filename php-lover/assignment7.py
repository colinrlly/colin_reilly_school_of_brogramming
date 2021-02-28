class Calculator:
    OPS = ()
    def __init__(self):
        self.OPS = {
            '/': self.div,
            '*': self.mul,
            '-': self.sub,
            '+': self.add
        }


    def calculate(self, equation: str):
        nq = []
        oq = []
        eq_arr = equation.split(' ')

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
            raise IndexError            


    def add(self, n1: int, n2: int) -> int:
        return n1 + n2


    def mul(self, n1: int, n2: int) -> int:
        return n1 * n2


    def div(self, n1: int, n2: int) -> int:
        try:
            return n1 // n2
        except ZeroDivisionError:
            return NaN


    def sub(self, n1: int, n2: int) -> int:
        return n1 - n2


if __name__ == "__main__":
    c = Calculator()

    r = c.calculate('4 + 5 * 4 - ( 3 * 3 )')

    print(r)