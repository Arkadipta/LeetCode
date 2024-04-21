from typing import List
from collections import defaultdict
def validPath(n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        def build_adjacency_list(edges):
            store = defaultdict(list)
            for n1, n2 in edges:
                store[n1].append(n2)
                store[n2].append(n1)

            return store

        store = build_adjacency_list(edges)
        stack = [source]
        visited = set()
        while len(stack) > 0:
            current = stack.pop()
            if current == destination:
                return True
            if current in visited:
                continue
            visited.add(current)
            for edges in store[current]:
                stack.append(edges)

        return False