class Stack(object):
    def __init__(self):
        self.theArray = []
        self.size = 0
    def push(self, n):
        self.theArray.append(n)
        self.size += 1
    def peek(self):
        return self.theArray[self.size - 1]
    def pop(self):
        self.size -= 1
        return self.theArray.pop()
    def __len__(self):
        return self.size
    def __nonzero__(self):
        if self.size == 0:
            return 0
        return 1
    def __str__(self):
        stringy = "["
        for item in self.theArray:
            stringy += str(item)
            stringy += ", "
        stringy += "]"
        return stringy