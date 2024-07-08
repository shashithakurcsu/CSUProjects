import heapq
import random


def dijkstra_basic(graph, start):
    priority_queue = [(0, start)]
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    visited = set()

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_vertex in visited:
            continue

        visited.add(current_vertex)

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


def update_graph_with_traffic(graph):
    traffic_factor = {
        'low': 1,
        'medium': 2,
        'high': 3
    }

    for vertex in graph:
        for neighbor in graph[vertex]:
            traffic_condition = random.choice(['low', 'medium', 'high'])
            original_weight = graph[vertex][neighbor]
            graph[vertex][neighbor] = original_weight * traffic_factor[traffic_condition]

    return graph


def dijkstra_optimized(graph, start):
    priority_queue = [(0, start)]
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    visited = set()

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_vertex in visited:
            continue

        visited.add(current_vertex)

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


# Example graph representation
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start_vertex = 'A'
distances_basic = dijkstra_basic(graph, start_vertex)
print(f"Shortest distances from {start_vertex} (Basic): {distances_basic}")

# Update the graph with simulated real-time traffic data
updated_graph = update_graph_with_traffic(graph.copy())

distances_optimized = dijkstra_optimized(updated_graph, start_vertex)
print(f"Shortest distances from {start_vertex} (Optimized with Traffic): {distances_optimized}")


