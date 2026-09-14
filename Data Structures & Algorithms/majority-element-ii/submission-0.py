class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        my_map = {}
        target = len(nums) / 3
        res = []

        for n in nums:
            my_map[n] = 1 + my_map.get(n, 0)
            if my_map[n] > target and n not in res:
                res.append(n)
        return res
