class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        nums = sorted(candidates)
        res = []
        subset = []

        def dfs(total, i):
            if total == target:
                res.append(subset.copy())
                return
            if i >= len(nums) or total > target:
                return 

            subset.append(nums[i])
            dfs(total+nums[i], i+1)
        
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1

            subset.pop()
            dfs(total, i+1)

        dfs(0,0)
        return res

