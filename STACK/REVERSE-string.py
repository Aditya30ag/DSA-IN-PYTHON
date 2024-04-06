class Stack:
    def __init__(self):
        self.container =[]

    def push(self, val):
        self.container=[val]+self.container

    def pop(self):
        return self.container.pop(0)

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)

def reverse(str):
    stack=Stack()

    for i in str:
        stack.push(i)

    l=""
    while stack.size()!=0:
        l+=stack.pop()
    print(l)

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
print(reverse("hello"))