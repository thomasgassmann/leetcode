from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = []
        maxi = None
        for i in range(len(nums)):
            cur = nums[i]
            for j in range(len(nums) - i - 1):
                cur += nums[i + j + 1]
                if maxi is None or cur > maxi:
                    maxi = cur
        return maxi


if __name__ == '__main__':
    Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
