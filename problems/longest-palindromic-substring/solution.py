class Solution(object):
    def exand_palindrome(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return r - l - 1

    def longestPalindrome(self, s):
        if s is None or len(s) <= 1:
            return s

        longest_start, longest_end = 0, 0
        for i in range(len(s)):
            len_1 = self.exand_palindrome(s, i, i)
            len_2 = self.exand_palindrome(s, i, i + 1)
            max_len = max(len_1, len_2)
            if (max_len > longest_end - longest_start):
                longest_start = int(i - (max_len - 1) / 2)
                longest_end = int(i + max_len / 2)
        return s[longest_start:longest_end + 1]


if __name__ == '__main__':
    print(Solution().longestPalindrome('bb'))
