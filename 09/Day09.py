def solve(num_tails):
    with open("input.txt", "r") as f:
        ans = set()
        num_tails = num_tails
        tails_pos = [(0, 0) for _ in range(num_tails + 1)]

        def dist(a, b):
            return (pow(b[0] - a[0], 2) + pow(b[1] - a[1], 2))

        for l in f.readlines():
            direction, n_moves = l.rstrip().split()            

            for _ in range(int(n_moves)):
                h_pos = tails_pos[0]

                match direction:
                    case "U":
                        h_pos = (h_pos[0], h_pos[1] + 1)

                    case "D":
                        h_pos = (h_pos[0], h_pos[1] - 1)

                    case "L":
                        h_pos = (h_pos[0] - 1, h_pos[1])

                    case "R":
                        h_pos = (h_pos[0] + 1, h_pos[1])

                tails_pos[0] = h_pos
                
                for i in range(1, num_tails + 1):
                    if dist(tails_pos[i], tails_pos[i - 1]) >= 3: 
                        if tails_pos[i][0] != tails_pos[i - 1][0] and tails_pos[i][1] != tails_pos[i - 1][1]:
                            dx = [1, 1, -1, -1]
                            dy = [1, -1, 1, -1]
                        else:
                            dx = [0, 1, 0, -1]
                            dy = [1, 0, -1, 0]

                        best = tails_pos[i]
                        for k in range(4):
                            nx = tails_pos[i][0] + dx[k]
                            ny = tails_pos[i][1] + dy[k]

                            if(dist((nx, ny), tails_pos[i - 1]) < dist(tails_pos[i - 1], best)):
                                best = (nx, ny)

                        tails_pos[i] = best

                ans.add(tails_pos[-1])

    return len(ans)

def main():
    print(f"Part 1: {solve(1)}")
    print(f"Part 2: {solve(9)}")

if __name__ == '__main__':
    main()
