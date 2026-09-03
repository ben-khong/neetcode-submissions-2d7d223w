class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        target = sum(nums) / k
        used = [False] * len(nums)

        def dfs(i,k,curSum):
            if k == 0:
                return True
            if curSum == target:
                return dfs(0,k-1,0)

            for j in range(i, len(nums)):
                if used[j] or curSum + nums[j] > target:
                    continue
                used[j] = True
                if dfs(j+1,k,curSum+nums[j]):
                    return True
                used[j] = False

                if curSum == 0:
                    return False
            return False

        return dfs(0,k,0)

