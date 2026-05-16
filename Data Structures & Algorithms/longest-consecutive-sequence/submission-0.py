class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        dp={}
        for i in sorted(set(nums)):
            if i-1 in dp:
                dp[i] = dp[i-1] +1
            else:
                dp[i]=1
            res= max(res,dp[i])
        return res