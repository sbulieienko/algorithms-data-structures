import heapq
from typing import Dict, Any, List, Optional


def shortest_path(graph: Dict[Any, Dict[Any, float]], start: Any, target: Any) -> Optional[List[Any]]:
	"""Возвращает кратчайший путь от `start` до `target` с помощью алгоритма Дейкстры.

	Если путь существует, возвращается список вершин [start, ..., target].
	Если пути нет, возвращается None.

	graph: {vertex: {neighbor: weight, ...}, ...}
	"""

	# Рекорд расстояний и предков
	distances: Dict[Any, float] = {v: float('infinity') for v in graph}
	previous: Dict[Any, Any] = {}

	distances[start] = 0
	pq = [(0, start)]

	while pq:
		current_distance, u = heapq.heappop(pq)
		if current_distance > distances[u]:
			continue

		# Если дошли до цели — можем прервать ранне
		if u == target:
			break

		for neighbor, weight in graph.get(u, {}).items():
			alt = current_distance + weight
			if alt < distances.get(neighbor, float('infinity')):
				distances[neighbor] = alt
				previous[neighbor] = u
				heapq.heappush(pq, (alt, neighbor))

	# Если целевая вершина недостижима
	if distances.get(target, float('infinity')) == float('infinity'):
		return None

	# Восстановление пути от target к start
	path: List[Any] = []
	node = target
	while node != start:
		path.append(node)
		node = previous.get(node)
		if node is None:
			# нет предка — путь не найден
			return None
	path.append(start)
	path.reverse()
	return path


if __name__ == '__main__':
	graph = {
		'A': {'B': 2, 'C': 6},
		'B': {'D': 5, 'C': 1},
		'C': {'D': 8},
		'D': {},
	}

	print(shortest_path(graph, 'A', 'D'))  # пример: ожидаемый маршрут ['A', 'B', 'D']