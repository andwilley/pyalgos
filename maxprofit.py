import math
from functools import reduce

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return reduce(lambda acc, price: (min(acc[0], price), max(acc[1], price - acc[0])), prices, (math.inf, 0))[1]

#         lowest = math.inf
#         biggest_diff = 0

#         for price in prices:
#             lowest = min(lowest, price)
#             biggest_diff = max(biggest_diff, price - lowest)

#         return biggest_diff
