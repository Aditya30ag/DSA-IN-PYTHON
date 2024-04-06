class TreeNode:
    def __init__(self,data):
        self.data=data
        self.children=[]
        self.parent=None

    def add_child(self,child):
        child.parent=self
        self.children.append(child)

    def get(self):
        level=0
        p=self.parent
        while p:
            level+=1
            p=p.parent
        return level

    def print(self):
        spaces=" "*self.get()*3
        prefix=spaces+"__"*self.get()
        print(prefix+self.data)
        for child in self.children:
            child.print()

def build():
    root=TreeNode("ELECTRONIC")

    laptop=TreeNode("laptop")
    laptop.add_child(TreeNode("mac"))
    laptop.add_child(TreeNode("surface"))
    laptop.add_child(TreeNode("think pad"))

    cellphone=TreeNode("cellphone")
    cellphone.add_child(TreeNode("i phone"))
    cellphone.add_child(TreeNode("goole pixle"))
    cellphone.add_child(TreeNode("vivo"))

    television=TreeNode("television")
    television.add_child(TreeNode("samsung"))
    television.add_child(TreeNode("LG"))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(television)

    root.print()

if __name__=="__main__":
    root=build()