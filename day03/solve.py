import re

def solve_1(data):
    return sum(int(r.group(1)) * int(r.group(2)) for r in re.finditer("mul\((\d{1,3}),(\d{1,3})\)", data))

def solve_2(data):
    return sum(int(r.group(1)) * int(r.group(2)) for active, chunk in zip([True] + [cmd == "do" for cmd in re.findall("(do|don't)\(\)", data)], re.split("do\(\)|don't\(\)", data)) if active for r in re.finditer("mul\((\d{1,3}),(\d{1,3})\)", chunk))

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        data = f.read().strip()
    
    print("Part 1:", solve_1(data))
    print("Part 2:", solve_2(data))
