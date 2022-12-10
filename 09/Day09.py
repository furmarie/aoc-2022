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
                (h_x, h_y) = tails_pos[0]

                match direction:
                    case "U":
                        h_y += 1

                    case "D":
                        h_y -= 1

                    case "L":
                        h_x -= 1

                    case "R":
                        h_x += 1

                tails_pos[0] = (h_x, h_y)
                
                for i in range(1, num_tails + 1):
                    x_sign = -1 if (tails_pos[i - 1][0] - tails_pos[i][0]) < 0 else 1
                    x_offset = abs(tails_pos[i - 1][0] - tails_pos[i][0])

                    y_sign = -1 if (tails_pos[i - 1][1] - tails_pos[i][1]) < 0 else 1
                    y_offset = abs(tails_pos[i - 1][1] - tails_pos[i][1])

                    dx, dy = 0, 0
                    
                    if x_offset > 1:
                        dx += 1
                        if y_offset > 0:
                            dy += 1
                    elif y_offset > 1:
                        dy += 1
                        if x_offset > 0:
                            dx += 1

                    tails_pos[i] = (tails_pos[i][0] + x_sign * dx, tails_pos[i][1] + y_sign * dy)

                ans.add(tails_pos[-1])

    return len(ans)

def main():
    print(f"Part 1: {solve(1)}")
    print(f"Part 2: {solve(9)}")

if __name__ == '__main__':
    main()
