from maaaaath import *
import random

# Alex Carpenter
# Colin Reilly School of Brogramming Assignment 5
# Math function demo


num1 = random.randrange(20)
num2 = random.randrange(20)

print(str(num1) + ' + ' + str(num2) + " =")
add(num1, num2)

num1 = random.randrange(20)
num2 = random.randrange(20)

print(str(num1) + ' - ' + str(num2) + " =")
sub(num1, num2)

num1 = random.randrange(20)
num2 = random.randrange(20)

print(str(num1) + ' * ' + str(num2) + " =")
mul(num1, num2)

num1 = random.randrange(20)
num2 = random.randrange(1,20)

print(str(num1) + ' / ' + str(num2) + " =")
div(num1, num2)

