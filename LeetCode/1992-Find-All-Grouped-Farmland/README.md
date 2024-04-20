# Problem statement:

You are given a 0-indexed `m x n` binary matrix land where a `0` represents a hectare of forested land and a `1` represents a hectare of farmland.

To keep the land organized, there are designated rectangular areas of hectares that consist entirely of farmland. These rectangular areas are called groups. No two groups are adjacent, meaning farmland in one group is not four-directionally adjacent to another farmland in a different group.

land can be represented by a coordinate system where the top left corner of land is `(0, 0)` and the bottom right corner of land is `(m-1, n-1)`. Find the coordinates of the top left and bottom right corner of each group of farmland. A group of farmland with a top left corner at `(r1, c1)` and a bottom right corner at `(r2, c2)` is represented by the 4-length array `[r1, c1, r2, c2]`.

Return a 2D array containing the 4-length arrays described above for each group of farmland in land. If there are no groups of farmland, return an empty array. You may return the answer in any order.

 

Example 1:

- Input: `land = [[1,0,0],[0,1,1],[0,1,1]]`
- Output: `[[0,0,0,0],[1,1,2,2]]`
- Explanation:
  - The first group has a top left corner at `land[0][0]` and a bottom right corner at `land[0][0]`.
  - The second group has a top left corner at `land[1][1]` and a bottom right corner at `land[2][2]`.

Example 2:

- Input: `land = [[1,1],[1,1]]`
- Output: `[[0,0,1,1]]`
- Explanation:
  - The first group has a top left corner at `land[0][0]` and a bottom right corner at `land[1][1]`.

Example 3:

- Input: `land = [[0]]`
- Output: `[]`
- Explanation:
  - There are no groups of farmland.

 

Constraints:

- `m == land.length`
- `n == land[i].length`
- `1 <= m, n <= 300`
- land consists of only `0`'s and `1`'s.
- Groups of farmland are rectangular in shape.

# Solution:

1. Initialize a hash-map `visited`, and two result arrays `res` and `result`
2. Iterate through the `m x n` grid and check if `grid[i][j] == 1` and `(i,j)` not in visited
3. If so, append `(i, j)` to `res` and start a Depth-first search at `(i,j)` 
   1. If `i < 0` or `i >= len(land)` or `j < 0` or `j >= len(land[0])` or `land[i][j] == 0`, return `False`
   2. If `(i,j)` in visited, return `True`
   3. Else `check = dfs(i+1, j) or dfs(i, j+1)`
      1. Update visited
      2. If `check` is `False`, append `(i,j)` to `res` and append `res` to `result`
   4. Return True <- Very important and counter intuitive>
   5. Reset `res = []`
4. Return `result`


```python
def findFarmland(land: List[List[int]]) -> List[List[int]]:
    def dfs(i: int, j: int, visited: dict, result: list, res: list) -> None:
        if i < 0 or i >= len(land) or j < 0 or j >= len(land[0]) or land[i][j] == 0:
            return False
        if f"{i}-{j}" in visited:
            return visited[f"{i}-{j}"]

        res1, res2 = dfs(i+1, j, visited, result, res), dfs(i, j+1, visited, result, res)
        ress = res1 or res2
        visited[f"{i}-{j}"] = True

        if not ress:
            res.append(i)
            res.append(j)
            result.append(res.copy())
        return True
        
    visited = {}
    res, result = [], []

    for i in range(len(land)):
        for j in range(len(land[0])):
            if land[i][j] == 1 and f"{i}-{j}" not in visited:
                res.append(i)
                res.append(j)
                dfs(i, j, visited, result, res)
            res = []

    return result            

```