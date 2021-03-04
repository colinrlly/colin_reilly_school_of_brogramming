import math

class tallCalc:
    
    # Core Basic Mathematical Functions

    # Basic Addition Function
    def add(self, floatList):
        solution = floatList[0] + floatList[1]
        return solution

    # Basic Subtraction Function
    def sub(self, floatList):
        solution = floatList[0] - floatList[1]
        return solution

    # Basic Multiplication Function
    def mul(self, floatList):
        solution = floatList[0] * floatList[1]
        return solution

    # Basic Division Function
    def div(self, floatList):
        solution = floatList[0] / floatList[1]
        return solution

    # Core Complex Mathematical Functions

    # Exponentiation
    def exp(self, floatList):
        solution = floatList[0] ** floatList[1]
        return solution

    # Square Root
    def sqrt(self, floatList):
        solution = math.sqrt(floatList[0])
        return solution
    

    # Trigonometry

    # Sin (Input in degrees, conversion to radians within function)
    def sin(self, floatList):
        solution = math.sin(math.radians(floatList[0]))
        return solution

    # Cos (Input in degrees, conversion to radians within function)
    def cos(self, floatList):
        solution = math.cos(math.radians(floatList[0]))
        return solution

    # Tan (Input in degrees, conversion to radians within function)
    def tan(self, floatList):
        solution = math.tan(math.radians(floatList[0]))
        return solution



    # Logic to Handle Calculator String Inputs.
    # Converting the user string input into usable floats.
    # Returns the floats as a list with indexed values.
    def probStringCast(self, probSplitStr):
        
        fL = []
        for n in probSplitStr:
            # if n.isnumeric(): # Breaks decimal places and whitespace for some reason.
            fL.append(float(n))
        return fL


    # Main calculator function, determines what basic function to call and passes floats.
    def calculate(self, prob):

        # Operator Dictionary
        # Ordered based on EMDAS.
        opDict = {
                '^': self.exp,
                '√': self.sqrt,
                '*': self.mul,
                '/': self.div,
                '+': self.add,
                '-': self.sub,
                'sin': self.sin,
                'cos': self.cos,
                'tan': self.tan
            }
        

        # Split the Problem String and push it to probStringParse function.
        # Use return from probStringParse and push it to corresponding operator function.
        operators = [
            '+', '-',
            '*', '/',
            '^', '√',
            'sin', 'cos', 'tan'
        ]


        # PEMDAS Lists
        parenOp = ['(', ')']
        expOp = ['^']
        muldivOp = ['*', '/']
        addsubOp = ['+', '-']


        # Look into "List Comprehension" to potentially streamline.
        # Recursion!!!
        # Recursive parentheses first, then work on EMDAS
        for o in operators:
            if o in prob:
                probSplitStr = prob.split(o)
                fL = self.probStringCast(probSplitStr)
                return opDict[o](fL)
        



tCalc = tallCalc()

result = tCalc.calculate('24/25')

print(result)
