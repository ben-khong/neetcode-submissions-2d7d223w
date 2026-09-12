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
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k

            