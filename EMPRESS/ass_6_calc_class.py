
a = 2
b = 10

# Create class
class Calculator:
    # adding self parameter is necessary, it is a reference
    # to the current instance of the class.
    def add(self,x,y): 
        return (x + y)

# mult function multiplies x and y, returns the result
    def mult(self,x,y):
        return (x * y)

# sub function subtracts x and y, returns the result
    def sub(self,x,y):
        return (x - y)

# div function divides x and y, returns the result
    def div(self,x,y):
        return (x / y)

# main function 
    def main(self):
        print(add(a,b))
        print(mult(a,b))
        print(sub(a,b))
        print(div(a,b))

# "cat" is an instance of class "animal"

# MyCalc() instantiates the MyCalc class - creates an instant
# that exists.
# Instance is placed in the calculator variable
calc = Calculator()

# self arg, self referencing the instance 'calculator'
# is added first, before 'a' 
print(calc.add(a,b))
print(calc.mult(a,b))
print(calc.div(a,b))
print(calc.sub(a,b))
