class Calculator:
    """
    A class to perform simple arithmatic.
    
    ...

    Attributes
    ----------
    history : list
        stores the previous calculation
    throw : bool
        whether to throw exceptions when dividing or modulating by zero

    Methods
    -------
    razer(message='Error'):
        raises an exception or prints to terminal, dependent on throw
    add(n1, n2):
        adds two numbers
    sub(n1, n2):
        subtracts two numbers
    mul(n1, n2):
        multiplies two numbers
    div(n1, n2):
        divide two numbers
    pwo(n1, n2):
        raises n1 to the n2th
    mod(n1, n2):
        takes n1 mod m2
    hst():
        prints the history, with formatting if 4 values are present
    calculate(stin: str):
        parses a string to perform an operation
    """

    def __init__(self, hist=[691, 692, -691, 'NA'], throw=False):
        """
        Initializes calculator class

        Parameters:
            hist : list , optional
                the history stored on creation
            throw : bool , optional
                wheather to throw exceptions or print to the command line
                when errors are encountered. default is False.
        """
        self.history = hist
        self.throw = throw

    def razer(self, message='Error') -> None:
        """
        raises an exception or prints to terminal, dependent on throw

        Parameters:
            message : str , optional
                message to display
        """
        if self.throw:
            raise Exception(message)
        else:
            print(message)

    def add(self, n1, n2):
        """
        adds two numbers

        Parameters:
            n1 (int or float): the first number
            n2 (int or float): the first number

        Returns:
            ans : the ans
        """
        ans = n1 + n2
        self.history = [n1, n2, ans, '+']
        return ans

    def sub(self, n1, n2):
        """
        adds two numbers

        Parameters:
            n1 (int or float): the first number
            n2 (int or float): the first number

        Returns:
            ans : the ans
        """
        ans = n1-n2
        self.history = [n1, n2, ans, '-']
        return ans

    def mul(self, n1, n2):
        """
        adds two numbers

        Parameters:
            n1 (int or float): the first number
            n2 (int or float): the first number

        Returns:
            ans : the ans
        """
        ans = n1*n2
        self.history = [n1, n2, ans, '*']
        return ans

    def div(self, n1, n2):
        """
        adds two numbers

        Parameters:
            n1 (int or float): the first number
            n2 (int or float): the first number

        Returns:
            ans : the ans
        """
        if n2 != 0:
            ans = n1/n2
            self.history = [n1, n2, ans, '/']
            return ans
        self.history = [n1, n2, None, '/']
        self.razer('Error, divide by zero. Get out of here with that shit.')

    def pwo(self, n1, n2):
        """
        adds two numbers

        Parameters:
            n1 (int or float): the first number
            n2 (int or float): the first number

        Returns:
            ans : the ans
        """
        ans = pow(n1, n2)
        self.history = [n1, n2, ans, '^']
        return ans

    def mod(self, n1, n2):
        """
        adds two numbers

        Parameters:
            n1 (int or float): the first number
            n2 (int or float): the first number

        Returns:
            ans : the ans
        """
        if n2 != 0:
            ans = n1%n2
            self.history = [n1, n2, ans, '%']
            return ans
        self.history = [n1, n2, None, '%']
        self.razer('Error, mod by zero. Get out of here with that shit.')

    def hst(self):
        """
        prints the history, with formatting if 4 values are present

        Returns: None
        """
        if self.history.__len__() == 4:
            print('n1: ' + str(self.history[0]) + ', n2: ' + str(self.history[1]) + ', ans: ' + str(self.history[2]) + ', op: ' + self.history[3])
        else:
            print(self.history)

    def calculate(self, stin: str):
        """
        parses a string to perform an operation

        Parameters:
            stin (str): string to parse
        Returns:
            ans : the ans
        """
        if stin: # protect against empty input
            # dictionary of functions to use based on the string
            switcher = {
                '+': self.add,
                '-': self.sub,
                '*': self.mul,
                '/': self.div,
                '^': self.pwo,
                '%': self.mod
            }
            spt = stin.split() # split string on whitespace
            if spt.__len__() == 3: # enforce three arguments (ideally two numbers and an operator)
                f = switcher.get(spt[1], 'nothing') # lookup the function to use from the dictionary
                if f: # if f is None, the string did not contain a valid operator
                    try: # try is for ValueError raised by float() if string is malformed
                        ans = f(float(spt[0]), float(spt[2]))
                        # check if it's an integer, use that formatting if so
                        if ans and ans.is_integer(): # protect against int(ans = None)
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


