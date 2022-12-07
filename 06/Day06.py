def solve_1():    
    with open("../Input.txt", "r") as f:
       for l in f.readlines():
        l = l.rstrip()
        for i in range(len(l)):
            if len(set(x for x in l[i :i + 4])) == 4:
                print("Part 1: ", i + 4)
                return


def solve_2():    
    with open("../Input.txt", "r") as f:
       for l in f.readlines():
        l = l.rstrip()
        for i in range(len(l)):
            if len(set(x for x in l[i :i + 14])) == 14:
                print("Part 2: ", i + 14)
                return

def main():
    solve_1()
    solve_2()

if __name__ == '__main__':
    main()
