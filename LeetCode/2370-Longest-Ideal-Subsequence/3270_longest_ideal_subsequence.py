def longestIdealString(self, s: str, k: int) -> int:
    tab = [0] * 128
    for char in s:
        i = ord(char)
        tab[i] = max(tab[i-k:i+k+1]) + 1
    return max(tab)


def longestIdealString2(self, s: str, k: int) -> int:
    def dfs(i, visited):
        if i == len(s) - 1:
            return 1
        if i in visited:
            return visited[i]
        res = 0
        for ii in range(i+1, len(s)):
            if abs(ord(s[ii]) - ord(s[i])) <= k:
                res = max(res, dfs(ii, visited))
        visited[i] = res + 1
        return visited[i]

    visited = {}
    result = []
    for i in range(len(s)):
        result.append(dfs(i, visited))
    return max(result)