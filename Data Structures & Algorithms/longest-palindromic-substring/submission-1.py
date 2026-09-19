class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = 0
        left = right = 0
        for i in range(len(s)):
            l = r = i
            while 0 <= l and r < len(s) and s[l] == s[r]:
                if r - l + 1 > length:
                    length = r - l + 1
                    left = l
                    right = r
                l -= 1
                r += 1
            
            l, r = i, i+1
            while 0 <= l and r < len(s) and s[l] == s[r]:
                if r - l + 1 > length:
                    length = r - l + 1
                    left = l
                    right = r
                l -= 1
                r += 1
        
        return s[left:right+1]
        