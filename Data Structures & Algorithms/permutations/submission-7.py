"""
Algorithm: Backtracking DFS 

dfs helper func that takes in an index. if index is greater than or equal to len of nums append copy of nums to res and exit

for loop with j index to iterate from i to len(nums)
    swap nums of j and nums i 
    run the dfs with with i + 1 (setting the nums[i] as a permanent num) 
    swap back
"""
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(i):
            if i >= len(nums):
                res.append(nums.copy())
                return 
            for j in range(i, len(nums)):
                nums[i], nums[j] = nums[j], nums[i]
                dfs(i+1)
                nums[i], nums[j] = nums[j], nums[i]
        dfs(0)
        return res
            
