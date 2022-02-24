class Cell:

    def __init__(self, x, y, dist) -> None:
        self.x = x
        self.y = y
        self.dist = dist


def isValid(dx, dy, N, visited):
    return 1 <= dx <= N and 1 <= dy <= N and not visited[dx][dy]


def myfun(start, end, N):
    dx = [2, 2, -2, -2, 1, 1, -1, -1]
    dy = [1, -1, -1, 1, 2, -2, 2, -2]
    queue = [Cell(start[0], start[1], 0)]
    visited = [[False for i in range(N + 1)] for _ in range(N + 1)]
    visited[start[0]][start[1]]
    while queue:
        t = queue.pop(0)
        if t.x == end[0] and t.y == end[1]:
            return t.dist
        for i in range(8):
            x = t.x + dx[i]
            y = t.y + dy[i]
            if isValid(x, y, N, visited):
                visited[x][y] = True
                queue.append(Cell(x, y, t.dist + 1))


start = [1, 1]
end = [15, 24]
print(myfun(start, end, 30))
