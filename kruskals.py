from typing import List


class Edge:
    def __init__(self, src, dest, weight):
        self.src = src
        self.dest = dest
        self.weight = weight

    def __repr__(self):
        return f"{self.src} - {self.dest} : {self.weight}"


class Subset:
    """A helper class for tracking subsets in Kruskal's algorithm."""

    def __init__(self, parent: int, rank: int):
        """Initialize the subset with a parent and rank."""
        self.parent = parent
        self.rank = rank


def find(subsets, i):
    """
    Finds the parent of a given subset.

    Args:
        subsets (list): A list of subset objects.
        i (int): The index of the subset to find the parent of.

    Returns:
        int: The parent index of the given subset.
    """

    # If the parent of the current subset is not the subset itself,
    # recursively call find() to find the parent.
    if subsets[i].parent != i:
        subsets[i].parent = find(subsets, subsets[i].parent)

    # Return the parent index of the current subset.
    return subsets[i].parent


def union(subsets, x, y):
    """
    Merges two subsets into a single subset.

    Args:
        subsets (List[Subset]): List of subsets.
        x (int): Root node of first subset.
        y (int): Root node of second subset.

    Returns:
        None

    Description:
        This function takes in a list of subsets, and two root nodes x and y. It then merges the two subsets
        containing x and y into a single subset. If the rank of the subset containing x is smaller than the rank
        of the subset containing y, then the subset containing x is made a child of the subset containing y.
        If the rank of the subset containing y is smaller than the rank of the subset containing x, then the subset
        containing y is made a child of the subset containing x. If the ranks of the two subsets are the same,
        then one subset is made a child of the other, and the rank of the root of the new subset is incremented by 1.
    """
    xroot = find(subsets, x)
    yroot = find(subsets, y)

    if subsets[xroot].rank < subsets[yroot].rank:
        subsets[xroot].parent = yroot
    elif subsets[xroot].rank > subsets[yroot].rank:
        subsets[yroot].parent = xroot
    else:
        subsets[yroot].parent = xroot
        subsets[xroot].rank += 1


def kruskals(num_vertices: int, edges: List[Edge]) -> None:
    """Runs Kruskal's algorithm on a graph given its number of vertices and edges.

    Args:
        num_vertices: The number of vertices in the graph.
        edges: A list of Edge objects representing the edges of the graph.

    Returns:
        None. The results are printed to the console.
    """

    # Initialize variables
    edge_count = 0
    subsets = [Subset(i, 0) for i in range(num_vertices)]
    results = [None] * num_vertices

    # Sort edges by weight
    edges.sort(key=lambda e: e.weight)

    # Iterate over edges
    for edge in edges:
        # Find the subsets of the source and destination vertices
        x = find(subsets, edge.src)
        y = find(subsets, edge.dest)

        # If the subsets are different, add the edge to the results and union the subsets
        if x != y:
            results[edge_count] = edge
            union(subsets, x, y)
            edge_count += 1

            # If we have found a spanning tree, break out of the loop
            if edge_count == num_vertices - 1:
                break

    # Print the results
    print("Edge  : Weight")
    min_cost = 0
    for i in range(edge_count):
        print(f"{results[i].src} - {results[i].dest} : {results[i].weight}")
        min_cost += results[i].weight

    print(f"Cost = {min_cost}")
    return results


if __name__ == "__main__":
    V = 5
    graphEdges = [
        Edge(0, 1, 50),
        Edge(0, 2, 20),
        Edge(0, 4, 65),
        Edge(1, 4, 10),
        Edge(2, 0, 15),
        Edge(2, 3, 25),
        Edge(3, 1, 12),
        Edge(4, 3, 18),
    ]
    res = kruskals(V, graphEdges)
    print(res)


"""
1. Sort all the edges in non-decreasing order of their weight.
2. Pick the smallest edge. Check if it forms a cycle with the spanning tree formed so far (initially, the tree will be empty). If cycle is not formed, include this edge. Else, discard it.
3. Repeat step 2 until there are (V-1) edges in the spanning tree, where V is the number of vertices in the graph.
"""
