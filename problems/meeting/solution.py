class Solution:

    def length(self, item):
        hour, minute = item.split(':')
        time = int(hour) * 60 + int(minute)
        return time

    def compare(self, a, b):
        time_a = self.length(a)
        time_b = self.length(b)
        return 1 if time_a > time_b else (0 if time_a == time_b else -1)

    def mini(self, a, b):
        return b if self.compare(a, b) > 0 else a

    def maxi(self, a, b):
        return a if self.compare(a, b) >= 0 else b

    def free_at(self, sched, bound, i):
        if i == 0:
            if self.compare(sched[i][0], bound[0]) == 1:
                return [bound[0], sched[i][0]]
            return None

        if len(sched) <= i:
            from_time = sched[len(sched) - 1][1]
            to_time = bound[1]
            if self.compare(from_time, to_time) == -1:
                return [from_time, to_time]
            return None

        from_time = sched[i - 1][1]
        to_time = sched[i][0]
        if self.compare(from_time, to_time) == 0:
            return None
        return [from_time, to_time]

    def reconc(self, a, b):
        from_time = self.maxi(a[0], b[0])
        to_time = self.mini(a[1], b[1])
        if self.compare(to_time, from_time) != 1:
            return None

        return [from_time, to_time]

    def meeting(self, sched_a, bound_a, sched_b, bound_b):
        free_times = []
        a_i = 0
        b_i = 0

        while True:
            # get free time of a
            # compare availablility with b
            # if yes, add to free_times, move forward
            free_a_slot = self.free_at(sched_a, bound_a, a_i)
            if free_a_slot is not None:
                while True:
                    free_b_slot = self.free_at(sched_b, bound_b, b_i)
                    if b_i != len(sched_b):
                        b_i += 1

                    if free_b_slot is None:
                        continue

                    res = self.reconc(free_a_slot, free_b_slot)
                    if res is None or self.compare(free_b_slot[0], free_a_slot[1]) >= 0:
                        break
                    free_times.append(res)
                    break

            if a_i == len(sched_a) and b_i == len(sched_b):
                break
            a_i += 1

        return free_times


if __name__ == '__main__':
    # problem from https://youtu.be/3Q_oYDQ2whs
    person_a = [['9:00', '10:30'], ['12:00', '13:00'], ['16:00', '18:00']]
    bound_a = ['8:00', '20:00']
    person_b = [['10:00', '11:30'], ['12:30', '14:30'],
                ['14:30', '15:00'], ['16:00', '17:00']]
    bound_b = ['8:00', '18:30']
    a = Solution().meeting(person_a, bound_a, person_b, bound_b)
    print(a)
