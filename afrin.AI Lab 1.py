import copy
from heapq import heappush, heappop

n = 3
row = [1, 0, -1, 0]
col = [0, -1, 0, 1]

class PriorityQueue:
    def __init__(self):
        self.heap = []

    def push(self, k):
        heappush(self.heap, (k.cost + k.level, k))

    def pop(self):
        return heappop(self.heap)[1]

    def empty(self):
        return not self.heap

class Node:
    def __init__(self, parent, mat, empty_tile_pos, cost, level):
        self.parent = parent
        self.mat = mat
        self.empty_tile_pos = empty_tile_pos
        self.cost = cost
        self.level = level

    def __lt__(self, nxt):
        return (self.cost + self.level) < (nxt.cost + nxt.level)

def calculateCost(mat, final):
    count = 0
    for i in range(n):
        for j in range(n):
            if mat[i][j] and mat[i][j] != final[i][j]:
                count += 1
    return count

def newNode(mat, empty_tile_pos, new_empty_tile_pos, level, parent, final):
    new_mat = copy.deepcopy(mat)
    x1, y1 = empty_tile_pos
    x2, y2 = new_empty_tile_pos
    new_mat[x1][y1], new_mat[x2][y2] = new_mat[x2][y2], new_mat[x1][y1]
    cost = calculateCost(new_mat, final)
    return Node(parent, new_mat, new_empty_tile_pos, cost, level)

def printMatrix(mat):
    for i in range(n):
        for j in range(n):
            print(f"{mat[i][j]} ", end="")
        print()
    print()

def isSafe(x, y):
    return 0 <= x < n and 0 <= y < n

def printPath(root):
    if root is None:
        return
    printPath(root.parent)
    printMatrix(root.mat)

def solve(initial, empty_tile_pos, final):
    cost = calculateCost(initial, final)
    root = Node(None, initial, empty_tile_pos, cost, 0)
    pq = PriorityQueue()
    pq.push(root)

    while not pq.empty():
        minimum = pq.pop()
        if minimum.cost == 0:
            print("Solution path:")
            printPath(minimum)
            return

        for i in range(4):
            new_x = minimum.empty_tile_pos[0] + row[i]
            new_y = minimum.empty_tile_pos[1] + col[i]
            if isSafe(new_x, new_y):
                child = newNode(minimum.mat, minimum.empty_tile_pos,
                                [new_x, new_y], minimum.level + 1, minimum, final)
                pq.push(child)

# Example usage
initial = [[1, 2, 3], [5, 6, 0], [7, 8, 4]]
final = [[1, 2, 3], [5, 8, 6], [0, 7, 4]]
empty_tile_pos = [1, 2]

solve(initial, empty_tile_pos, final)
print("Afrin.u  B.Tech AiDS")
