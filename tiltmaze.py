from collections import deque

"""
given a graph
output minimum number of moves to get to the output
goal could be anywhere
"""

class Node:
    def __init__(self, row, col, cnt = -1):
        self.row = row
        self.col = col
        self.point = (row, col)
        self.count = cnt

    @classmethod
    def fromPoint(self, point, cnt = -1):
        return self(point[0], point[1], cnt)

    def __eq__(self, other):
        return self.point == other.point

    def __hash__(self):
        return hash(self.point)

layout = [
    [0, 0, 1, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 2, 0, 1],
]

# create a adjacency matrix
# adjacent nodes are a "slide" apart
# for every node
# try left right up down and go as far as you can in that direction.
# check for goal at destination and check for goal along the way
# BFS

moves = [
    (-1, 0), # up
    (1, 0), # down
    (0, 1), # right
    (0, -1), #left
]

start = (0, 0)

def add(a, b):
    return (a[0] + b[0], a[1] + b[1])

def is_in_bounds(pos, graph):
    return (0 <= pos[0] < len(graph)) and (0 <= pos[1] < len(graph[0]))

def gen_next_nodes(start, moves, graph):
    goal = None
    for move in moves:
        pos = start
        while is_in_bounds(add(pos, move), graph) and \
                graph[add(pos, move)[0]][add(pos, move)[1]] in (0, 2):
            pos = add(pos, move)
            if graph[pos[0]][pos[1]] == 2:
                goal = pos
        if pos != start:
            yield pos, goal

# bfs
def tilt_bfs(start, graph):
    q = deque([])
    seen = set([])

    q.append(Node.fromPoint(start, 0))
    while q:
        curr_node = q.popleft()
        seen.add(curr_node.point)
        for next_point in gen_next_nodes(curr_node.point, moves, graph):
            next_node = Node.fromPoint(next_point[0], curr_node.count + 1)
            if next_point[1]:
                # goal found
                return next_node.count, next_point[1]
            if next_node.point not in seen and next_node not in q:
                q.append(next_node)
    return -1

# print("ans:", tilt_bfs(start, layout))


# recursive dfs

def rec_dfs(point, graph, seen):
    # base
    if graph[point[0]][point[1]] == 2:
        return point
    seen.add(point)
    print("call", point)
    for next_point in gen_next_nodes(point, moves, graph):
        print("***level", point)
        print("next", next_point[0])
        if next_point[1]:
            return next_point[1]
        if next_point[0] not in seen:
            res = rec_dfs(next_point[0], graph, seen)
            if res != -1:
                return res
    return -1

print(rec_dfs((0, 0), layout, set([])))
