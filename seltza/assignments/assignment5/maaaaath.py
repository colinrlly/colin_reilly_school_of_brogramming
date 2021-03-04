# Alex Carpenter
# Colin Reilly School of Brogramming Assignment 5
# math functions
# i looked up the PEP guide for docstrings and decided it wasn't worth it


def add(n1, n2):
    ans = n1 + n2
    print(ans)
    return ans

def sub(n1, n2):
    ans = n1-n2
    print(ans)
    return ans

def mul(n1, n2):
    ans = n1*n2
    print(ans)
    return ans

def div(n1, n2):
    if n2 != 0:
        ans = n1/n2
        print(ans)
        return ans
    print ('Error, divide by zero. Get out of here with that shit.')

