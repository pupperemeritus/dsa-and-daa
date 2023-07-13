def is_safe(v, color, graph, colors):
    """
    Check if it is safe to assign a color to a vertex in a graph.

    Args:
        v (int): The vertex index.
        color (int): The color to be assigned.
        graph (List[List[int]]): The adjacency matrix representation of the graph.
        colors (List[int]): The list of colors assigned to the vertices.

    Returns:
        bool: True if it is safe to assign the color to the vertex, False otherwise.
    """
    return all(graph[v][i] == 0 or colors[i] != color for i in range(len(graph)))


def m_coloring_util(graph, m, colors, v, solutions):
    """
    Recursively finds all valid colorings of a given graph with a maximum of m colors.

    Args:
        graph (list): The adjacency matrix representation of the graph.
        m (int): The maximum number of colors.
        colors (list): The current color assignment for each vertex.
        v (int): The current vertex being colored.
        solutions (list): The list to store all valid colorings.

    Returns:
        None

    """
    # Base case: all vertices have been colored
    if v == len(graph):
        solutions.append(colors.copy())
        return

    # Try all possible colors for the current vertex
    for color in range(1, m + 1):
        if is_safe(v, color, graph, colors):
            colors[v] = color
            m_coloring_util(graph, m, colors, v + 1, solutions)
            colors[v] = 0


def m_coloring(graph, m):
    """
    Find all possible colorings of a graph using at most m colors.

    Args:
        graph (List[List[int]]): The graph represented as an adjacency matrix.
        m (int): The maximum number of colors to use.

    Returns:
        List[List[int]]: A list of all possible colorings of the graph.

    """
    # Initialize the colors list with 0s
    colors = [0] * len(graph)

    # List to store all the solutions
    solutions = []

    # Find all possible colorings
    m_coloring_util(graph, m, colors, 0, solutions)

    return solutions


if __name__ == "__main__":
    # Example usage
    graph = [
        [0, 1, 0, 0, 1],
        [1, 0, 1, 0, 1],
        [0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1],
        [1, 1, 0, 1, 0],
    ]
    m = 3
    solutions = m_coloring(graph, m)
    print(len(solutions))
    print(solutions)
