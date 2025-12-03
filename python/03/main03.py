from typing import List
from collections import deque

def format_banks(banks: List[str]) -> List[List[int]]:
    return [list(map(int, list(bank.strip()))) for bank in banks]


def part01_batteries_on(banks: List[List[int]]) -> int:
    
    def activate_bank(bank: List[int]) -> int:
        q, n = deque([]), len(bank)

        for battery in bank:
            if len(q) < 2: 
                q.append(battery)
            elif battery > q[0] or battery > q[1]:
                if q[0] < q[1]:
                    _ = q.popleft()
                    q.append(battery)
                else: 
                    _ = q.pop()
                    q.append(battery)
            elif q[0] < q[1]:
                _  = q.popleft()
                q.append(battery) 
            elif battery > q[1]:
                _ = q.pop()
                q.appendleft(battery)

        return int(''.join(map(str, q)))
    
    return sum(activate_bank(bank) for bank in banks)


if __name__ == "__main__":

    with open('input03.txt', 'r') as f:
        banks = f.readlines()

    banks = format_banks(banks)

    print ("""--- Part One ---""")
    print("Total output Joltage:", part01_batteries_on(banks), "\n")