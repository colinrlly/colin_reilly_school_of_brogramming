class calculator:
    def add(self, x, y):
        return x + y

    def sub(self, x, y):
        return x - y

    def mul(self, x, y):
        return x * y

    def div(self, x, y):
        return x / y

    def calculate(self, prob):
        parsed_prob = prob.split()
        c1 = parsed_prob[0]
        if c1.isnumeric():
            c1 = int(c1)
        c2 = parsed_prob[2]
        if c2.isnumeric():
            c2 = int(c2)
        o = parsed_prob[1]
        if o == "+":
            return self.add(c1, c2)
        elif o == "-":
            return self.sub(c1, c2)
        elif o == "*":
            return self.mul(c1, c2)
        elif o == "/":
            return self.div(c1, c2)

    def prepare_prob(self, adv_parsed_prob):
        unstr_c1 = adv_parsed_prob[0]
        c1 = unstr_c1.strip()
        if c1.isnumeric():
            c1 = int(c1)

        unstr_c2 = adv_parsed_prob[1]
        c2 = unstr_c2.strip()
        if c2.isnumeric():
            c2 = int(c2)

        return c1, c2

    def AdvCalculate(self, prob):
        if "+" in prob:
            adv_parsed_prob = prob.split("+")
            (c1, c2) = self.prepare_prob(adv_parsed_prob)
            return self.add(c1, c2)

        elif "-" in prob:
            adv_parsed_prob = prob.split("-")
            (c1, c2) = self.prepare_prob(adv_parsed_prob)
            return self.sub(c1, c2)

        elif "*" in prob:
            adv_parsed_prob = prob.split("*")
            (c1, c2) = self.prepare_prob(adv_parsed_prob)
            return self.mul(c1, c2)

        elif "/" in prob:
            adv_parsed_prob = prob.split("/")
            (c1, c2) = self.prepare_prob(adv_parsed_prob)
            return self.div(c1, c2)

calc = calculator()

result = calc.AdvCalculate("10*2")

print(result)
