class Calculator:
    def add(self, n1: int, n2: int) -> int:
        return n1 + n2

    def mul(self, n1: int, n2: int) -> int:
        return n1 + n2

    def div(self, n1: int, n2: int) -> int:
        try:
            return n1 // n2
        except ZeroDivisionError:
            return -1

    def sub(self, n1: int, n2: int) -> int:
        return n1 - n2


if __name__ == "__main__":
    c = Calculator()
    
    print(c.add(1,2))
    print(c.mul(3,4))
    print(c.div(5,0))
    print(c.sub(7,8))
