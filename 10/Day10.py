def solve_1():
    with open("input.txt", "r") as f:
        instructions = [l.rstrip() for l in f.readlines()]

    ans = 0
    cycles = 0
    X = 1

    def cycle():
        nonlocal ans, cycles
        cycles += 1
        ans += cycles * X * (cycles % 40 == 20)

    for l in instructions:
        inst = l.split()

        cycle()
        if inst[0] == 'addx':
            cycle()
            X += int(inst[1])

    return ans


def solve_2():
    with open("input.txt", "r") as f:
        instructions = [l.rstrip() for l in f.readlines()]

    ans = ""
    cycles = 0
    X = 1

    def cycle():
        nonlocal ans, cycles
        ans += "#" if (abs(X - (cycles % 40)) < 2) else " "
        cycles += 1

    for l in instructions:
        inst = l.split()

        cycle()
        if inst[0] == 'addx':
            cycle()
            X += int(inst[1])

    res = "\n"

    for i in range(0, 220, 40):
        res += ans[i: i + 40] + '\n'

    return res


def main():
    print(f"Part 1: {solve_1()}")
    print(f"Part 2: {solve_2()}")


if __name__ == '__main__':
    main()
