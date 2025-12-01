"""
Advent of Code 2025
2025 December 01

Frank Schoeneman
"""

from typing import List


def part01_count_zeros(start: int, rotation: List[str]) -> int:
    count = 0
    for line in rotations:
        line = line.strip()
        
        turn, val = line[0], line[1:]
        if turn == "L":
            val = -int(val)
        else:
            val = int(val)
        
        start = (start + val) % 100
        if start == 0:
            count += 1

    return start, count

def part02_count_zeros(start: int, rotation: List[str]) -> int:
    pass_count = 0
    for line in rotations:
        line = line.strip()
        
        turn, val = line[0], int(line[1:])
        
        pass_count += val // 100
        val = val % 100

        val = -int(val) if turn == "L" else int(val)

        if start + val >= 100 or start + val <=0:
            if start != 0: pass_count += 1
        start += val
        start %= 100

    return start, pass_count


if __name__ == "__main__":

    start = 50
    with open("input01.txt", "r") as f:
        rotations = f.readlines()

    print ("--- Part One ---")
    print ("start at ", start, "\n")
    stop, count = part01_count_zeros(start, rotations)

    print ("stop at ", stop, "\n")
    print ("count ", count, "\n")

    print ("--- Part Two ---")
    print ("start at ", start, "\n")
    stop, pass_count = part02_count_zeros(start, rotations)

    print ("stop at ", stop, "\n")
    print ("pass count ", pass_count, "\n")
