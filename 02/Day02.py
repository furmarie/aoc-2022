def main():
    ans1, ans2 = 0, 0

    d = {'X' : 1, 'Y' : 2, 'Z' : 3}

    win = {'A' : 'Y', 'B' : 'Z', 'C' : 'X'}
    draw = {'A' : 'X', 'B' : 'Y', 'C' : 'Z'}
    lose = {'A' : 'Z', 'B' : 'X', 'C' : 'Y'}

    with open("input.txt", "r") as f:
        for l in f.readlines():
            a, b = l.rstrip().split()
            ans1 += d[b] + 3 * (draw[a] == b) + 6 * (win[a] == b)

            if b == 'X':
                ans2 += d[lose[a]]
            if b == 'Y':
                ans2 += d[draw[a]] + 3
            if b == 'Z':
                ans2 += d[win[a]] + 6


    print("Part 1: ", ans1)
    print("Part 2: ", ans2)


if __name__ == '__main__':
    main()
