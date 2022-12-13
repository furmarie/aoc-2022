from functools import cmp_to_key
import copy


def solve_1():
    with open("input.txt", "r") as f:
        lines = f.readlines()

    ans1 = 0

    def check_order(a, b):
        if isinstance(a, int) and isinstance(b, list):
            a = [a]

        if isinstance(a, list) and isinstance(b, int):
            b = [b]

        val = 0
        while a or b:
            val = 0
            if not b:
                return -1
            if not a:
                return 1

            a1 = a.pop(0)
            b1 = b.pop(0)

            if isinstance(a1, int) and isinstance(b1, int):
                if a1 < b1:
                    val = 1
                if a1 > b1:
                    val = -1
                if a1 == b1:
                    continue

            if val == 0:
                val = check_order(a1, b1)

            if val == 1:
                return 1
            if val == -1:
                return -1

        return val

    def cmp(a, b):
        _a = copy.deepcopy(a)
        _b = copy.deepcopy(b)
        val = check_order(_a, _b)
        return -1 if val == 1 else 1

    for i in range(0, len(lines), 3):
        a = eval(lines[i])
        b = eval(lines[i + 1])
        if check_order(a, b) == 1:
            ans1 += ((i + 3) // 3)

    part_2 = [[[2]], [[6]]]
    for i in range(0, len(lines), 3):
        a = eval(lines[i])
        b = eval(lines[i + 1])
        part_2.extend([a, b])

    part_2.sort(key=cmp_to_key(cmp))

    ans2 = (part_2.index([[2]]) + 1) * (part_2.index([[6]]) + 1)

    return ans1, ans2


def main():
    print("Part 1: %d\nPart 2: %d" % solve_1())


if __name__ == '__main__':
    main()
