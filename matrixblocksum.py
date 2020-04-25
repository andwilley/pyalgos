import numpy as np
from typings import List

class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        arr = np.array(mat)
        clamp_w_hi = lambda hi: lambda num: max(0, min(num, hi))
        clamp_i = clamp_w_hi(len(mat))
        clamp_j = clamp_w_hi(len(mat[0]))

        return [[np.sum(arr[clamp_i(i-K):clamp_i(i+K+1),clamp_j(j-K):clamp_j(j+K+1)]) for j, _ in enumerate(row)] for i, row in enumerate(mat)]

