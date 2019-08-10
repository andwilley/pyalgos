from collections import deque

BLOCKED_SPACE = 'D'
GOAL = 'X'

class Node:
    def __init__(self, coord, parent):
        self.coord = coord
        self.parent = parent

    def __hash__(self):
        return hash(self.coord)

    def __eq__(self, other):
        return other == self.coord


input = [
    [ 0,  0, 0, 'D', 'X'],
    ['D', 0, 0, 'D',  0],
    ['D', 0, 0, 'D',  0],
    [ 0,  0, 0,  0,   0],
    [ 0,  0, 0,  0,  'D'],
]

# (y, x)
directions = (
    (-1, 0), # up
    (1, 0), # down
    (0, -1), # left
    (0, 1), # right
)

def get_moves(grid, current_node):
    for dir in directions:
        addy, addx = dir
        y, x = current_node.coord
        newy, newx = y + addy, x + addx
        # make sure the new point is on the grid and isn't a blocked space
        if 0 <= newy < len(grid) and 0 <= newx < len(grid[1]) and grid[newy][newx] != BLOCKED_SPACE:
            yield Node((newy, newx), current_node)

def find_shortest_path(grid):
    visited = set([])
    unvisited = deque([])

    unvisited.appendleft(Node((0, 0), None))

    # bfgs because w/ step size of 1, bfs is optimal
    while unvisited:
        current_node = unvisited.pop()
        visited.add(current_node)
        y, x = current_node.coord
        if grid[y][x] == GOAL:
            return get_path_from_node(current_node)
        for move in get_moves(grid, current_node):
            if move not in visited:
                unvisited.appendleft(move)
    return None

def get_path_from_node(node):
    path = deque([])
    path.appendleft(node.coord)
    while node.parent:
        path.appendleft(node.parent.coord)
        node = node.parent
    return path
