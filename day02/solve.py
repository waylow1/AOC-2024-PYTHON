def solve_1(data):
    count = 0
    for values in data:
        if(is_safe(values)):
            count += 1
    return count


def is_safe(values):
    ascending_safe = all(i < j and 1 <= (j - i) <= 3 for i, j in zip(values, values[1:]))
    descending_safe = all(i > j and 1 <= (i - j) <= 3 for i, j in zip(values, values[1:]))
    return ascending_safe or descending_safe

def solve_2(data):
    count = 0
    for values in data:
        if is_safe(values):
            count += 1
            continue
        for i in range(len(values)):
            modified_values = values[:i] + values[i + 1:]
            if is_safe(modified_values):
                count += 1
                break
    return count

    

def main():
    with open("input.txt") as f:
        data = [list(map(int, line.strip().split())) for line in f]
    print(solve_1(data))
    print(solve_2(data))

if __name__ == "__main__":
    main()
