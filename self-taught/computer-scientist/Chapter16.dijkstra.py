import heapq
from typing import Dict, Any


def dijkstra(graph: Dict[Any, Dict[Any, float]], starting_vertex: Any) -> Dict[Any, float]:
	"""Compute shortest path distances from `starting_vertex` to all other vertices.

	Parameters:
	- graph: adjacency representation: {vertex: {neighbor: weight, ...}, ...}
	- starting_vertex: source vertex key

	Returns:
	- distances: dict mapping each vertex to its shortest distance from source

	The implementation uses a min-priority queue (heap) and follows the
	classic Dijkstra algorithm (non-negative edge weights required).
	"""

	# Initialize distances to infinity, except the start vertex (0)
	distances: Dict[Any, float] = {vertex: float('infinity') for vertex in graph}
	distances[starting_vertex] = 0

	# Priority queue of (distance, vertex). heapq is a min-heap by first tuple item.
	pq = [(0, starting_vertex)]

	while pq:
		current_distance, current_vertex = heapq.heappop(pq)

		# If we have already found a better path to current_vertex, skip
		if current_distance > distances[current_vertex]:
			continue

		# Relaxation step for all neighbors of the current vertex
		for neighbor, weight in graph[current_vertex].items():
			distance = current_distance + weight
			# If a shorter path to neighbor is found, update and push to heap
			if distance < distances.get(neighbor, float('infinity')):
				distances[neighbor] = distance
				heapq.heappush(pq, (distance, neighbor))

	return distances


if __name__ == '__main__':
	# Example graph as adjacency dictionary
	graph = {
		'A': {'B': 2, 'C': 6},
		'B': {'D': 5},
		'C': {'D': 8},
		'D': {},
	}

	# Compute shortest distances from 'A'
	distances = dijkstra(graph, 'A')
	print('Shortest distances from A:')
	for vertex, dist in distances.items():
		print(f"  {vertex}: {dist}")