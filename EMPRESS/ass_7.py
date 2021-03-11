
class Calculator:
        
    def add(self, x, y): 
        return x + y

    # mult function multiplies x and y, returns the result
    def mult(self, x, y):
        return x * y

    # sub function subtracts x and y, returns the result
    def sub(self, x, y):
        return x - y

    # div function divides x and y, returns the result
    def div(self, x, y):
        return x / y

    # defining the calculate function that will pass the string operation
    # then make it calculate haha
    def calculate(self, operation):
        # Using string method split to return operation as a list
        # ['4', '+', '5']
        operationlist = operation.split()

        # cast list items from string type to int type
        # now '4' and '5' are integers in operationlist
        # [4, '+', 5]
        x = int(operationlist[0])
        y = int(operationlist[2])
        # look at '+', understand to add
        if operationlist[1] == '+':
            return self.add(x, y)

        # if '-', do the subtract function
        elif operationlist[1] == '-':
            return self.sub(x,y)

        elif operationlist[1] == '*':
            return self.mult(x,y)

        elif operationlist[1] == '/':
            return self.div(x,y)

calc = Calculator()

result = calc.calculate('4 / 5')

print(result)
