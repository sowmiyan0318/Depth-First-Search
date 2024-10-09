def dfs(graph, start):
    # Create a stack to store the nodes to be visited
    stack = [start]
    # Create a set to store the visited nodes
    visited = set()

    while stack:
        # Pop a node from the stack and mark it as visited
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            print(node, end=" ")

            # Push all unvisited neighbors of the current node onto the stack
            for neighbor, weight in enumerate(graph[node]):
                if weight > 0 and neighbor not in visited:
                    stack.append(neighbor)

# Example usage:
graph = [
    [0, 1, 1, 0, 0],
    [1, 0, 1, 1, 0],
    [1, 1, 0, 1, 1],
    [0, 1, 1, 0, 1],
    [0, 0, 1, 1, 0]
]
start_node = 0
print("Depth-First Search traversal starting from node", start_node, ":")
dfs(graph, start_node)
