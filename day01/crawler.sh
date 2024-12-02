#!/bin/bash
if [ -f "../.env" ]; then
    export $(grep -v '^#' ../.env | xargs)
else
    echo ".env file missing. Place a .env file with SESSION_COOKIE inside."
    exit 1
fi

URL="https://adventofcode.com/2024/day/1/input"

curl -s -H "Cookie: session=$SESSION_COOKIE" -H "User-Agent: Bash Advent of Code Fetcher" "$URL" -o "input.txt"

if [ $? -eq 0 ]; then
    echo "Input successfully downloaded into input.txt"
else
    echo "Error downloading the input"
fi
