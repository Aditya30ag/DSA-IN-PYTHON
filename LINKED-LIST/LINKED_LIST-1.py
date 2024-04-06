class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class linked_list:
    def __init__(self):
        self.head=None

    def insert_at_beginning (self,data):
        node=Node(data,self.head)
        self.head=node
    def print(self):
        if self.head is None:
            print("my list is empty")

        itr=self.head
        l=''
        while itr:
            l+=str(itr.data)+"-->"
            itr=itr.next

        print(l)


    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr =self.head
        while itr.next:
            itr=itr.next

        itr.next=Node(data,None)

if __name__=='__main__':
    s1=linked_list()
    s1.insert_at_beginning(5)
    s1.insert_at_beginning(89)
    s1.insert_at_end(79)
    s1.print()