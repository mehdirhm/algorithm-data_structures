from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self,s,d):
        self.graph[s].append(d)
    def bfsTraversal(self,s):
        visited = [False] * (len(self.graph))
        print(visited)
        q = []
        q.append(s)
        visited[s] = True
        while q:
            s = q.pop(0)
            print(s , end = " ")

            for i in self.graph[s]:
                if visited[i] == False:
                    q.append(i)
                    visited[i] = True
   
    





    