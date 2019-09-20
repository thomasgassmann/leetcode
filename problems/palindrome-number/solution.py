class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or x % 10 == 0 and x != 0:
            return False

        reverted = 0
        while reverted < x:
            reverted = x % 10 + reverted * 10
            x //= 10
        return reverted == x or reverted // 10 == x


if __name__ == '__main__':
    print(Solution().isPalindrome(10))
    print(Solution().isPalindrome(121))
    print(Solution().isPalindrome(1221))
    print(Solution().isPalindrome(876))
    print(Solution().isPalindrome(0))
