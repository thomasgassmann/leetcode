class Solution:
    def numDecodings(self, s: str) -> int:
        combinations = [None] * (len(s) + 1)
        combinations[0], combinations[1] = 1, 0 if int(s[0]) == 0 else 1
        for i in range(2, len(s) + 1):
            current, currentWithPrevious = int(s[i - 1]), int(s[i - 2:i])
            combinations[i] = combinations[i - 1] if current != 0 else 0
            if currentWithPrevious >= 10 and currentWithPrevious <= 26:
                combinations[i] += combinations[i - 2]

        return combinations[len(s)]
            

if __name__ == '__main__':
    print(Solution().numDecodings('226')) # 22 6, 2 26, 2 2 6
