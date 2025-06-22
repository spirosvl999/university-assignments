import heapq


class Graph:
    def __init__(self, V):
        self.V = V
        self.adj = [[] for _ in range(V)]

    def add_edge(self, u, v, w):
        self.adj[u].append((v, w))
        self.adj[v].append((u, w))

    def prim_mst(self):
        pq = []
        src = 0

        key = [float('inf')] * self.V

        parent = [-1] * self.V

        in_mst = [False] * self.V

        heapq.heappush(pq, (0, src))
        key[src] = 0

        while pq:

            u = heapq.heappop(pq)[1]

            if in_mst[u]:
                continue

            in_mst[u] = True  

            for v, weight in self.adj[u]:
                if not in_mst[v] and key[v] > weight:
                    key[v] = weight
                    heapq.heappush(pq, (key[v], v))
                    parent[v] = u

        for i in range(1, self.V):
            print(f"{parent[i]} - {i}")
