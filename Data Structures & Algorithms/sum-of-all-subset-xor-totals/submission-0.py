class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0
        subset = []
        def dfs(i):
            nonlocal res
            if i >= len(nums):
                curSum = 0
                for n in subset:
                    curSum ^= n
                res += curSum
                return

            subset.append(nums[i])
            dfs(i+1)

            subset.pop()
            dfs(i+1)

        dfs(0)
        return res