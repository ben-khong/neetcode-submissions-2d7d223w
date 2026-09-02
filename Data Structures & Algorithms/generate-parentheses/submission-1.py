class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []

        def dfs(openP, closeP):
            if len(stack) == (n * 2):
                res.append("".join(stack))
                return

            if openP < n:
                stack.append("(")
                dfs(openP+1,closeP)
                stack.pop()


            if closeP < openP:
                stack.append(")")
                dfs(openP,closeP+1)
                stack.pop()

        dfs(0,0)
            
        return res

