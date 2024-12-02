#!/bin/bash

YEAR=2024

if [ ! -f ".env" ]; then
    echo ".env file is missing. Please create it with SESSION_COOKIE inside."
    exit 1
fi

for DAY in $(seq 1 31); do
    DAY_PADDED=$(printf "%02d" $DAY)
    DIRECTORY="day$DAY_PADDED"
    mkdir -p "$DIRECTORY"

    CRAWLER_FILE="$DIRECTORY/crawler.sh"
    cat << EOF > "$CRAWLER_FILE"
#!/bin/bash
if [ -f "../.env" ]; then
    export \$(grep -v '^#' ../.env | xargs)
else
    echo ".env file missing. Place a .env file with SESSION_COOKIE inside."
    exit 1
fi

URL="https://adventofcode.com/$YEAR/day/$DAY/input"

curl -s -H "Cookie: session=\$SESSION_COOKIE" -H "User-Agent: Bash Advent of Code Fetcher" "\$URL" -o "input.txt"

if [ \$? -eq 0 ]; then
    echo "Input successfully downloaded into input.txt"
else
    echo "Error downloading the input"
fi
EOF

    chmod +x "$CRAWLER_FILE"

    SOLVE_FILE="$DIRECTORY/solve.py"
    cat << EOF > "$SOLVE_FILE"
def solve_1(data):
    pass

def solve_2(data):
    pass

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        data = f.read().strip()
    
    print("Part 1:", solve_1(data))
    print("Part 2:", solve_2(data))
EOF

done

echo "Structure created successfully! Don't forget to configure your .env file."
