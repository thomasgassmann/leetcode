from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        best = current = nums[0]
        for i in range(1, len(nums)):
            current = max(nums[i], current + nums[i])
            best = max(best, current)
        return best


if __name__ == '__main__':
    Solution().maxSubArray([1, -10, 11])
