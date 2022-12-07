def main():
    ans1, ans2 = 0, 0
    with open("input.txt", "r") as f:
        for l in f.readlines():
            a, b = l.split(',')
            a1, a2 = a.split('-')
            b1, b2 = b.split('-') 
            a1 = int(a1)
            a2 = int(a2)
            b1 = int(b1)
            b2 = int(b2)
            if((b1 >= a1 and b2 <= a2) or \
                (a1 >= b1 and a2 <= b2)
                ):    
                ans1 += 1

            if((b1 >= a1 and b1 <= a2) or \
                (a1 >= b1 and a1 <= b2)
                ):    
                ans2 += 1
    
    print("Part 1: ", ans1)
    print("Part 2: ", ans2)



if __name__ == '__main__':
    main()
