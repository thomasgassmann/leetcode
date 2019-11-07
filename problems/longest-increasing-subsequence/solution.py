class Solution(object):
    def lengthOfLIS(self, nums):
        if len(nums) < 2:
            return len(nums)

        dp = [0 for num in nums]
        dp[0] = 1
        max_len = 0
        for i in range(1, len(nums)):
            max_value = 0
            for j in range(i):
                if nums[i] > nums[j]:
                    max_value = max(max_value, dp[j])
            dp[i] = max_value + 1
            max_len = max(dp[i], max_len)
        return max_len


if __name__ == '__main__':
    print(Solution().lengthOfLIS([2, 2]))  # 2
    print(Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))  # 4
