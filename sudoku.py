def printf(grid):
    for i in grid:
        for j in i:
            print(j, end=" ")
        print()


def issutable(x, y, val):
    if val not in grid[x]:
        return all(val != grid[i][y] for i in range(9))
    return False


def used_in_box(arr, row, col, num):
    for i in range(3):
        for j in range(3):
            if (arr[i + row][j + col] == num):
                return True
    return False


def solver():
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                for val in range(1, 10):
                    if issutable(i, j, val) and used_in_box(grid, i, j, val):
                        grid[i][j] = val
                        solver()
                        grid[i][j] = 0
                return
    printf(grid)
    x = input()


grid = [[2, 5, 0, 0, 3, 0, 9, 0, 1], [0, 1, 0, 0, 0, 4, 0, 0, 0],
        [4, 0, 7, 0, 0, 0, 2, 0, 8], [0, 0, 5, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 9, 8, 1, 0, 0], [0, 4, 0, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 3, 6, 0, 0, 7, 2], [0, 7, 0, 0, 0, 0, 0, 0, 3],
        [9, 0, 3, 0, 0, 0, 6, 0, 4]]

solver()
