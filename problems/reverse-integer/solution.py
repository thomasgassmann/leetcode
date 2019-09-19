class Solution:
    def reverse(self, x: int) -> int:
        MAX = 2 ** 31 - 1
        MIN = -(2 ** 31)
        rev = 0
        abs_x = abs(x)
        while abs_x != 0:
            pop = abs_x % 10
            abs_x //= 10
            if rev > MAX / 10 or rev < MIN / 10:
                return 0
            rev = rev * 10 + pop
        return rev if x > 0 else -rev


if __name__ == '__main__':
    print(Solution().reverse(-123))
    print(Solution().reverse(123))
    print(Solution().reverse(-0))
    print(Solution().reverse(1563847412))
