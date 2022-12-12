from collections import deque
from string import ascii_lowercase


def solve():
    mat = []
    start_x, start_y = 0, 0
    dest_x, dest_y = 0, 0

    with open("input.txt", "r") as f:
        for i, l in enumerate(f.readlines()):
            l = l.rstrip()
            a = []
            for j, ch in enumerate(l):
                if ch == 'S':
                    start_x, start_y = i, j
                    a.append(0)
                elif ch == 'E':
                    dest_x, dest_y = i, j
                    a.append(25)
                else:
                    a.append(ascii_lowercase.index(ch))
            mat.append(a)

    n, m = len(mat), len(mat[0])
    q = deque([(dest_x, dest_y)])
    vis = [[-1 for _ in range(m)] for _ in range(n)]
    vis[dest_x][dest_y] = 0

    ans1, ans2 = -1, -1

    while q:
        x, y = q.popleft()

        if ans2 == -1 and mat[x][y] == 0:
            ans2 = vis[x][y]
            
        if (x, y) == (start_x, start_y):
            ans1 = vis[x][y]
            break

        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < m and mat[x][y] - mat[nx][ny] <= 1 and vis[nx][ny] == -1:
                vis[nx][ny] = vis[x][y] + 1
                q.append((nx, ny))

    return ans1, ans2


def main():
    print("Part 1: %d\nPart 2: %d" % solve())


if __name__ == '__main__':
    main()
