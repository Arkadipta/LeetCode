# Problem statement:

A tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.

Given a tree of n nodes labelled from `0` to `n - 1`, and an array of `n - 1` edges where `edges[i] = [ai, bi]` indicates that there is an undirected edge between the two nodes ai and bi in the tree, you can choose any node of the tree as the root. When you select a node `x` as the root, the result tree has height `h`. Among all possible rooted trees, those with minimum height (i.e. `min(h)`)  are called minimum height trees (MHTs).

Return a list of all MHTs' root labels. You can return the answer in any order.

The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.

 

Example 1:

- Input: `n = 4, edges = [[1,0],[1,2],[1,3]]`
- Output: `[1]`
- Explanation: As shown, the height of the tree is `1` when the root is the node with label `1` which is the only MHT.

Example 2:

- Input: `n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]`
- Output: `[3,4]`

 

Constraints:

- `1 <= n <= 2 * 10^4`
- `edges.length == n - 1`
- `0 <= ai, bi < n`
- `ai != bi`
- All the pairs `(ai, bi)` are distinct.
- The given input is guaranteed to be a tree and there will be no repeated edges.

# Solution:

This solution only works because it is stated in the problem it is a connected acyclic graph. In this scenario, there can only be at-most two nodes for which the height is minimum. These nodes are the centers of the graph.

1. Create an adjacency matrix (`adj`) from the edges. While doing so, also note the number of edges connected to a particular node in a list `degree`
2. Start removing leaf nodes from the graph, where `degree[i] == 1` till only two or less nodes remain.

```python
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
```