class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(cur, open_count, close_count):
            if len(cur) == n * 2:
                res.append("".join(cur))
                return

            if open_count < n:
                cur.append("(")
                dfs(cur, open_count + 1, close_count)
                cur.pop()

            if close_count < open_count:
                cur.append(")")
                dfs(cur, open_count, close_count + 1)
                cur.pop()

        dfs([], 0, 0)
        return res