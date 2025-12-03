from typing import List
from collections import deque
from functools import lru_cache

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

def part02_batteries_on(banks: List[List[int]], k: int) -> int:

    def activate_bank(bank: str, k: int) -> int:
        @lru_cache(maxsize=None)
        def build_max(curr: int, remaining: int) -> str:

            # base cases
            if not remaining:
                return ''
            if curr == len(bank):
                return ''
                        
            # recursive cases
            use_battery = bank[curr] + build_max(curr + 1, remaining - 1) \
                if remaining <= len(bank) - curr else ''
            skip_battery = build_max(curr + 1, remaining)

            return max(use_battery, skip_battery)
            
        return int(build_max(0, k))

    return sum(activate_bank(''.join(map(str, bank)), k) for bank in banks)


if __name__ == "__main__":

    with open('input03.txt', 'r') as f:
        banks = f.readlines()

    banks = format_banks(banks)
    k = 12

    print ("""--- Part One ---""")
    print("Total output Joltage:", part01_batteries_on(banks), "\n")

    print ("""--- Part Two ---""")
    print("Total output Joltage:", part02_batteries_on(banks, k), "\n")
