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

    def dfs(self, vertex):
        """
        Perform depth-first search (DFS) starting from the given vertex.

        Parameters:
            vertex (Any): The starting vertex for the DFS.

        Returns:
            None

        Description:
            This function performs depth-first search (DFS) starting from the given vertex. It uses a stack to keep track of the vertices to visit next. The DFS traversal result is stored in the 'dfs_res' attribute of the class.

            The algorithm works as follows:
            1. Initialize an empty stack and an empty list to store the DFS traversal result.
            2. Push the starting vertex onto the stack.
            3. Create a 'visited' dictionary to keep track of visited vertices. Initially, all vertices are marked as unvisited.
            4. Mark the starting vertex as visited.
            5. While the stack is not empty:
                - Pop a vertex from the stack.
                - Append the popped vertex to the DFS traversal result list.
                - For each neighbor of the popped vertex:
                    - If the neighbor is not visited:
                        - Push the neighbor onto the stack.
                        - Mark the neighbor as visited.
            6. Store the final DFS traversal result in the 'dfs_res' attribute of the class.
        """
        stack = []
        dfs_res = []
        stack.append(vertex)
        visited = {x: False for x in self.vertedge.keys()}
        visited[vertex] = True
        while stack:
            s = stack.pop()
            dfs_res.append(s)
            for i in self.vertedge[s]:
                if visited[i] is False:
                    stack.append(i)
                    visited[i] = True
        self.dfs_res = dfs_res

    def isConnected(self):
        """
        Checks if the graph is connected.

        Returns:
            bool: True if the graph is connected, False otherwise.
        """
        print(list(self.vertedge.keys())[0])
        self.dfs(list(self.vertedge.keys())[0])
        print(self.dfs_res)
        return set(self.vertedge.keys()) == set(self.dfs_res)


if __name__ == "__main__":
    g = Graph()
    g.insert(1, [2, 5])
    g.insert(2, [3, 4, 5])
    g.insert(3, [4, 6])
    g.insert(4, [5, 2, 3, 6])
    g.insert(5, [1, 2, 4])
    g.insert(6, [3, 4])
    # g.insert(1, [2])
    # g.insert(3, [4])
    print(g.isConnected())
