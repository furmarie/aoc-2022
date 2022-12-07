def main():
    curr = 0
    ans = []
    with open("input.txt", "r") as f:
        for l in f.readlines():
            if l == '\n':
                ans.append(curr)
                curr = 0
                continue
            curr += int(l.rstrip('\r\n'))

    print("Part 1: ", max(ans))
    print("Part 2: ", sum(sorted(ans)[-3:]))

if __name__ == '__main__':
    main()
