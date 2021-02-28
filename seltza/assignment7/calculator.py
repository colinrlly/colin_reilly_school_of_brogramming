class Calculator:
    """
    A class to perform simple arithmatic.
    
    ...

    Attributes
    ----------
    history : list
        stores the previous calculation
    throw : bool
        whether to throw exceptions when dividing by zero
    """

    def __init__(self, n1=691, n2=692, ans=-691, op='NA', throw=False):
        self.history = [n1, n2, ans, op]
        self.throw = throw

    def razer(self, message='Error'):
        if self.throw:
            raise Exception(message)
        else:
            print(message)

    def add(self, n1, n2):
        ans = n1 + n2
        self.history = [n1, n2, ans, '+']
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
        self.razer('Error, divide by zero. Get out of here with that shit.')

    def pwo(self, n1, n2):
        ans = pow(n1, n2)
        self.history = [n1, n2, ans, '^']
        return ans

    def mod(self, n1, n2):
        if n2 != 0:
            ans = n1%n2
            self.history = [n1, n2, ans, '%']
            return ans
        self.history = [n1, n2, None, '%']
        self.razer('Error, mod by zero. Get out of here with that shit.')

    def hst(self):
        if self.history.__len__() == 4:
            print('n1: ' + str(self.history[0]) + ', n2: ' + str(self.history[1]) + ', ans: ' + str(self.history[2]) + ', op: ' + self.history[3])
        else:
            print(self.history)

    def calculate(self, stin: str):
        if stin:
            switcher = {
                '+': self.add,
                '-': self.sub,
                '*': self.mul,
                '/': self.div,
                '^': self.pwo,
                '%': self.mod
            }
            spt = stin.split()
            if spt.__len__() == 3:
                f = switcher.get(spt[1], 'nothing')
                if f:
                    try:
                        ans = f(float(spt[0]), float(spt[2]))
                        # check if it's an integer, use that formatting if so
                        if ans and ans.is_integer():
                            return int(ans)
                        return ans
                    except ValueError:
                        self.razer('You think you can get away with putting messed up numbers in here?')
                else:
                    self.razer('You think ' + spt[1] + ' is a valid operator? Are ya stupid or somethin?')
            else:
                self.razer('You think you can just put together an expression all willy nilly like? STICK TO THE FRICKIN FORMAT! calculate(\'n1 $ n2\') where $ is your operator')
        else:
            self.razer('You think you can get arround just sending empty strings all over the joint?')


