"""
Two hashmaps # c->occurrences
Two passes to populate each hashmap
return if they equal 

O(N), O(N)
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map_s = {}
        for c in s:
            if c not in map_s:
                map_s[c] = 1
            else:
                map_s[c] += 1

        map_t = {}
        for c in t:
            if c not in map_t:
                map_t[c] = 1
            else:
                map_t[c] += 1
        
        return map_s == map_t

