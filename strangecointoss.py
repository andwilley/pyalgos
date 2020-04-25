class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        from functools import lru_cache
        
        @lru_cache(None)
        def dfs(i, left):
            if left < 0 or len(prob) - i < left:
                return 0
            if i >= len(prob):
                return 1
            return prob[i] * dfs(i+1, left-1) + (1-prob[i]) * dfs(i+1, left)
        
        return dfs(0, target)
