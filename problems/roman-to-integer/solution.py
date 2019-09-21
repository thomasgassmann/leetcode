class Solution:
    value_map = {
        'M': 1000,
        'D': 500,
        'C': 100,
        'L': 50,
        'X': 10,
        'V': 5,
        'I': 1
    }

    def romanToInt(self, s: str) -> int:
        i = 0
        while s != '':
            index = 0
            current_val = self.value_map[s[index]]
            while len(s) - 1 > index and s[index] == s[index + 1]:
                current_val += self.value_map[s[index + 1]]
                index += 1
            if len(s) - 1 > index and self.value_map[s[index + 1]] > self.value_map[s[index]]:
                current_val = -current_val
            if current_val > 0:
                i += current_val
                s = s[index + 1:]
                continue

            i += self.value_map[s[index + 1]] + current_val
            s = s[index + 2:]
        return i


if __name__ == '__main__':
    print(Solution().romanToInt('MCMXCIV'))
