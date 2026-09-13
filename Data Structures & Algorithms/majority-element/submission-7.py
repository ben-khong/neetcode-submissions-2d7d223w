"""

nums=[1,2,3,2,2,2,5,4,2]
"""
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        res = 0

        for n in nums:
            if count == 0:
                res = n

            if n == res:
                count += 1
            else:
                count -= 1
            
        return res
            


        

            
        
