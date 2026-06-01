class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curMax = curMin = nums[0]

        for i in range(1, len(nums)):
            n = nums[i]

            tempMax = max(n, curMax * n, curMin * n)
            curMin = min(n, curMax * n, curMin * n)
            curMax = tempMax

            res = max(res, curMax)

        return res
        