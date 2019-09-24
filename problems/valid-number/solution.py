class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip(' ')
        try:
            float(s)
            return True
        except:
            return False


if __name__ == '__main__':
    print(Solution().isNumber('0'))
    print(Solution().isNumber(' 0.1 '))
    print(Solution().isNumber('abc'))
    print(Solution().isNumber('1 a'))
    print(Solution().isNumber('2e10'))
    print(Solution().isNumber(' -90e3   '))
    print(Solution().isNumber(' 1e'))
    print(Solution().isNumber('e3'))
    print(Solution().isNumber(' 6e-1'))
    print(Solution().isNumber(' 99e2.5 '))
    print(Solution().isNumber('53.5e93'))
    print(Solution().isNumber(' --6 '))
    print(Solution().isNumber('-+3'))
    print(Solution().isNumber('95a54e53'))
