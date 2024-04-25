# Problem statement:

You are given a string `s` consisting of lowercase letters and an integer `k`. We call a string `t` ideal if the following conditions are satisfied:

- `t` is a subsequence of the string `s`.
- The absolute difference in the alphabet order of every two adjacent letters in `t` is less than or equal to `k`.

Return the length of the longest ideal string.

A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.

Note that the alphabet order is not cyclic. For example, the absolute difference in the alphabet order of `'a'` and `'z'` is `25`, not `1`.

 

Example 1:

- Input: `s = "acfgbd", k = 2`
- Output: `4`
- Explanation: The longest ideal string is `"acbd"`. The length of this string is `4`, so `4` is returned.
Note that `"acfgbd"` is not ideal because `'c'` and `'f'` have a difference of `3` in alphabet order.

Example 2:

- Input: `s = "abcd", k = 3`
- Output: `4`
Explanation: The longest ideal string is `"abcd"`. The length of this string is `4`, so `4` is returned.

 

Constraints:

- `1 <= s.length <= 10^5`
- `0 <= k <= 25`
- `s` consists of lowercase English letters.


# Solution:

Like most subsequence problem, we can use DP to solve this. There are two different approach

## Recursive + Memoization Top-down DP approach:
1. Create a helper function `helper` to start recursion. It accepts `i`, the pointer of the character and the hash-map `visited`. This function computes the the longest ideal subsequence starting from the position `i`
   1. If `i == len(s) - 1`, it means that we are at the end of the string. The longest subsequence starting from `i` is then just `s[i]`. Thus return `1`.
   2. If `i` is already visited, return `visited[i]`
   3. Loop through the elements from `i` to `len(s)`. If the difference is less than `k`, compute `helper` again. Store the value in a list `res`.
   4. Get the maximum of this list.
   5. The longest ideal subsequence starting from `i` then is `max(res) + 1`
   6. Store this value with key `i` in visited and return
2. Loop through the letters in the string and run `helper`. Store the result in a list `result`
3. Return `max(result)`

## Tabulation Botom-up approach:
1. Initialize an array `tab` of zeros of length `128`
2. Loop over the characters in `s`
   1. Set `i = ord(s)`
   2. Then set `tab[i] = max(tab[i-k:i+k+1]) + 1`
3. Return `max(tab)`

This works because the array `tab` keeps track of the number of occurance of characters. `max(tab[i-k:i+k+1])` looks if the character being added can have a neighbour that are separated by `k`.


```python
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
```