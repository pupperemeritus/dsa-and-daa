import numpy as np


def next_node(dist: np.ndarray, visited: np.ndarray) -> int:
    """
    Find the index of the next unvisited node with minimum distance.

    Args:
        dist (np.ndarray): 1D array containing the distance from the start node
            to each node in the graph.
        visited (np.ndarray): 1D boolean array where visited[i] is True if node
            i has already been visited.

    Returns:
        int: Index of the next unvisited node with minimum distance.

    """
    # get the number of nodes
    n = len(dist)

    # set the minimum value to infinity and the minimum index to -1
    min_val = np.inf
    min_ind = -1

    # iterate through all the nodes
    for i in range(n):
        # check if the node has not been visited and its distance is less than the minimum value
        if not visited[i] and dist[i] < min_val:
            # update the minimum value and index
            min_val = dist[i]
            min_ind = i

    # return the index of the node with minimum distance
    return min_ind


import numpy as np


def dijkstra(graph: np.ndarray, src: int) -> list:
    """
    Applies Dijkstra's algorithm on a given graph to find the shortest path from a
    given source node to all other nodes in the graph.

    Args:
    - graph: a 2D numpy array representing the graph where each row and column
             represent a node and each cell represents the weight of the edge
             connecting the nodes.
    - src: an integer representing the index of the source node.

    Returns:
    - A list containing two 1D numpy arrays:
        - The first array represents the shortest distance from the source node to
          all other nodes.
        - The second array represents the previous node in the shortest path from
          the source node to all other nodes.
    """

    # Get number of nodes in graph
    n = len(graph[0])

    # Initialize arrays for distances, visited nodes, and previous nodes
    dist = np.full(n, np.inf, dtype=float)
    visited = np.zeros(n, dtype=bool)
    prev = np.full(n, np.nan, dtype=float)

    # Set distances from source node to all directly connected nodes
    for i in range(n):
        if graph[src][i] != 0:
            dist[i] = graph[src][i]

    # Set distance from source to itself as 0 and mark as visited
    dist[src] = 0
    visited[src] = True

    # Loop through each node in graph
    i = 0
    while i < n - 1:
        # Get the next node with the smallest distance that hasn't been visited
        u = next_node(dist, visited)
        if u < 0:
            i += 1
            continue

        # Mark node as visited
        visited[u] = True

        # Update distances to all unvisited nodes connected to current node
        for v in range(n):
            if not visited[v] and graph[u][v] != 0 and dist[v] > dist[u] + graph[u][v]:
                dist[v] = dist[u] + graph[u][v]
                prev[v] = u

        i += 1

    # Set previous node of source node as NaN and fill in any remaining NaN values
    prev[np.isnan(prev)] = src
    prev[src] = np.nan

    # Return list of distance and previous node arrays
    return [dist, prev]


if __name__ == "__main__":
    INF = np.inf
    graph = [
        [0, 50, 15, INF, 65],
        [INF, 0, INF, INF, 10],
        [20, INF, 0, 25, INF],
        [INF, 12, INF, 0, 18],
        [INF, INF, INF, INF, 0],
    ]

    dist, prev = dijkstra(graph, 0)
    print(dist)
    print(prev)
