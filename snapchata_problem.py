def fun(z):  # sourcery no-metrics

    a = [["1", "2", "3", "4", "5", "6", "7", "8", "9"], ["1", "2", "3", "4", "5", "6", "7", "8", "9"], ["1", "2", "3", "4", "5", "6", "7", "8", "9"], ["1", "2", "3", "4", "5", "6", "7", "8", "9"], ["1", "2", "3", "4",
                                                                                                                                                                                                      "5", "6", "7", "8", "9"], ["1", "2", "3", "4", "5", "6", "7", "8", "9"], ["1", "2", "3", "4", "5", "6", "7", "8", "9"], ["1", "2", "3", "4", "5", "6", "7", "8", "9"], ["1", "2", "3", "4", "5", "6", "7", "8", "9"]]

    b = [["1", "2", "3", "4", "5", "6", "7", "8", "9"], ["1", "2", "3", "4", "5", "6", "7", "8", "9"], ["1", "2", "3", "4", "5", "6", "7", "8", "9"], ["1", "2", "3", "4", "5", "6", "7", "8", "9"], ["1", "2", "3", "4",
                                                                                                                                                                                                      "5", "6", "7", "8", "9"], ["1", "2", "3", "4", "5", "6", "7", "8", "9"], ["1", "2", "3", "4", "5", "6", "7", "8", "9"], ["1", "2", "3", "4", "5", "6", "7", "8", "9"], ["1", "2", "3", "4", "5", "6", "7", "8", "9"]]
    x = [["1", "2", "3", "4", "5", "6", "7", "8", "9"], ["1", "2", "3", "4", "5", "6", "7", "8", "9"], ["1", "2", "3", "4", "5", "6", "7", "8", "9"], ["1", "2", "3", "4", "5", "6", "7", "8", "9"], ["1", "2", "3", "4",
                                                                                                                                                                                                      "5", "6", "7", "8", "9"], ["1", "2", "3", "4", "5", "6", "7", "8", "9"], ["1", "2", "3", "4", "5", "6", "7", "8", "9"], ["1", "2", "3", "4", "5", "6", "7", "8", "9"], ["1", "2", "3", "4", "5", "6", "7", "8", "9"]]

    i = 0
    f = 1
    while (i < 9):
        j = 0
        while (j < 9):
            if z[i][j] != ".":

                c = int(z[i][j])

                if i < 3 and j < 3:
                    if z[i][j] == x[0][c-1]:
                        x[0][c-1] = "."
                    else:
                        f = 0
                        break

                elif i < 3 and j > 2 and j < 6:
                    if z[i][j] == x[1][c-1]:
                        x[1][c-1] = "."
                    else:
                        f = 0
                        break

                elif i < 3 and j > 5 and j < 9:
                    if z[i][j] == x[2][c-1]:
                        x[2][c-1] = "."
                    else:
                        f = 0
                        break

                elif i > 2 and i < 6 and j < 3:
                    if z[i][j] == x[3][c-1]:
                        x[3][c-1] = "."
                    else:
                        f = 0
                        break

                elif i > 2 and i < 6 and j > 2 and j < 6:
                    if z[i][j] == x[4][c-1]:
                        x[4][c-1] = "."
                    else:
                        f = 0
                        break

                elif i > 2 and i < 6 and j > 5 and j < 9:
                    if z[i][j] == x[5][c-1]:
                        x[5][c-1] = "."
                    else:
                        f = 0
                        break

                elif i > 5 and i < 9 and j < 3:
                    if z[i][j] == x[6][c-1]:
                        x[6][c-1] = "."
                    else:
                        f = 0
                        break

                elif i > 5 and i < 9 and j > 2 and j < 6:
                    if z[i][j] == x[7][c-1]:
                        x[7][c-1] = "."
                    else:
                        f = 0
                        break

                elif z[i][j] == x[8][c-1]:
                    x[8][c-1] = "."
                else:
                    f = 0
                    break

                if z[i][j] == a[i][c-1] and z[i][j] == b[j][c-1]:
                    a[i][c-1] = "."
                    b[j][c-1] = "."
                else:

                    f = 0
                    break

            j += 1

        if f == 1:
            i += 1
        else:
            break

    return f == 1


print(fun([[".", ".", ".", ".", "5", ".", ".", "1", "."],
           [".", "4", ".", "3", ".", ".", ".", ".", "."],
           [".", ".", ".", ".", ".", "3", ".", ".", "1"],
           ["8", ".", ".", ".", ".", ".", ".", "2", "."],
           [".", ".", "2", ".", "7", ".", ".", ".", "."],
           [".", "1", "5", ".", ".", ".", ".", ".", "."],
           [".", ".", ".", ".", ".", "2", ".", ".", "."],
           [".", "2", ".", "9", ".", ".", ".", ".", "."],
           [".", ".", "4", ".", ".", ".", ".", ".", "."]]))
