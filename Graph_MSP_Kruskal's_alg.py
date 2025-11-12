#  4 Graph: Minimum Spanning Tree:
#  Represent a graph of your college campus using adjacency list /adjacency matrix. Nodes should represent 
# the various departments/institutes and links should represent the distance between them.
#  Find minimum spanning tree
#  a) Using Kruskal’s algorithm

class Graph:
    def __init__(self, v):
        self.V = v
        self.edges = []

    def add_edge(self, u, v, w):
        self.edges.append([u, v, w])

    def find(self, parent, i):
        if parent[i] == i: return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        xroot, yroot = self.find(parent, x), self.find(parent, y)
        if rank[xroot] < rank[yroot]: parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]: parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def kruskal(self):
        self.edges.sort(key=lambda x: x[2])
        parent, rank = [], []
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        result = []
        e = i = 0
        while e < self.V - 1:
            u, v, w = self.edges[i]
            i += 1
            x, y = self.find(parent, u), self.find(parent, v)
            if x != y:
                e += 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)
        print("Edges in Minimum Spanning Tree:")
        total = 0
        for u, v, w in result:
            print(f"{u} -- {v} == {w}")
            total += w
        print("Total Minimum Distance:", total)

# ---- Main ----
g = Graph(5)
# Representing departments and distances (example)
g.add_edge(0, 1, 2)   # CSE - IT
g.add_edge(0, 3, 6)   # CSE - Civil
g.add_edge(1, 3, 8)   # IT - Civil
g.add_edge(1, 2, 3)   # IT - Mech
g.add_edge(1, 4, 5)   # IT - EXTC
g.add_edge(2, 4, 7)   # Mech - EXTC
g.add_edge(3, 4, 9)   # Civil - EXTC

g.kruskal()
