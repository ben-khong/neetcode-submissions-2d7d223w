"""
update nums to not include integers with the val
return k which is the number of elem in nums that arent equal to val (len of nums)

By in-place, does that mean no extra lists

while i less than len nums
    another variable j which equals i 
    while j less than len of nums character at j index equals val
        j += 1
    set nums of i equal to nums of j
    set i equals j + 1
    
O(N)
"""
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        while i < len(nums):
            j = i
            while j + 1 < len(nums) and nums[j] == val:
                j += 1
            nums[i], nums[j] = nums[j], nums[i]
            i += 1

        res = 0
        for c in nums:
            if c == val:
                return res
            res += 1
        return res