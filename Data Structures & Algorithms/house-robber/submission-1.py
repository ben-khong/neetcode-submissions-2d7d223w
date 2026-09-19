class Solution:
    def rob(self, nums: List[int]) -> int:
        before_prev = prev = 0
        for n in nums:
            temp = max(before_prev + n, prev)
            before_prev = prev
            prev = temp
        return prev