from typing import List
from collections import defaultdict, deque

def findMinHeightTrees(n: int, edges: List[List[int]]) -> List[int]:
    if n == 1:
        return [0]
    adj = defaultdict(list)
    degree = [0] * n
    for e1, e2 in edges:
        adj[e1].append(e2)
        adj[e2].append(e1)
        degree[e1] = degree[e1] + 1
        degree[e2] = degree[e2] + 1

    leaves = deque([i for i in range(n) if degree[i] == 1])
    nodes_left = n
    while nodes_left > 2:
        count = len(leaves)
        nodes_left = nodes_left - count
        for i in range(count):
            leaf = leaves.popleft()
            for neighbor in adj[leaf]:
                degree[neighbor] = degree[neighbor] - 1
                if degree[neighbor] == 1:
                    leaves.append(neighbor)

    return list(leaves)