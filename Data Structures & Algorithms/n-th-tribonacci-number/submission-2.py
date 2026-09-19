class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0

        dp = [0, 1, 1]
        i = 2
        while i < n:
            temp1 = dp[2]
            temp2 = dp[1]

            dp[2] = dp[2] + dp[1] + dp[0]
            
            dp[1] = temp1
            dp[0] = temp2
            i += 1
        
        return dp[2]