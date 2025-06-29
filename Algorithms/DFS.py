from collections import defaultdict          # We need the import
                                             # to have graphs into our script.
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    def addEdge(self, u, v):
        self.graph[u].append(v)

  
    def DFSUtil(self, v, visited):
        visited.add(v)
        print(v, end=' ')

        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited)


    def DFS(self, v):
        visited = set()
        self.DFSUtil(v, visited)
