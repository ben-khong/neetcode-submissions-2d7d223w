class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        combo = []


        def dfs(i):
            if len(combo) == k:
                res.append(combo.copy())
                return 
            
            for j in range(i, n+1):
                combo.append(j)
                dfs(j+1)
                combo.pop()
        
        dfs(1)
        return res
            
  


                
            
