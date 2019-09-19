class Solution:
    def reverse(self, x: int) -> int:
        val = int(str(abs(x))[::-1])
        signed = val if x > 0 else -val
        return signed if val < 2 ** 31 else 0


if __name__ == '__main__':
    print(Solution().reverse(123))
    print(Solution().reverse(-123))
    print(Solution().reverse(-0))
    print(Solution().reverse(1563847412))
