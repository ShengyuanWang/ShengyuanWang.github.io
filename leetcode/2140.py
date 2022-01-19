class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        
        n = len(questions)
        dp = [0] * n
        for i in range(n-1, -1, -1):
            end = i + questions[i][1] + 1
            dp[i] = questions[i][0]
            if end < n:
                dp[i] = questions[i][0] + dp[end]
            if i < n-1:
                dp[i] = max(dp[i], dp[i+1])
        return dp[0]

        