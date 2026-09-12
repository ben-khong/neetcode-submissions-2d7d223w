"""
default dictionary of type list 
for loop to traverse every string in strs
    password (occurences of a particular character) 26 0s
    for c in s
        increment the index of where the character would be in the password
    convert password into a tuple 
    append s at password key
return dictionary's values as a list

O(N * M) M is the avg length of the str
O(26) -> O(N) Space complexity 
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_map = defaultdict(list)
        for s in strs:
            key = [0] * 26
            for c in s:
                key[ord(c)-ord('a')] += 1
            key = tuple(key)
            my_map[key].append(s)
        return list(my_map.values())
