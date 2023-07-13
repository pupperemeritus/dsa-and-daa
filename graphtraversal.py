class Graph:
    def __init__(self):
        self.vertedge = {}

    def insert(self, vertice, edge):
        if vertice not in self.vertedge.keys():
            self.vertedge[vertice] = []
        self.vertedge[vertice] += edge
        for i in edge:
            if i not in self.vertedge.keys():
                self.vertedge[i] = []

    def bfs(self, vertex):
        """
        Perform a breadth-first search starting from the given vertex.

        Args:
            vertex: The starting vertex.
        """
        queue = []
        queue.append(vertex)

        # Initialize visited dictionary
        visited = {x: False for x in self.vertedge.keys()}
        visited[vertex] = True

        while queue:
            # Dequeue vertex from queue
            s = queue.pop(0)
            print(s)

            # Enqueue all adjacent vertices of s
            for i in self.vertedge[s]:
                if visited[i] is False:
                    queue.append(i)
                    visited[i] = True

    def dfs(self, vertex):
        """
        Perform depth-first search starting from the given vertex.

        Args:
            vertex (str): The starting vertex for the depth-first search.

        Returns:
            None
        """
        # Initialize stack with the starting vertex
        stack = [vertex]

        # Initialize visited dictionary with all vertices as False
        visited = {x: False for x in self.vertedge.keys()}

        # Mark the starting vertex as visited
        visited[vertex] = True

        # Perform depth-first search
        while stack:
            # Pop the top vertex from the stack
            s = stack.pop()

            # Print the visited vertex
            print(s)

            # Iterate through the adjacent vertices
            for i in self.vertedge[s]:
                # If the adjacent vertex is not visited, add it to the stack and mark it as visited
                if visited[i] is False:
                    stack.append(i)
                    visited[i] = True


if __name__ == "__main__":
    g = Graph()
    g.insert(1, [2, 5])
    g.insert(2, [3, 4, 5])
    g.insert(3, [4, 6])
    g.insert(4, [5, 2, 3, 6])
    g.insert(5, [1, 2, 4])
    g.insert(6, [3, 4])
    print("BFS : ")
    g.bfs(1)
    print("DFS : ")
    g.dfs(1)
