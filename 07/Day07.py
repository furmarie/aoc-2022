from collections import defaultdict
import functools

def solve():
    file_sizes = defaultdict(int)
    dirs = defaultdict(list)

    path = []

    last_command = ""

    @functools.lru_cache
    def get_size(dir):
        res = file_sizes[dir]
        for nxt_dir in dirs[dir]:
            res += get_size(nxt_dir)
        return res

    paths = set()
    with open("input.txt", "r") as f:
        for l in f.readlines():
            l = l.rstrip().split()
            if (l[0] == '$'):
                if l[1] == 'cd':
                    if l[2] == '..':
                        path.pop()
                    else:
                        path.append(l[2])
                    paths.add("/".join(path))
            else:
                path_str = "/".join(path)
                if l[0] == 'dir':
                    dirs[path_str].append(path_str + "/" + l[1])
                else:
                    file_sizes[path_str] += int(l[0])
                    
    ans1 = 0
    ans2 = 1e9
    total_space = 70_000_000
    max_used_space = total_space - 30_000_000
    used_space = get_size("/")

    for dir in paths:
        curr_size = get_size(dir)
        if(curr_size <= 100_000):
            ans1 += curr_size

        if used_space - curr_size <= max_used_space:
            ans2 = min(ans2, curr_size)

    print("Part 1: ", ans1)
    print("Part 2: ", ans2)


def main():
    solve()

if __name__ == '__main__':
    main()
