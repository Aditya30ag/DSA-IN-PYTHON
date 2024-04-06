class binary_tree:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def add_child(self,data):
        if self.data==data:
            return

        if self.data>data:
            if self.left:
                self.left.add_child(data)

            else:
                self.left=binary_tree(data)

        else:
            if self.right:
                self.right.add_child(data)

            else:
                self.right = binary_tree(data)
    def in_order_travel(self):
        elements=[]

        if self.left:
            elements+=self.left.in_order_travel()

        elements.append(self.data)

        if self.right:
            elements+=self.right.in_order_travel()

        return elements
def build_tree(elements):
    print("BUILD TREE FOR:",elements)
    root=binary_tree(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root


if __name__=="__main__":
    numbers=[17,4,1,20,9,23,18,34]
    root=build_tree(numbers)
    print(root.in_order_travel())