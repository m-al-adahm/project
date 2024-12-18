class DisjointSet:
    def _init_(self, n):
        self.parent = [i for i in range(n)]  # Parent of each node
        self.rank = [0] * n  # Rank to optimize union operation

    def find(self, x):
        # Path compression optimization
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        # Union by rank
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1

def kruskal(n, edges):
    """
    n: Number of vertices
    edges: List of tuples (weight, u, v), where u and v are vertices connected by an edge
    """
    # Step 1: Sort all edges by weight
    edges.sort()

    # Step 2: Initialize disjoint set and the MST result
    ds = DisjointSet(n)
    mst = []  # To store edges in the MST
    mst_weight = 0

    # Step 3: Process edges in sorted order
    for weight, u, v in edges:
        if ds.find(u) != ds.find(v):  # Check for cycle
            ds.union(u, v)  # Join the components
            mst.append((u, v, weight))  # Include this edge in the MST
            mst_weight += weight

    # Return the MST and its total weight
    return mst, mst_weight