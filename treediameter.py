from collections import deque, defaultdict
from heapq import heappush, heappop

class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        graph = self.build_graph(edges)
        _, max_len = self.dfs(graph, edges[0][0], -1, 0)
        return max_len

    @staticmethod
    def build_graph(edges):
        graph = defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]]
        return graph

    def dfs(self, graph, node, parent_len, max_so_far):
        child_lens = []
        msf = max_so_far
        for child in graph[node]:
            child_len, child_max = self.dfs(graph, child, max(child_lens + [parent_len + 1]), msf)
            heappush(child_lens, -(child_len + 1))
            msf = max(msf, child_max)
        longest = 0
        kids = child_lens.copy()
        heappush(child_lens, -(parent_len + 1))
        if len(child_lens) > 1:
            longest = -heappop(child_lens) + -heappop(child_lens)
        elif len(child_lens) == 1:
            longest = -heappop(child_lens)
        return -heappop(kids) if kids else 0, max(msf, longest)