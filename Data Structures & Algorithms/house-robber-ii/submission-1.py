"""
[3,4,3] -> 4
[2,9,8,3,6] -> 15
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
            
        def robPartition(arr):
            rob1 = rob2 = 0
            for n in arr:
                temp = max(rob1+n,rob2)
                rob1 = rob2
                rob2 = temp
            return rob2
        return max(robPartition(nums[1:]), robPartition(nums[:len(nums)-1]))
