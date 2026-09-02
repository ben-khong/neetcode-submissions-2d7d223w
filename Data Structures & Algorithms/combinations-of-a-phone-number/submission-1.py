class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
            
        res = []
        combo = []

        phoneMap = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }

        def dfs(i):
            if i >= len(digits):
                res.append("".join(combo.copy()))
                return
            
            for letter in phoneMap[digits[i]]:
                combo.append(letter)
                dfs(i+1)
                combo.pop()
        dfs(0)
        return res 