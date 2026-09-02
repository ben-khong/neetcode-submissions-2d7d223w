"""
aab

a       aa      !aab
a  !ab   b
b   
"""
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        pali = []

        def dfs(i):
            if i >= len(s):
                res.append(pali.copy())
                return
            
            for j in range(i, len(s)):
                if self.isPali(s,i,j):
                    pali.append(s[i:j+1])
                    dfs(j+1)
                    pali.pop()
                
                    
        dfs(0)
        return res 

    def isPali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False 
            l += 1
            r -= 1
        return True


