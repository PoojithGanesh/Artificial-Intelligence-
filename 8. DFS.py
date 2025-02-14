# Depth-First Search (DFS) implementation in Python

def dfs(graph, node, visited):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)

# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Set to keep track of visited nodes
visited = set()

# Start DFS from node 'A'
print("Depth-First Search traversal:")
dfs(graph, 'A', visited)
