class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        window = []
        def dfs(openP, closeP):
            if openP == closeP == n:
                res.append("".join(window))
                return 
            
            if openP < n:
                window.append("(")
                dfs(openP+1, closeP)
                window.pop()

            if closeP < openP:
                window.append(")")
                dfs(openP, closeP+1)
                window.pop()

        dfs(0,0)
        return res