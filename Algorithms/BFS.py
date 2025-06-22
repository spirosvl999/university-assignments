from collections import deque                # We need the import
                                             # to have graphs into our script.

def bfsOfGraph(adj, s, visited, res):
    q = deque()
    visited[s] = True
    q.append(s)
    while q:
        curr = q.popleft()
        res.append(curr)
        for x in adj[curr]:
            if not visited[x]:
                visited[x] = True
                q.append(x)
    return res

def bfsDisconnected(adj):
    V = len(adj)
    res = []
    visited = [False] * V
    for i in range(V):
        if not visited[i]:
            bfsOfGraph(adj, i, visited, res)
    return res
