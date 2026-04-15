class MinStack:

    def __init__(self):
        self.s = []

    def push(self, val: int) -> None:
        if not self.s:
            min_ = val
        else:
            min_ = self.s[-1][1]
            if(val<min_):
                min_ = val
        self.s.append([val, min_])
        

    def pop(self) -> None:
        if(len(self.s)!=0):
            val = self.s[-1]
            self.s.pop()
            return val[0]
        else:
            return None

    def top(self) -> int:
        if(len(self.s)!=0):
            return self.s[-1][0]
        else:
            return None

    def getMin(self) -> int:
        if(len(self.s)!=0):
            return self.s[-1][1]
        else:
            return None
