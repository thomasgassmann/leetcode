from typing import List


class LargerNumKey(str):
    def __lt__(x, y):
        return x+y > y+x


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        strs = map(str, nums)
        sorted_strs = ''.join(sorted(strs, key=LargerNumKey))
        return '0' if sorted_strs[0] == '0' else sorted_strs


if __name__ == '__main__':
    print(Solution().largestNumber([3, 30, 34, 5, 9]))
