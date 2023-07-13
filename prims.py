import sys
from typing import List


def prim(G: List[List[int]], V: int) -> int:
    """
    Finds the minimum spanning tree of a graph using Prim's algorithm.

    Args:
        G (List[List[int]]): the graph in matrix representation.
        V (int): the number of vertices.

    Returns:
        int: the total weight of the minimum spanning tree.
    """
    INF = sys.maxsize
    n_edge = 0
    cost = 0
    selected = [False] * V
    selected[0] = True

    print("Edge : Weight")

    while n_edge < V - 1:
        min = INF
        x = 0  # row number
        y = 0  # col number

        for i in range(V):
            if selected[i]:
                for j in range(V):
                    if not selected[j] and G[i][j] != 0:
                        if min > G[i][j]:
                            min = G[i][j]
                            x = i
                            y = j

        cost += G[x][y]
        print(f"{x} - {y} : {G[x][y]}")
        selected[y] = True
        n_edge += 1

    return cost


if __name__ == "__main__":
    V = 5
    INF = sys.maxsize
    graph = [
        [0, 50, 15, INF, 65],
        [INF, 0, INF, INF, 10],
        [20, INF, 0, 25, INF],
        [INF, 12, INF, 0, 18],
        [INF, INF, INF, INF, 0],
    ]
    cost = prim(graph, V)
    print(f"Cost = {cost}")

"""
1.  Choose a starting vertex and add it to the minimum spanning tree.

2.  For all adjacent vertices to the starting vertex, add the edge with the smallest weight to the minimum spanning tree.

3.  Choose the adjacent vertex with the smallest weight to add to the minimum spanning tree.

4.  Repeat steps 2 and 3 until all vertices have been added to the minimum spanning tree.

3.  The idea behind Prim's algorithm is to iteratively grow the minimum spanning tree by selecting the cheapest edge that
    connects the tree to a new vertex. The algorithm maintains a set of vertices that have been added to the tree and a
    set of vertices that have not been added to the tree. At each iteration, it selects the cheapest edge that connects a
    vertex in the tree to a vertex outside the tree, and adds the new vertex to the tree.
"""
