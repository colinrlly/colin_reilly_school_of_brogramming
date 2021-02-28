class Calculator:
    def __init__(self, n1=691, n2=692, ans=-691, op='NA', throw=False):
        self.history = [n1, n2, ans, op]
        self.throw = throw

    def add(self, n1, n2):
        ans = n1 + n2
        self.history = [n1, n2, ans, '+']
        print(ans)
        return ans

    def sub(self, n1, n2):
        ans = n1-n2
        self.history = [n1, n2, ans, '-']
        return ans

    def mul(self, n1, n2):
        ans = n1*n2
        self.history = [n1, n2, ans, '*']
        return ans

    def div(self, n1, n2):
        if n2 != 0:
            ans = n1/n2
            self.history = [n1, n2, ans, '/']
            return ans
        self.history = [n1, n2, None, '/']
        if self.throw:
            raise ValueError('Error, divide by zero. Get out of here with that shit.')
        else:
            print('Error, divide by zero. Get out of here with that shit.')

    def hst(self):
        if self.history.__len__() == 4:
            print('n1: ' + str(self.history[0]) + ', n2: ' + str(self.history[1]) + ', ans: ' + str(self.history[2]) + ', op: ' + self.history[3])
        else:
            print(self.history)

