class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        before = after = 1

        for i in range(len(nums)):
            res[i] *= before
            before *= nums[i]

        for j in range(len(nums)-1,-1,-1):
            res[j] *= after
            after *= nums[j]

        return res