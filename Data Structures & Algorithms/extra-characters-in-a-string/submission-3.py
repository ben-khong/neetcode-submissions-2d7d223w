class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        words = set(dictionary)
        cache = {len(s):0}

        def dfs(i):
            if i in cache:
                return cache[i]
            
            # skip the current character
            res = 1 + dfs(i+1)
            for j in range(i, len(s)):
                if s[i:j+1] in words:
                    res = min(res, dfs(j+1))
            cache[i] = res
            return res

        return dfs(0)
