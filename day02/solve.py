def solve_1(data):
    return sum(1 for values in data if is_safe(values))


def is_safe(values):
    ascending_safe = all(i < j and 1 <= (j - i) <= 3 for i, j in zip(values, values[1:]))
    descending_safe = all(i > j and 1 <= (i - j) <= 3 for i, j in zip(values, values[1:]))
    return ascending_safe or descending_safe

def solve_2(data):
    return sum(1 for values in data if any(is_safe(values[:i]+values[i+1:])for i in range(len(values))))


def main():
    with open("input.txt") as f:
        data = [list(map(int, line.strip().split())) for line in f]
    print(solve_1(data))
    print(solve_2(data))

if __name__ == "__main__":
    main()
