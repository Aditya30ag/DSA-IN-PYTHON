from collections import deque
class Queue:
    def __init__(self):
        self.values=deque()

    def add(self,value):
        self.values.appendleft(value)

    def pop(self):
        print(self.values.pop())

    def is_empty(self):
        if len(self.values)==0:
            print("it is not empty")
        else:
            print("it is not empty")

    def size(self):
        print(len(self.values))
s1=Queue()
s1.add(12)
s1.add(13)
s1.add(14)
s1.add(15)
s1.pop()
s1.is_empty()
s1.size()
print(s1.values)