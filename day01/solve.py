def solve_1(first_list, second_list):
    return sum(abs(a - b) for a, b in zip(sorted(map(int, first_list)), sorted(map(int, second_list))))

def solve_2(first_list, second_list):
    nb_occurences_b = {int(b): second_list.count(b) for b in set(second_list)}
    return sum(int(a) * nb_occurences_b.get(int(a), 0) for a in first_list)

    

def main():
    with open("input.txt") as f:
        data = [line.strip().split(" ") for line in f]
    first_list,second_list= [int(x[0]) for x in data], [int(x[-1]) for x in data]
    print(solve_1(first_list, second_list))
    print(solve_2(first_list, second_list))

if __name__ == "__main__":
    main()