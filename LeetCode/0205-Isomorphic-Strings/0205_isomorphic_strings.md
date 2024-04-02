# Problem statement:

Given two strings `s` and `t`, determine if they are isomorphic.

Two strings `s` and `t` are isomorphic if the characters in `s` can be replaced to get `t`.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

 

Example 1:

- Input: `s = "egg", t = "add"`
- Output: `true`

Example 2:

- Input: `s = "foo", t = "bar"`
- Output: `false`

Example 3:

- Input: `s = "paper", t = "title"`
- Output: `true`

 

Constraints:

- `1 <= s.length <= 5 * 104`
- `t.length == s.length`
- `s` and `t` consist of any valid ascii character.

# Solution:

1. Initialize a hashmap
2. Iterating over the characters in `s` and `t`
   1. Check if character from `s`, `char_s` is in store, if not `store[char_s] = char_t`  
   2. If it is in store, check if its value matches with the character from `t`, if not return `False`
3. Repeat step 2 but instead by matching characters from `t` to `s`
4. If no return is triggered, return `True` at the end. 