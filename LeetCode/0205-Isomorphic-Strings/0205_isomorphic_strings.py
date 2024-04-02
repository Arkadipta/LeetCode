def isIsomorphic(s: str, t: str) -> bool:
    store = {}
    for char_s, char_t in zip(s, t):
        if char_s in store:
            if store[char_s] != char_t:
                return False
        else:
            store[char_s] = char_t
    store = {}
    for char_s, char_t in zip(s, t):
        if char_t in store:
            if store[char_t] != char_s:
                return False
        else:
            store[char_t] = char_s
    return True