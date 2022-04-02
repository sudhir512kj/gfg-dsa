class EvalPostfix:
    def __init__(self) -> None:
        self.stack = []
        self.top = -1

    def pop(self):
        if self.top == -1:
            return
        else:
            self.top -= 1
            return self.stack.pop()

    def push(self, op):
        self.top += 1
        self.stack.append(op)

    def mainFunc(self, ab):
        for x in ab:
            try:
                self.push(int(x))
            except ValueError:
                val1 = self.pop()
                val2 = self.pop()

                switcher = {'+': val2 + val1, '-': val2-val1,
                            '*': val2 * val1, '/': val2 / val1, '^': val2**val1}
                self.push(switcher.get(x))

        return int(self.pop())


obj = EvalPostfix()
print(obj.mainFunc("123+*8-"))
