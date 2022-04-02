class MinStack:

    def __init__(self):
        self.mst = []
        self.min = 0

    def push(self, val: int) -> None:
        if not self.mst:
            self.min = val
            self.mst.append(val)
        elif val <= self.min:
            self.mst.append(2*val-self.min)
            self.min = val
        else:
            self.mst.append(val)

    def pop(self) -> None:
        t = self.mst.pop()
        if t <= self.min:
            res = self.min
            self.min = 2*self.min - t

    def top(self) -> int:
        t = self.mst[-1]
        if t <= self.min:
            return self.min
        return t

    def getMin(self) -> int:
        return self.min
