def createCycle (rows, cols) :
    res = [[0 for _ in range(cols)] for _ in range(rows)]
    l, r, t, d = [0, cols - 1, 0, rows - 1]
    count = 1
    while l <= r and t <= d :
        for j in range (l, r + 1) :
            res[t][j] = count
            count += 1
        t += 1
        if t > d :
            break

        for i in range (t, d + 1) :
            res[i][r] = count
            count += 1
        r -= 1
        if l > r :
            break

        for j in range(r, l - 1, -1) :
            res[d][j] = count
            count += 1
        d -= 1
        if t > d :
            break

        for i in range (d, t - 1, -1) :
            res[i][l] = count
            count += 1
        l += 1
        if l > r:
            break
    return res
print(createCycle(5, 3))