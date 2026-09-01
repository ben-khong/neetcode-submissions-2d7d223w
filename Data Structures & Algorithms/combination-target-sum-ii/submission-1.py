class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def dfs(cur, total, i):
            if total == target:
                res.append(cur.copy())
                return 
            if i >= len(candidates) or total > target:
                return 
        
            cur.append(candidates[i])
            dfs(cur, total + candidates[i], i+1)

            while i+1<len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            
            cur.pop()
            dfs(cur, total, i+1)

        dfs([],0,0)
        return res
