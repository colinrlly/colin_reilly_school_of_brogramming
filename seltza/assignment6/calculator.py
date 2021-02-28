

class calculator:

    def __init__(self, n1=691, n2=692, ans=-691, op='NA'):
        self.history = [n1, n2, ans, op]

    def add(self, n1, n2):
        ans = n1 + n2
        history = [n1, n2, ans, '+']
        print(ans)
        return ans

    def sub(self, n1, n2):
        ans = n1-n2
        history = [n1, n2, ans, '-']
        return ans

    def mul(self, n1, n2):
        ans = n1*n2
        history = [n1, n2, ans, '*']
        return ans

    def div(self, n1, n2):
        if n2 != 0:
            ans = n1/n2
            history = [n1, n2, ans, '/']
            return ans
        raise ValueError('Error, divide by zero. Get out of here with that shit.')

    def hst(self):
        print(self.history)

