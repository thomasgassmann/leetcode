from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        built = ''
        length = len(str(strs[0])) if len(
            strs) != 0 and len(strs[0]) > 0 else 0
        for i in range(length):
            equals = len(set([a[i] if len(a) > i else '' for a in strs])) == 1
            if not equals:
                break
            built += strs[0][i]
        return built


if __name__ == '__main__':
    print(Solution().longestCommonPrefix([]))
