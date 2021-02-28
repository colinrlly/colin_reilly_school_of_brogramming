from calculator import Calculator
import random

# Alex Carpenter
# Colin Reilly School of Brogramming Assignment 5
# Math function demo

c = Calculator(throw=False)

num1 = random.randrange(20)
num2 = random.randrange(20)

print(str(num1) + ' + ' + str(num2) + " =")
print(c.add(num1, num2))

num1 = random.randrange(20)
num2 = random.randrange(20)

print(str(num1) + ' - ' + str(num2) + " =")
print(c.sub(num1, num2))

num1 = random.randrange(20)
num2 = random.randrange(20)

print(str(num1) + ' * ' + str(num2) + " =")
print(c.mul(num1, num2))

num1 = random.randrange(20)
num2 = random.randrange(1,20)

print(str(num1) + ' / ' + str(num2) + " =")
print(c.div(num1, num2))

num1 = random.randrange(20)
num2 = 0

print(str(num1) + ' / ' + str(num2) + " =")
print(c.div(num1, num2))

print('History:')
c.hst()

str_2_test = '4 + 5'
c.prs(str_2_test)
