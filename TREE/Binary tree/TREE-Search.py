class binarytree:
    def  __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def add(self,data):
        if self.data==data:
            return

        if self.data>data:
            if self.left:
                self.left.add(data)

            else:
                self.left=binarytree(data)
        else:
            if self.right:
                self.right.add(data)

            else:
                self.right = binarytree(data)

    def in_order_travel(self):
        elements=[]

        if self.left:
            elements+=self.left.in_order_travel()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_travel()

        return elements

    def search(self,value):
        if self.data==value:
            print(value,"is present in tree")

        if self.data>value:
            if self.left:
                print(self.left.search(value))
            else:
                print(value,"is not present in the tree")

        if self.data<value:
            if self.right:
                print(self.right.search(value))
            else:
                print(value,"is not present in the tree")


def build(elements):
    print("build the tree for",elements)
    root=binarytree(elements[0])

    for i in range(1,len(elements)):
        root.add(elements[i])

    return root



if __name__=="__main__":
    numbers=["india","russia","china","canada"]
    root=build(numbers)
    print(root.in_order_travel())
