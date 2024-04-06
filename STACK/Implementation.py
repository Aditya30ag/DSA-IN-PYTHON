class Stack:
    def __init__(self):
        self.container =[]

    def push(self, val):
        self.container=[val]+self.container

    def pop(self):
        print(self.container.pop(0))

    def peek(self):
        print(self.container[-1])

    def is_empty(self):
        if len(self.container)==0:
            print("list is empty")

        else:
            print("the list is not empty")
    def size(self):
        print(len(self.container))

s1=Stack()
s1.push(12)
s1.push(13)
s1.push(14)
s1.push(15)
s1.pop()
s1.peek()
s1.is_empty()
s1.size()
print(s1.container)
