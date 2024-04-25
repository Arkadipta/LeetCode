from typing import List
from collections import deque


def openLock(deadends: List[str], target: str) -> int:
    def increment(current, target):
        result = []
        current2 = [int(x) for x in current]

        for i, val in enumerate(current2):
            result.append(current[:i] + str((val + 1) % 10) + current[i + 1 :])
            result.append(current[:i] + str((val - 1) % 10) + current[i + 1 :])

        return result

    if "0000" in deadends:
        return -1

    queue = deque([[0, "0000"]])
    count = 0
    deadends_set = set(deadends)
    visited = set()
    end = ["0000"]

    while len(queue) > 0:
        count, code = queue.popleft()
        if code == target:
            return count

        if code in visited:
            continue

        visited.add(code)
        next_moves = increment(code, target)

        for next_move in next_moves:
            if next_move not in deadends_set and next_move not in visited:
                queue.append([count + 1, next_move])

    return -1
