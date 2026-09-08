"""
Use a hashmap to count the occurrence of integer # integer -> occurences
Create a list of lists which each index is the frequency of this integer
Go in reverse order and append the character to res k many times

O(N)

O(N * M)
"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n,0)
        
        freq = [[] * i for i in range(len(nums))]

        for n, c in count.items():
            freq[c-1].append(n)
        
        res = []
        for i in range(len(freq)-1, -1, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res


