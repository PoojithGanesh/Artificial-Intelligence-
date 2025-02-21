from queue import PriorityQueue

def a_star_algorithm(graph, start, goal, heuristic):
    open_set = PriorityQueue()
    open_set.put((0, start))  # (cost, node)
    came_from = {}  # To reconstruct the path
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0
    f_score = {node: float('inf') for node in graph}
    f_score[start] = heuristic[start]

    while not open_set.empty():
        current_cost, current = open_set.get()

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]  # Return reversed path

        for neighbor, cost in graph[current].items():
            tentative_g_score = g_score[current] + cost

            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + heuristic[neighbor]
                open_set.put((f_score[neighbor], neighbor))

    return None  # No path found

# Example graph (adjacency list representation)
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1, 'E': 3},
    'E': {'D': 3}
}

# Example heuristic values (estimated cost to goal 'E')
heuristic = {
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 1,
    'E': 0
}

# Finding the shortest path from 'A' to 'E'
path = a_star_algorithm(graph, 'A', 'E', heuristic)
print("Shortest path:", path)
