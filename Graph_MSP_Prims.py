#   5.Graph: Minimum Spanning Tree:
#  Represent a graph of your college campus using adjacency list /adjacency matrix. Nodes should represent 
# the various departments/institutes and links should represent the distance between them.
#  Find minimum spanning tree
#  a) Using Prim’s algorithm

 import sys

V = 5  # number of departments

# College departments graph (Adjacency Matrix)
# 0 means no direct connection
graph = [
 [0, 2, 0, 6, 0],  # CSE
 [2, 0, 3, 8, 5],  # IT
 [0, 3, 0, 0, 7],  # Mech
 [6, 8, 0, 0, 9],  # Civil
 [0, 5, 7, 9, 0]   # EXTC
]

def minKey(key, mstSet):
    min_val = sys.maxsize
    min_index = -1
    for v in range(V):
        if mstSet[v] == False and key[v] < min_val:
            min_val = key[v]
            min_index = v
    return min_index

def primMST(graph):
    key = [sys.maxsize] * V   # Distance values
    parent = [None] * V       # Store MST
    key[0] = 0
    mstSet = [False] * V

    parent[0] = -1  # First node is root

    for _ in range(V - 1):
        u = minKey(key, mstSet)
        mstSet[u] = True

        for v in range(V):
            if graph[u][v] > 0 and mstSet[v] == False and key[v] > graph[u][v]:
                key[v] = graph[u][v]
                parent[v] = u

    print("Edge \tWeight")
    total = 0
    for i in range(1, V):
        print(parent[i], "-", i, "\t", graph[i][parent[i]])
        total += graph[i][parent[i]]
    print("Total Minimum Distance:", total)

# ---- Main ----
print("Minimum Spanning Tree using Prim's Algorithm:\n")
primMST(graph)
