import math

class tallCalc:
    
    # Core Basic Mathematical Functions

    # Basic Addition Function
    def add(self, n1, n2):
        return n1 + n2

    # Basic Subtraction Function
    def sub(self, n1 , n2):
        return n1 - n2

    # Basic Multiplication Function
    def mul(self, n1, n2):
        return n1 * n2

    # Basic Division Function
    def div(self, n1, n2):
        return n1 / n2

    # Core Complex Mathematical Functions

    # Exponentiation
    def exp(self, n1, n2):
        return n1 ** n2

    # Square Root
    def sqrt(self, n1):
        return math.sqrt(n1)
    

    # Trigonometry
    # Complex, need to convert degrees to radians for input then radians back to degrees for output.

    # Sin (I/O in Radians Currently)
    def sin(self, n1):
        return math.sin(n1)

    # Cos (I/O in Radians Currently)
    def cos(self, n1):
        return math.cos(n1)

    # Tan (I/O in Radians Currently)
    def tan(self, n1):
        return math.tan(n1)


    # Logic to Handle Calculator String Inputs.

    # Converting the user string input into usable floats.
    def probStringParse(self, probSplitStr):
        
        n1 = probSplitStr[0]
        f1 = n1.strip()
        if f1.isnumeric():
            f1 = float(f1)
        
        n2 = probSplitStr[1]
        f2 = n2.strip()
        if f2.isnumeric():
            f2 = float(f2)

        return f1, f2


    # Main calculator function, determines what basic function to call and passes floats.
    def calculate(self, prob):

        # Operator Dictionary
        # Add trig once logic is entirely sorted there.
        # opDict = {
        #         '+': self.add,
        #         '-': self.sub,
        #         '*': self.mul,
        #         '/': self.div,
        #         '^': self.exp,
        #         'sqrt': self.sqrt
        #     }
        

        # Split the Problem String
        if '+' '-' '*' '/' '^' '√' in prob:
            probSplitStr = prob.split('+', '-', '*', '/', '^', '√')
            (f1, f2) = self.probStringParse(probSplitStr)
            return self.exp(f1, f2)
        



tCalc = tallCalc()

result = tCalc.calculate('4 ^ 3')

print(result)



