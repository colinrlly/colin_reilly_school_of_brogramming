Assignment 7

Objective
Add methods to your class to allow a string to be passed in. Then by parsing that string decide
what the two arguments are as well as what the operation is. 

For example
You pass in the string '4 + 5', your program needs to be able to figure out that the two arguments
are 4 and 5 and the operator is addition.

It then must call one of your 4 functions on the class to add 4 and 5.
Print the result of this operation to the console.

Things you will have to consider / tips from professor man
1. String parsing. Look into operating on strings as arrays in python. Look into python string operation.
2. You will most likely need to 'loop' over each character in the string. Look into 'for in' loops.
3. You will need to 'cast' the string from a string to an integer in order to convert
   the numbers in your string to operatable entities. Look into 'casting' in python.

Goal
The goal of this is to be able to type

calc = Calculator()

result = calc.calculate('4 + 5')

print(result)

In the console see 9
