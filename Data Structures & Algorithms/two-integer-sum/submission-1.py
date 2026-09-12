"""
hashmap # number->idx
range based for loop
if the difference (target minus current number) is a key in the map, then we'd return the two indicies
add the number index pair to map

O(N) O(N)
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_map = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in my_map:
                return [my_map[diff], i]
            my_map[nums[i]] = i
            