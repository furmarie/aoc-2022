def solve():
    rocks = set()
    max_y, min_x, max_x = 0, 1e9, -1e9
    with open("input.txt", "r") as f:
        for l in f.read().splitlines():
            coords = [(int(x), int(y)) for x, y in (p.rstrip().split(',') for p in l.split('->'))]

            for i in range(len(coords) - 1):
                x1, y1 = coords[i]
                x2, y2 = coords[i + 1]
            
                for x in range(min(x1, x2), max(x1, x2) + 1):
                    for y in range(min(y1, y2), max(y1, y2) + 1):
                        max_y = max(max_y, y)
                        min_x = min(min_x, x)
                        max_x = max(max_x, x)
                        rocks.add((x, y))

    def part_1(rocks):
        ans = 0
        s_x, s_y = 500, 0
        while True:
            if(s_x < min_x or s_x > max_x or s_y > max_y):
                break

            if (s_x, s_y + 1) not in rocks:
                s_y += 1
                continue
            if (s_x - 1, s_y +1) not in rocks:
                s_x -= 1
                s_y += 1
                continue
            if (s_x + 1, s_y + 1) not in rocks:
                s_x += 1
                s_y += 1
                continue

            ans += 1
            rocks.add((s_x, s_y))
            s_x, s_y = 500, 0

        return ans
        
    def part_2(rocks):
        ans = 0
        floor_y = max_y + 2
        s_x, s_y = 500, 0
        while True:
            if s_y + 1 != floor_y:
                if (s_x, s_y + 1) not in rocks:
                    s_y += 1
                    continue
                if (s_x - 1, s_y +1) not in rocks:
                    s_x -= 1
                    s_y += 1
                    continue
                if (s_x + 1, s_y + 1) not in rocks:
                    s_x += 1
                    s_y += 1
                    continue
                
            ans += 1
            rocks.add((s_x, s_y))
            if((s_x, s_y) == (500, 0)):
                break

            s_x, s_y = 500, 0

        return ans
    
    return part_1(rocks), part_2(rocks)


def main():
    print("Part 1: %d\nPart 2: %d" % solve())
    

if __name__ == '__main__':
    main()
