def floydWarshall(graph):
    V = len(graph)
    for k in range(V):
        for i in range(V):
            for j in range(V):
                if ((graph[i][j] == -1 or 
                    graph[i][j] > (graph[i][k] + graph[k][j]))
                    and (graph[k][j] != -1 and graph[i][k] != -1)):
                    graph[i][j] = graph[i][k] + graph[k][j]

# Into the main, something like this:
#    floydWarshall(graph)
#    for i in range(len(graph)):
#        for j in range(len(graph)):
#            print(graph[i][j], end=" ")
#        print()
