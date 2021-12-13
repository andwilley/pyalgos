from heapq import heappush, heappop

class TempIndex:
    def __init__(self, temp, index):
        self.temp = temp
        self.index = index

    def __lt__(self, other):
        return self.temp < other.temp

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        res = [0]*len(T)
        q = []

        for i, temp in enumerate(T):
            newTempIndex = TempIndex(temp, i)
            while q and q[0].temp < newTempIndex.temp:
                tempIndex = heappop(q)
                res[tempIndex.index] = newTempIndex.index - tempIndex.index
            heappush(q, newTempIndex)
        return res

