
# ASSESSMENT 3.4
# GRAPH - SEDANO

from collections import deque


class Graph:

    def __init__(self):

        self.graph = {
            'S': ['E', 'D'],
            'E': ['S', 'A', 'N', 'D'],
            'D': ['S', 'O', 'E'],
            'A': ['E'],
            'N': ['E', 'O'],
            'O': ['N', 'D']
        }

    # BFS Traversal
    def bfs(self, start):

        visited = set()
        queue = deque([start])

        visited.add(start)
        result = []

        while queue:

            vertex = queue.popleft()
            result.append(vertex)

            for neighbor in self.graph[vertex]:

                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return result

    # DFS Traversal
    def dfs(self, start):

        visited = set()
        result = []

        def search(vertex):

            visited.add(vertex)
            result.append(vertex)

            for neighbor in self.graph[vertex]:

                if neighbor not in visited:
                    search(neighbor)

        search(start)

        return result


# Main Program
if __name__ == "__main__":

    graph = Graph()

    print("GRAPH: SEDANO")
    print("-------------------------")

    print("Vertices: S, E, D, A, N, O")

    print("Edges:")
    print("S-E, S-D, E-A, E-N, N-O, D-O, E-D")

    print("\nBFS Traversal:")
    print(" -> ".join(graph.bfs('S')))

    print("\nDFS Traversal:")
    print(" -> ".join(graph.dfs('S')))

    print("\nProgram executed successfully!")
