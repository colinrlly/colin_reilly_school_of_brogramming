from calculator import Calculator

# Alex Carpenter
# Colin Reilly School of Brogramming Assignment 5
# Math function demo

def calc(obj, expr='4 + 5'):
    print(expr)
    ans = obj.calculate(expr)
    if ans:
        print(ans)

c = Calculator(throw=False)

print('\n\noperators:')
calc(c)
calc(c, '4 - 5')
calc(c, '4 * 5')
calc(c, '4 / 5')
calc(c, '4 ^ 5')
calc(c, '4 % 5')

print('\nfloat input:')
calc(c, '7.5 - 2.5')

print('\nfloat output:')
calc(c, '10 / 3')

print('\nfloat input & output:')
calc(c, '13.37 * 6.9')

print('\ndiv by 0:')
calc(c, '420 / 0')
calc(c, '4 % 0')

print('\nbad formatting:')
calc(c, '4 +4')
calc(c, '4+4')

print("\nempty string:")
calc(c, '')

print("\nbad numbers:")
calc(c, 'dog + shit')
calc(c, '420 + 6ix9ine')
