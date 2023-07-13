import numpy as np


class Vertex:
    def __init__(self, key, freq):
        self.key = key
        self.freq = freq

    def __repr__(self):
        return f"Key : {self.key} : Freq : {self.freq}"


def Sum(vertices, i, j):
    """
    Calculate the sum of the frequencies of vertices from index i to index j.

    Parameters:
    - vertices (list): A list of vertices.
    - i (int): The starting index.
    - j (int): The ending index.

    Returns:
    - s (int): The sum of the frequencies of vertices from index i to index j.
    """
    s = 0
    for k in range(i, j + 1):
        s += vertices[k].freq
    return s


import numpy as np


def obst(vertices):
    """
    Calculates the minimum cost of constructing a binary search tree from a given set of vertices.

    Args:
        vertices (list): List of vertices

    Returns:
        float: Minimum cost of constructing the binary search tree
    """
    n = len(vertices)
    cost_mat = np.zeros((n + 1, n + 1))

    def cost_rec(vertices, i, j):
        """
        Recursive helper function to calculate the minimum cost of constructing a binary search tree.

        Args:
            vertices (list): List of vertices
            i (int): Start index of the subarray
            j (int): End index of the subarray

        Returns:
            float: Minimum cost of constructing the binary search tree for the subarray
        """
        if cost_mat[i, j]:
            return cost_mat[i, j]
        Min = np.inf
        fsum = Sum(vertices, i, j)
        for k in range(i, j + 1):
            c = cost_rec(vertices, i, k - 1) + cost_rec(vertices, k + 1, j)
            c += fsum
            if c < Min:
                Min = c
                cost_mat[i, j] = c

        return cost_mat[i, j]

    return cost_rec(vertices, 0, n - 1)


def make_vertex_list(keys, freqs):
    """
    Generates a list of Vertex objects based on the given keys and frequencies.

    Parameters:
        keys (list): A list of keys representing the vertices.
        freqs (list): A list of frequencies for each vertex.

    Returns:
        list: A sorted list of Vertex objects.
    """
    vertices = []
    for i in range(len(keys)):
        vertices.append(Vertex(keys[i], freqs[i]))
    vertices.sort(key=lambda x: x.key)
    return vertices


if __name__ == "__main__":
    keys = [10, 20, 30, 40]
    freqs = [4, 2, 6, 3]
    # keys = [10, 12, 20]
    # freqs = [34, 8, 50]
    vertices = make_vertex_list(keys, freqs)
    print(obst(vertices))
