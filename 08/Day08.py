def solve_1():
    with open("input.txt", "r") as f:
        mat = [l.rstrip() for l in f.readlines()]
        mat = [list(map(int, x)) for x in mat]

    n, m = len(mat), len(mat[0])
    vis = [[0 for _ in range(m)] for _ in range(n)]

    for i in range(n):
        mx = -1
        for j in range(m):
            if mat[i][j] > mx:
                vis[i][j] = 1
                mx = mat[i][j]
        mx = -1
        for j in range(m - 1, -1, -1):
            if mat[i][j] > mx:
                vis[i][j] = 1
                mx = mat[i][j]               
        
    for j in range(m):
        mx = -1
        for i in range(n):
            if mat[i][j] > mx:
                vis[i][j] = 1
                mx = mat[i][j]
        mx = -1
        for i in range(n - 1, -1, -1):
            if mat[i][j] > mx:
                vis[i][j] = 1
                mx = mat[i][j]       

    print("Part 1: ", sum(sum(x) for x in vis))


def solve_2():
    ans = 0

    with open("input.txt", "r") as f:
        mat = [l.rstrip() for l in f.readlines()]
        mat = [list(map(int, x)) for x in mat]

    n, m = len(mat), len(mat[0])

    def go(x, y, dx, dy):
        res = 0
        nx, ny = x + dx, y + dy
        while 0 <= nx < n and 0 <= ny < m:
            res += 1
            if mat[nx][ny] >= mat[x][y]:
                break
            nx = nx + dx
            ny = ny + dy

        return res                

    for i in range(1, n - 1):
        for j in range(1, m - 1):
            curr = go(i, j, 0, -1) * go(i, j, 1, 0) * go(i, j, 0, 1) * go(i, j, -1, 0)
            ans = max(ans, curr)
    
    print("Part 2: ", ans)


def main():
    solve_1()
    solve_2()


if __name__ == '__main__':
    main()
