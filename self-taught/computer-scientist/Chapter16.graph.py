class Vertex:
	"""Класс вершины графа.

	Атрибуты:
		key: уникальный идентификатор вершины (любой хешируемый объект)
		connections: словарь {Vertex: weight} — смежные вершины и веса ребер
	"""

	def __init__(self, key):
		self.key = key
		self.connections = {}

	def add_adj(self, vertex, weight=0):
		"""Добавляет ориентированное ребро от этой вершины к `vertex` с `weight`.

		Если ребро уже существует, оно перезаписывается новым весом.
		"""
		self.connections[vertex] = weight

	def get_connections(self):
		"""Возвращает итерируемый объект с соседними вершинами (ключи словаря)."""
		return self.connections.keys()

	def get_weight(self, vertex):
		"""Возвращает вес ребра до `vertex`. Бросит KeyError, если ребро отсутствует."""
		return self.connections[vertex]


class Graph:
	"""Простейшая реализация ориентированного графа на базе словаря вершин.

	vertex_dict хранит сопоставление ключ -> Vertex.
	Методы работают с ключами вершин (не с объектами Vertex), за исключением
	возврата самих объектов через `get_vertex`.
	"""

	def __init__(self):
		self.vertex_dict = {}

	def add_vertex(self, key):
		"""Создаёт новую вершину с идентификатором `key` и возвращает её.

		Если вершина с таким ключом уже существует, метод перезапишет её.
		"""
		new_vertex = Vertex(key)
		self.vertex_dict[key] = new_vertex
		return new_vertex

	def get_vertex(self, key):
		"""Возвращает объект `Vertex` по ключу или `None`, если не найден."""
		return self.vertex_dict.get(key)

	def add_edge(self, f, t, weight=0):
		"""Добавляет ориентированное ребро из вершины с ключом `f` в `t`.

		Автоматически создаёт вершины, если их ещё нет в графе.
		"""
		if f not in self.vertex_dict:
			self.add_vertex(f)
		if t not in self.vertex_dict:
			self.add_vertex(t)
		self.vertex_dict[f].add_adj(self.vertex_dict[t], weight)

	def get_vertices(self):
		"""Возвращает итерируемый объект с ключами всех вершин графа."""
		return self.vertex_dict.keys()


# Пример использования
if __name__ == '__main__':
	# Создаём граф и добавляем ребра
	g = Graph()
	g.add_edge('A', 'B', 5)
	g.add_edge('A', 'C', 3)
	g.add_edge('B', 'C', 2)
	g.add_edge('C', 'D', 4)

	# Печатаем вершины и их смежности
	for key in g.get_vertices():
		v = g.get_vertex(key)
		print(f"Vertex {v.key}:")
		for nbr in v.get_connections():
			print(f"\t-> {nbr.key} (weight={v.get_weight(nbr)})")