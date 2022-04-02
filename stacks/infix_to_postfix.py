class InfixToPostfix:
    def __init__(self) -> None:
        self.top = -1
        self.st = []
        self.res = []
        self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    def isEmpty(self):
        return True if self.top == -1 else False

    def peek(self):
        return self.st[-1]

    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.st.pop()
        return "$"

    def push(self, ch):
        self.top += 1
        self.st.append(ch)

    def notGreater(self, i):
        try:
            a = self.precedence[i]
            b = self.precedence[self.peek()]
            return True if a <= b else False
        except KeyError:
            return False

    def infixToPostfix(self, exp):
        for x in exp:
            if x.isalpha():
                self.res.append(x)

            elif x == '(':
                self.push(x)

            elif x == ')':
                while not self.isEmpty() and self.peek() != '(':
                    a = self.pop()
                    self.res.append(a)
                if not self.isEmpty() and self.peek() != '(':
                    return -1
                else:
                    self.pop()

            else:
                while not self.isEmpty() and self.notGreater(x):
                    if x == '^' and self.peek() == x:
                        break
                    self.res.append(self.pop())
                self.push(x)

        while not self.isEmpty():
            self.res.append(self.pop())

        return "".join(self.res)


obj = InfixToPostfix()
print(obj.infixToPostfix("a+b*(c^d-e)^(f+g*h)-i"))
