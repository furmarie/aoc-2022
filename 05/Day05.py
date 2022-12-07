def solve_1():
    with open("input.txt", "r") as f:
        mat = []
        d = [[] for _ in range(10)]
        for l in f.readlines():
            if(len(l) < 2):
                nms = mat[-1]
                mat.pop()
                n = len(nms)
                for j in range(n):
                    if nms[j].isdecimal():
                        for i in range(len(mat) - 1, -1, -1):
                            if mat[i][j].isalpha():
                                d[int(nms[j])].append(mat[i][j])
            elif l[0] == "m":
                a = []
                l = l.rstrip()
                for c in l.split(' '):
                    if c.isdecimal():
                        a.append(int(c))

                d[a[-1]] += d[a[-2]][-a[0]:][::-1]
                d[a[-2]] = d[a[-2]][:-a[0]]
         
            else:
                mat.append(l[:-1])

        print("Part 1: ", end="")
        for i in range(1, 10):
            print(d[i][-1] if d[i] else " ", end="")
        print()

def solve_2():
    with open("input.txt", "r") as f:
        mat = []
        d = [[] for _ in range(10)]
        for l in f.readlines():
            if(len(l) < 2):
                nms = mat[-1]
                mat.pop()
                n = len(nms)
                for j in range(n):
                    if nms[j].isdecimal():
                        for i in range(len(mat) - 1, -1, -1):
                            if mat[i][j].isalpha():
                                d[int(nms[j])].append(mat[i][j])
            elif l[0] == "m":
                a = []
                l = l.rstrip()
                for c in l.split(' '):
                    if c.isdecimal():
                        a.append(int(c))

                d[a[-1]] += d[a[-2]][-a[0]:]
                d[a[-2]] = d[a[-2]][:-a[0]]
         
            else:
                mat.append(l[:-1])

        print("Part 2: ", end="")
        for i in range(1, 10):
            print(d[i][-1] if d[i] else " ", end="")
        print()


def main():
    solve_1()
    solve_2()


if __name__ == '__main__':
    main()
