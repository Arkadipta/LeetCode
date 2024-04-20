from typing import List


def findFarmland(land: List[List[int]]) -> List[List[int]]:
    def dfs(i: int, j: int, visited: dict, result: list, res: list) -> None:

        if i < 0 or i >= len(land) or j < 0 or j >= len(
                land[0]) or land[i][j] == 0:
            return False

        if f"{i}-{j}" in visited:
            return visited[f"{i}-{j}"]

        ress = dfs(i+1, j, visited, result, res), dfs(i, j+1, visited, result, res)
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
