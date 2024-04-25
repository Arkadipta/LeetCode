def tribonacci(self, n: int) -> int:
    t0, t1, t2 = 0, 1, 1
    if n == 0:
        return t0
    for i in range(n-2):
        t0, t1, t2 = t1, t2, t0 + t1 + t2
    return t2