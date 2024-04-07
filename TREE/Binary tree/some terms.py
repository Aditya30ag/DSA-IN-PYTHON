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
    def calculate_sum(self):
        left=self.left.calculate_sum() if self.left else 0
        right=self.right.calculate_sum() if self.right else 0
        return self.data + left +right

    def max(self):
        if self.right is None:
            return self.data
        return self.right.max()

    def min(self):
        if self.left is None:
            return self.data
        return self.left.min()

    def pre_order_traversal(self):
        elements = [self.data]
        if self.left:
            elements += self.left.pre_order_traversal()
        if self.right:
            elements += self.right.pre_order_traversal()

        return elements

    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()
        if self.right:
            elements += self.right.post_order_traversal()

        elements.append(self.data)

        return elements
def build(elements):
    print("build the tree for",elements)
    root=binarytree(elements[0])

    for i in range(1,len(elements)):
        root.add(elements[i])

    return root

if __name__=="__main__":
    numbers=[23,4,5,32,8,99,90,567]
    root=build(numbers)
    print(root.in_order_travel())
    print(root.calculate_sum())
    print(root.max())
    print(root.min())
    print(root.pre_order_traversal())
    print(root.post_order_traversal())