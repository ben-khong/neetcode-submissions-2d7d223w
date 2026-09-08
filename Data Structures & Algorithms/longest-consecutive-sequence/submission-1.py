"""
nums=[2,20,4,10,3,5]

while loop i

"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0

        for n in nums:
            if n-1 in nums:
                continue 
            else:
                i = 1
                while n + i in nums:
                    i += 1
                res = max(res, i)
        return res

