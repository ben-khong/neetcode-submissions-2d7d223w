"""
 p         c-x
1 -> 2 -> 3 -> 4
          ^    |
          6 <- 5 
          x
• Treat array as nodes with index as pointers
• Find the intersection of slow and fast pointer in the cycle 
• Create a second slow pointer that will intersect with the originally slow pointer 
• This is because the distance from the intersection will be the same as the starting distance
to the intersection 

2 * (p + (c - x)) = p + c + (c - x)
2p + 2c -2x = p + 2c - x
p = x

p = distance before cycle
x = from the intersection point to the beginning of the cycle 
c = distance of the cycle

"""
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
        


