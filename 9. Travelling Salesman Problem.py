from itertools import permutations

def tsp(graph, start):
    vertices = list(graph.keys())
    vertices.remove(start)  # Remove the start node from other vertices
    min_cost = float('inf')
    best_path = []

    # Generate all possible permutations of the vertices
    for perm in permutations(vertices):
        current_path = [start] + list(perm) + [start]  # Complete cycle
        current_cost = sum(graph[current_path[i]][current_path[i + 1]] for i in range(len(current_path) - 1))

        # Update minimum cost and path
        if current_cost < min_cost:
            min_cost = current_cost
            best_path = current_path

    return best_path, min_cost

# Example Graph as an adjacency dictionary (distance between cities)
graph = {
    'A': {'A': 0, 'B': 10, 'C': 15, 'D': 20},
    'B': {'A': 10, 'B': 0, 'C': 35, 'D': 25},
    'C': {'A': 15, 'B': 35, 'C': 0, 'D': 30},
    'D': {'A': 20, 'B': 25, 'C': 30, 'D': 0}
}

# Starting node
start_city = 'A'

# Solve TSP
best_route, min_cost = tsp(graph, start_city)

print("Optimal Route:", " -> ".join(best_route))
print("Minimum Cost:", min_cost)
