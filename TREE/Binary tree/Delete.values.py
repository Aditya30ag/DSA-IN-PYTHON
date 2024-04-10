class binary_tree:
    def __init__(self,data):
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
                self.left=binary_tree(data)
        else:
            if self.right:
                self.right.add(data)
            else:
                self.right=binary_tree(data)
    def in_order_travel(self):
        element=[]

        if self.left:
            element+=self.left.in_order_travel()

        element.append(self.data)

        if self.right:
            element+=self.right.in_order_travel()

        return element

    def search(self,data):
        if self.data==data:
            print(data,"--","yes it is present")

        if self.data>data:
            if self.left:
                print(self.left.search(data))
            else:
                print("no it is not present in thr tree")

        if  self.data<data:
            if self.right:
                print(self.right.search(data))
            else:
                print("no it is not present in thr tree")
    def max(self):
        if self.right is None:
            return self.data
        return self.right.max()
    def min(self):
        if self.left is None:
            return self.data
        return self.left.min()
    def delete(self,value):
        if value<self.data:
            if self.left:
                self.left=self.left.delete(value)
            else:
                return None
        elif value>self.data:
            if self.right:
                self.right=self.right.delete(value)
            else:
                return None

        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left

            minval=self.right.min()
            self.data=minval
            self.right=self.right.delete(minval)

        return self
    def calculate_sum(self):
        left=self.left.calculate_sum() if self.left else 0
        right=self.right.calculate_sum() if self.right else  0
        return self.data + left + right
def build(elements):
    print("BUILD TREE FOR",elements)
    s2=binary_tree(elements[0])
    for i in range(1,len(elements)):
        s2.add(elements[i])
    return s2
if __name__=="__main__":
    numbers=[12,13,11,5,6,122,33,44]
    s1=build(numbers)
    print(s1.in_order_travel())
    print(s1.search(11))
    print(s1.calculate_sum())
    print(s1.delete(6))
    print(s1.in_order_travel())