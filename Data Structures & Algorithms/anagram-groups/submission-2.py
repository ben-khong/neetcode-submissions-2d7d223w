class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_map = defaultdict(list)
        for string in strs:
            key = [0] * 26
            for c in string:
                key[ord(c)-ord('a')] += 1
            key = tuple(key)
            my_map[key].append(string)
        return list(my_map.values())
            

