from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # need to check if this is a DAG
        # count the in-degree of each vertex,
        # which we need to do with edges
        # add those with 0 to the stack

        # for each edge, use key fst edge
        # append snd edge

        # then check for topological order

        incnt  = defaultdict(lambda : 0)
        outadj = defaultdict(list)
        for edge in prerequisites:
            outadj[edge[0]].append(edge[1])
            # makes sure nodes with no in degree get in the in count
            incnt[edge[0]] = incnt[edge[0]]
            # count the number of inbound edges
            incnt[edge[1]] += 1

        # add the nodes with 0 indegree
        stack = [key for key, val in incnt.items() if not val]
        res = []

        # dfs-ish
        while stack:
            cur = stack.pop()
            res.append(cur)
            for node in outadj[cur]:
                incnt[node] -= 1
                if incnt[node] == 0:
                    stack.append(node)
        return len(res) == len(incnt)