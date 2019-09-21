class FreqStack:

    def __init__(self):
        self._freq = {}
        self._group = {}
        self._maxfreq = 0

    def push(self, x: int) -> None:
        if x not in self._freq:
            self._freq[x] = 0
        self._freq[x] += 1
        f = self._freq[x]
        if f > self._maxfreq:
            self._maxfreq = f
        if f not in self._group:
            self._group[f] = []
        self._group[f].append(x)

    def pop(self) -> int:
        x = self._group[self._maxfreq].pop(-1)
        self._freq[x] -= 1
        if len(self._group[self._maxfreq]) == 0:
            self._maxfreq -= 1
        return x


if __name__ == '__main__':
    obj = FreqStack()
    obj.push(5)
    obj.push(7)
    obj.push(5)
    obj.push(7)
    obj.push(4)
    obj.push(5)
    print(obj.pop())
    print(obj.pop())
    print(obj.pop())
    print(obj.pop())
