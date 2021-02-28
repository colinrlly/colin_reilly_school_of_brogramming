def summ(a, b):
    return a + b


def diff(a, b):
    return a - b


def prod(a, b):
    return a * b


def quot(a, b):
    if b == 0:
        return "undefined"
    return a / b


print(summ(3, 2))
print(diff(3, 2))
print(prod(3, 2))
print(quot(3, 2))
