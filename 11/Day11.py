import sys

class Monkey:
    def __init__(self, items, operation, test_num, true_throw, false_throw):
        self.items = items
        self.op = operation
        self.test_num = test_num
        self.true_throw = true_throw
        self.false_throw = false_throw
        self.num_inspected = 0

    def get_throw(self, mod, div_factor):
        while self.items:
            self.num_inspected += 1
            curr_item = self.items.pop(0)
            old = curr_item
            new_val = eval(self.op) % mod
            new_val //= div_factor

            if new_val % self.test_num == 0:
                yield new_val, self.true_throw
            else:
                yield new_val, self.false_throw

def get_line():
    return sys.stdin.readline().rstrip('\r\n')

def solve(num_rounds, div_factor):
    sys.stdin = open("input.txt", "r")
    
    monkeys = []
    mod = 1
    for _ in range(8):
        monkey_id = int(get_line()[-2])
        items = eval("[" + get_line().split(':')[-1] + "]")
        operation = get_line().split("=")[-1]
        test_num = int(get_line().split()[-1])
        true_throw = int(get_line().split()[-1])
        false_throw = int(get_line().split()[-1])

        mod *= test_num

        get_line()

        monkeys.append(
            Monkey(items, operation, test_num, true_throw, false_throw)
        )

    for _ in range(num_rounds):
        for monkey in monkeys:
            for item_val, to_id in monkey.get_throw(mod=mod, div_factor=div_factor):
                monkeys[to_id].items.append(item_val)

    monkeys.sort(key=lambda monkey : monkey.num_inspected)
    
    return monkeys[-1].num_inspected * monkeys[-2].num_inspected
        

def main():
    print(f"Part 1: {solve(20, 3)}")
    print(f"Part 2: {solve(10000, 1)}")


if __name__ == '__main__':
    main()
