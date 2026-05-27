class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        cur = nums[0]
        maxi = nums[0]

        for i in range(1, len(nums)):

            cur = max(nums[i], nums[i] + cur)

            maxi = max(maxi, cur)

        return maxi