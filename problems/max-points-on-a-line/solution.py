from typing import List
from collections import Counter
from decimal import Decimal

class Solution:

    def get_weight(self, p_1, p_2):
        if p_1[0] == p_2[0]:
            return None
        m = Decimal(p_2[1] - p_1[1]) / Decimal(p_2[0] - p_1[0])
        return m

    def maxPoints(self, points: List[List[int]]) -> int:
        max_points = 0
        n = len(points)
        counter = Counter([(x[0], x[1]) for x in points])
        points = list(counter.keys())
        if len(points) < 3:
            return n

        for i, p1 in enumerate(points):
            combinations = {}
            for p2 in points[i+1:]:
                weight = self.get_weight(p1, p2)
                if weight not in combinations:
                    combinations[weight] = counter.get(p1)
                combinations[weight] += counter.get(p2)
                if combinations[weight] > max_points:
                    max_points = combinations[weight]
        return max_points


if __name__ == '__main__':
    print(Solution().maxPoints(
        [[0,0],[94911151,94911150],[94911152,94911151]]))
    print(Solution().maxPoints(
        [[1,1],[1,1],[1,1]]))
    print(Solution().maxPoints(
        [[0, 0], [1, 1], [0, 0]]))
    print(Solution().maxPoints(
        [[560,248],[0,16],[30,250],[950,187],[630,277],[950,187],[-212,-268],[-287,-222],[53,37],[-280,-100],[-1,-14],[-5,4],[-35,-387],[-95,11],[-70,-13],[-700,-274],[-95,11],[-2,-33],[3,62],[-4,-47],[106,98],[-7,-65],[-8,-71],[-8,-147],[5,5],[-5,-90],[-420,-158],[-420,-158],[-350,-129],[-475,-53],[-4,-47],[-380,-37],[0,-24],[35,299],[-8,-71],[-2,-6],[8,25],[6,13],[-106,-146],[53,37],[-7,-128],[-5,-1],[-318,-390],[-15,-191],[-665,-85],[318,342],[7,138],[-570,-69],[-9,-4],[0,-9],[1,-7],[-51,23],[4,1],[-7,5],[-280,-100],[700,306],[0,-23],[-7,-4],[-246,-184],[350,161],[-424,-512],[35,299],[0,-24],[-140,-42],[-760,-101],[-9,-9],[140,74],[-285,-21],[-350,-129],[-6,9],[-630,-245],[700,306],[1,-17],[0,16],[-70,-13],[1,24],[-328,-260],[-34,26],[7,-5],[-371,-451],[-570,-69],[0,27],[-7,-65],[-9,-166],[-475,-53],[-68,20],[210,103],[700,306],[7,-6],[-3,-52],[-106,-146],[560,248],[10,6],[6,119],[0,2],[-41,6],[7,19],[30,250]]))
    print(Solution().maxPoints(
        [[3, 3], [1, 1], [2, 2]]))
    print(Solution().maxPoints(
        [[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]))
