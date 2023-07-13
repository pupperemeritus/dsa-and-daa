def is_valid(v, pos, path, graph):
    """
    Check if a vertex is valid to be added to the path.

    Args:
        v: The vertex to be checked.
        pos: The position of the vertex in the path.
        path: The current path of vertices.
        graph: The graph representing the connections between vertices.

    Returns:
        True if the vertex is valid, False otherwise.
    """
    return graph[path[pos - 1]][v] != 0 and v not in path


def hamiltonian_cycle_util(graph, path, pos, cycles):
    """
    Finds all Hamiltonian cycles in a graph.

    Args:
        graph (List[List[int]]): The graph represented as an adjacency matrix.
        path (List[int]): The current path being constructed.
        pos (int): The current position in the path.
        cycles (List[List[int]]): The list to store all the Hamiltonian cycles.

    Returns:
        None
    """
    # Base case: If all vertices have been visited and the last vertex is connected to the first vertex,
    # add the current path to the list of Hamiltonian cycles.
    if pos == len(graph) and graph[path[pos - 1]][path[0]] == 1:
        cycles.append(path.copy())
        return

    # Try all possible vertices as the next vertex in the path.
    for v in range(len(graph)):
        if is_valid(v, pos, path, graph):
            # Add the vertex to the path.
            path[pos] = v
            # Recursively find the next vertex in the path.
            hamiltonian_cycle_util(graph, path, pos + 1, cycles)
            # Remove the vertex from the path.
            path[pos] = -1


def hamiltonian_cycle(graph):
    """
    Finds all Hamiltonian cycles in a given graph.

    Args:
        graph (list): The adjacency matrix representation of the graph.

    Returns:
        list: A list of all Hamiltonian cycles in the graph.
    """
    # Initialize the path with -1 for all vertices
    path = [-1] * len(graph)
    # List to store all Hamiltonian cycles
    cycles = []
    # Start with the first vertex as the initial position in the path
    path[0] = 0
    # Call the helper function to find all Hamiltonian cycles
    hamiltonian_cycle_util(graph, path, 1, cycles)
    # Return the list of Hamiltonian cycles
    return cycles


# Example usage

if __name__ == "__main__":
    graph = [
        [0, 1, 1, 1, 0],
        [1, 0, 1, 0, 1],
        [1, 1, 0, 1, 0],
        [1, 0, 1, 0, 1],
        [0, 1, 0, 1, 0],
    ]

    cycles = hamiltonian_cycle(graph)
    print(cycles)
    graph = [
        [0, 1, 1, 0, 0, 0, 1, 0],
        [1, 0, 1, 0, 0, 0, 0, 1],
        [1, 1, 0, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0],
        [1, 0, 0, 0, 0, 1, 0, 1],
        [0, 1, 0, 0, 0, 0, 1, 0],
    ]
    cycles = hamiltonian_cycle(graph)
    print(cycles)
