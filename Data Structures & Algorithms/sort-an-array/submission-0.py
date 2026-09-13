"""
[5, 4, 3, 2, 1]

[4, 5, 3, 2, 1]

[3, 4, 5, 2, 1]

[2, 3, 4, 5, 1]

[1, 2, 3, 4, 5]

can nums be empty or contain duplicates?

how big or small will nums be?

use a ranged based for loop w i index
    create a j pointer which will be i minus one
    while j >= 0 and curr num is smaller than nums of j 
        swap and subtract j 
return nums
"""
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        i = 0 
        while i < len(nums):
            j = i - 1
            b = i
            while j >= 0 and nums[j] > nums[i]:
                nums[j], nums[i] = nums[i], nums[j]
                j -= 1
                i -= 1
            i = b 
            i += 1
        return nums

            