class graph:
    def __init__(self,edges):
        self.edges=edges
        self.graph={}

        for start,end in self.edges:
            if start in self.graph:
                self.graph[start].append(end)
            else:
                self.graph[start]=[end]
        print(self.graph)

    def get_path(self,start,end,path=[]):

        path=path+[start]

        if start==end:
            return [path]

        if start not in self.graph:
            return []

        paths=[]
        for node in self.graph[start]:
            if node not in path:
                new_path=self.get_path(node,end,path)
                for p in new_path:
                    paths.append(p)

        return paths
# FIND THE SHORTEST PATH
    def shortest_path(self,start,end,path=[]):
        path = path + [start]

        if start == end:
            return path

        if start not in self.graph:
            return None

        shortest=None
        for node in self.graph[start]:
            if node not in path:
                sp=self.shortest_path(node,end,path)
                if sp:
                    if shortest is None or len(shortest)>len(sp):
                        shortest=sp

        return shortest


if __name__=="__main__":
    route=[("mumbai","paris"),
           ("mumbai","egypt"),
           ("paris","dubai"),
           ("paris","new york"),
           ("dubai","new york"),
           ("egypt","dubai"),
           ("new york","dubai")
           ]
    s1=graph(route)
    print(s1.get_path("mumbai","mumbai"))
    print(s1.get_path("mumbai","dubai"))
    print(s1.shortest_path("mumbai","dubai"))