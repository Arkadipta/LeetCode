# Problem statement:

You have a lock in front of you with `4` circular wheels. Each wheel has `10` slots: `'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'`. The wheels can rotate freely and wrap around: for example we can turn `'9'` to be `'0'`, or `'0'` to be `'9'`. Each move consists of turning one wheel one slot.

The lock initially starts at `'0000'`, a string representing the state of the `4` wheels.

You are given a list of `deadends` dead ends, meaning if the lock displays any of these codes, the wheels of the lock will stop turning and you will be unable to open it.

Given a `target` representing the value of the wheels that will unlock the lock, return the minimum total number of turns required to open the lock, or `-1` if it is impossible.

 

Example 1:

- Input: `deadends = ["0201","0101","0102","1212","2002"], target = "0202"`
- Output: `6`
- Explanation: 
    A sequence of valid moves would be `"0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202"`.
    Note that a sequence like `"0000" -> "0001" -> "0002" -> "0102" -> "0202"` would be invalid,
    because the wheels of the lock become stuck after the display becomes the dead end `"0102"`.

Example 2:

- Input: `deadends = ["8888"], target = "0009"`
- Output: `1`
- Explanation: We can turn the last wheel in reverse to move from `"0000" -> "0009"`.

Example 3:

- Input: `deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888"`
- Output: `-1`
- Explanation: We cannot reach the target without getting stuck.

 

Constraints:

- `1 <= deadends.length <= 500`
- `deadends[i].length == 4`
- `target.length == 4`
- `target` will not be in the list `deadends`.
- `target` and `deadends[i]` consist of digits only.




# Solution:

1. To begin with if `"0000"` is in `deadends`, return `-1`
2. Start a BFS with `queue = [[0, "0000"]]` where the first value is the number of moves
   1. Get current by popping from left of the queue
   2. If current is target, return moves
   3. If current is in `visited` set, continue
   4. Add current into `visited` set.
   5. Get the next possible codes, which for `"0000"` is `["1000", "9000", "0100". "0900", "0010", "0090", "0001", "0009"]`
   6. Append them in queue while adding one to the number of moves
3. Return -1


```python
from typing import List
from collections import deque
def openLock(deadends: List[str], target: str) -> int:

    def increment(current, target):
        result = []
        current2 = [int(x) for x in current]

        for i, val in enumerate(current2):
            result.append(current[:i] + str((val + 1)%10) + current[i+1:])
            result.append(current[:i] + str((val - 1)%10) + current[i+1:])

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
                queue.append([count+1, next_move])

    return -1
```