# Problem statement:

There is a bi-directional graph with `n` vertices, where each vertex is labeled from `0` to `n - 1` (inclusive). The edges in the graph are represented as a 2D integer array edges, where each `edges[i] = [ui, vi]` denotes a bi-directional edge between vertex `ui` and vertex `vi`. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.

You want to determine if there is a valid path that exists from vertex source to vertex destination.

Given edges and the integers n, source, and destination, return true if there is a valid path from source to destination, or false otherwise.

 

Example 1:

- Input: `n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2`
- Output: `true`
- Explanation: There are two paths from vertex `0` to vertex `2`:
  - `0 → 1 → 2`
  - `0 → 2`

Example 2:

- Input: `n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5`
- Output: `false`
- Explanation: There is no path from vertex `0` to vertex `5`.

 

Constraints:

- `1 <= n <= 2 * 10^5`
- `0 <= edges.length <= 2 * 10^5`
- `edges[i].length == 2`
- `0 <= ui, vi <= n - 1`
- `ui != vi`
- `0 <= source, destination <= n - 1`
- There are no duplicate edges.
- There are no self edges.


# Solution:

1. Build an adjacency matrix from the list
2. Initialize an empty set `visited`
3. Run DFS from `source`, at each step check:
   1. If the node is the destination, if so return `True`
   2. If the node is already in visited, if so skip it
   3. If node is not destination and not visited, add it to visited and move on to the subsequent nodes
4. If the program execution reaches this far then the node can not be reached. Return `False`.


```python
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
```
