
# ASSESSMENT 3.4
# BINARY TREE - SEDANO

from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def create_tree():
    root = Node('S')

    root.left = Node('E')
    root.right = Node('D')

    root.left.left = Node('A')
    root.left.right = Node('N')

    root.right.left = Node('O')

    return root


# BFS Traversal
def bfs(root):
    queue = deque([root])
    result = []

    while queue:
        node = queue.popleft()
        result.append(node.data)

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)

    return result


# DFS Traversal (Preorder)
def dfs(root):
    if root is None:
        return []

    return (
        [root.data]
        + dfs(root.left)
        + dfs(root.right)
    )


# Main Program
if __name__ == "__main__":

    tree = create_tree()

    print("BINARY TREE: SEDANO")
    print("-------------------------")

    print("        S")
    print("       / \\")
    print("      E   D")
    print("     / \\ /")
    print("    A  N O")

    print("\nBFS Traversal:")
    print(" -> ".join(bfs(tree)))

    print("\nDFS Traversal:")
    print(" -> ".join(dfs(tree)))

    print("\nProgram executed successfully!")
