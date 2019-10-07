from typing import List


class Solution:
    def get_points_on(self, points: List[List[int]], m: float, b: float) -> int:
        return sum([1 if point[0] * m + b == point[1] else 0 for point in points])

    def get_m_b(self, p_1, p_2):
        x_diff = (p_2[0] - p_1[0])
        if x_diff == 0:
            return (None, None)

        m = (p_2[1] - p_1[1]) / x_diff
        b = p_1[1] - m * p_1[0]
        return (m, b)

    def maxPoints(self, points: List[List[int]]) -> int:
        max_points = 0
        if len(points) == 1:
            return 1

        for i in range(len(points)):
            for j in range(len(points)):
                if i == j:
                    continue

                (m, b) = self.get_m_b(points[i], points[j])
                if m is not None and b is not None:
                    points_on = self.get_points_on(points, m, b)
                else:
                    points_on = len(list(filter(
                        lambda x: x[0] == points[i][0], points)))

                if points_on > max_points:
                    max_points = points_on
        return max_points


if __name__ == '__main__':
    print(Solution().maxPoints(
        [[3, 1], [12, 3], [3, 1], [-6, -1]]))
    print(Solution().maxPoints(
        [[1, 1], [2, 2], [3, 3]]))
    print(Solution().maxPoints(
        [[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]))
