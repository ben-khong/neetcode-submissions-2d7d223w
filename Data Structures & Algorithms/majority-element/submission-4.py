"""

nums=[1,2,3,2,2,2,5,4,2]
"""
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        res = nums[0]

        for n in nums:
            if n == res:
                count += 1
            else:
                count -= 1
                if count == 0:
                    count += 1
                    res = n
            
        return res
            


        

            
        
