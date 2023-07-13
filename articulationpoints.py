class Graph:
    def __init__(self):
        self.vertedge = {}
        self.time = 0

    def insert(self, vertice, edge):
        if vertice not in self.vertedge.keys():
            self.vertedge[vertice] = []
        self.vertedge[vertice] += edge
        for i in edge:
            if i not in self.vertedge.keys():
                self.vertedge[i] = []

    def find_articulation_points(self):
        visited = {x: False for x in self.vertedge.keys()}  # Track visited vertices
        articulation_points = set()  # Set to store the articulation points

        # Recursive depth-first search function to find articulation points
        def dfs_articulation(node, parent, visited, low, disc, is_articulation):
            """
            Depth-first search algorithm to find articulation points in a graph.
            Args:
                node (int): The current node being visited.
                parent (int): The parent node of the current node.
                visited (dict): A dictionary to track visited nodes.
                low (dict): A dictionary to track the low value of each node.
                disc (dict): A dictionary to track the discovery time of each node.
                is_articulation (dict): A dictionary to track whether a node is an articulation point.
            Returns:
                None
            """
            visited[node] = True  # Mark the current node as visited
            disc[node] = self.time  # Set the discovery time of the current node
            low[node] = self.time  # Set the low value of the current node
            self.time += 1  # Increment the time

            child_count = 0  # Track the number of children of the current node

            # Explore all neighbors of the current node
            for neighbor in self.vertedge[node]:
                if not visited[neighbor]:  # If the neighbor is not visited
                    child_count += 1  # Increment the child count
                    dfs_articulation(
                        neighbor, node, visited, low, disc, is_articulation
                    )  # Recursively call the function for the neighbor

                    low[node] = min(
                        low[node], low[neighbor]
                    )  # Update the low value of the current node

                    if parent != -1 and low[neighbor] >= disc[node]:
                        is_articulation[node] = True
                    if parent == -1 and child_count > 1:
                        is_articulation[node] = True
                elif (
                    neighbor != parent
                ):  # If the neighbor is already visited and not the parent node
                    low[node] = min(
                        low[node], disc[neighbor]
                    )  # Update the low value of the current node

        low = {
            x: float("inf") for x in self.vertedge.keys()
        }  # Initialize the low values of all vertices with infinity
        disc = {
            x: float("inf") for x in self.vertedge.keys()
        }  # Initialize the discovery times of all vertices with infinity
        is_articulation = {
            x: False for x in self.vertedge.keys()
        }  # Initialize the is_articulation dictionary with False for all vertices

        # Iterate through all vertices in the graph
        for v in self.vertedge.keys():
            if not visited[v]:  # If the vertex is not visited
                dfs_articulation(
                    v, -1, visited, low, disc, is_articulation
                )  # Call the dfs_articulation function for the vertex

        # Add all vertices that are marked as articulation points to the set
        for v in self.vertedge.keys():
            if is_articulation[v]:
                articulation_points.add(v)

        return articulation_points  # Return the set of articulation points


if __name__ == "__main__":
    # Create a graph instance
    graph = Graph()

    # Insert vertices and edges into the graph
    graph.insert(0, [1, 2])
    graph.insert(1, [0, 2])
    graph.insert(2, [0, 1, 3, 4])
    graph.insert(4, [2, 5, 6])
    graph.insert(5, [4, 6]), graph.insert(6, [4, 5, 7]), graph.insert(7, [6])

    # Find the articulation points in the graph
    articulation_points = graph.find_articulation_points()

    print(articulation_points)
