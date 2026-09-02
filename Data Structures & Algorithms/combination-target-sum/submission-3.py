class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        def dfs(total, i):
            if total == target:
                res.append(subset.copy())
                return 
            if i >= len(nums) or total > target:
                return 
            
            subset.append(nums[i])
            dfs(total+nums[i], i)

            subset.pop()
            dfs(total, i+1)
        dfs(0,0)
        return res
        