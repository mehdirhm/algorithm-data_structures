from collections import defaultdict
class Graph:

    def __init__(self):
        self.graph = defaultdict(list) 

    def addEdge(self,s,d):
        self.graph[s].append(d)
    def dfs_utill(self,s,visited):
        visited[s] = True
        print(s,end=' ')
        for i in self.graph[s]:
            if visited[i] == False: 
                self.dfs_utill(i, visited) 

    def dfs_traversal(self , s):
        visited = [False] * (max(self.graph)+1)
        self.dfs_utill(v, visited) 

        

        
            
