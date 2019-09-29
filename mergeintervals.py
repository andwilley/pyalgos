class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])
        if intervals:
            res = [intervals[0]]
        else:
            return []

        for interval in intervals[1:]:
            if interval[0] <= res[-1][1]:
                res[-1] = [min(interval[0], res[-1][0]), max(interval[1], res[-1][1])]
            else:
                res.append(interval)

        return res