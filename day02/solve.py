def solve_1(data):
    count = 0
    for values in data:
        ascending_safe = all(i < j and 1 <= (j - i) <= 3 for i, j in zip(values, values[1:]))
        descending_safe = all(i > j and 1 <= (i - j) <= 3 for i, j in zip(values, values[1:]))
        if ascending_safe or descending_safe:
            count += 1
    return count


def solve_2(data):
    pass

def main():
    with open("input.txt") as f:
        data = [list(map(int, line.strip().split())) for line in f]
    print(solve_1(data))

if __name__ == "__main__":
    main()
