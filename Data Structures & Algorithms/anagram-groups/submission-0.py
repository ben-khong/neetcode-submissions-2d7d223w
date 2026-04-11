class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for string in strs:
            password = [0] * 26
            for c in string:
                password[ord(c) - ord('a')] += 1
            password = tuple(password)
            hashmap[password].append(string)
        return list(hashmap.values())