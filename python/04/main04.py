from typing import List, Tuple

def parse_paper_rolls(raw: List[str]) -> List[List[str]]:
    return [list(line) for line in raw]

def part01_count_accessible(paper_rolls: List[List[str]]) -> int:

    m, n = len(paper_rolls), len(paper_rolls[0])
    accessible = 0
    for i in range(m):
        for j in range(n):
            # check in all 8 directions for '@'
            # count fewer than 4
            if paper_rolls[i][j] == '.' : continue
            count = 0
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if dx == 0 and dy == 0: continue
                    if i + dx < 0 or i + dx >= m: continue
                    if j + dy < 0 or j + dy >= n: continue
                    if paper_rolls[i + dx][j + dy] == '@' or paper_rolls[i + dx][j + dy] == 'x':
                        count += 1
            if count < 4:
                accessible += 1
                paper_rolls[i][j] = 'x'

    return accessible

def part02_clear_accessible(paper_rolls: List[List[str]]) -> None:
    
    def count_accessible(paper_rolls: List[List[str]]) -> Tuple[int, List[List[str]]]:

        m, n = len(paper_rolls), len(paper_rolls[0])
        accessible = 0
        for i in range(m):
            for j in range(n):
                # check in all 8 directions for '@'
                # count fewer than 4
                if paper_rolls[i][j] == '.' : continue
                count = 0
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        if dx == 0 and dy == 0: continue
                        if i + dx < 0 or i + dx >= m: continue
                        if j + dy < 0 or j + dy >= n: continue
                        if paper_rolls[i + dx][j + dy] == '@' or paper_rolls[i + dx][j + dy] == 'x':
                            count += 1
                if count < 4:
                    accessible += 1
                    paper_rolls[i][j] = 'x'

        for i in range(m):
            for j in range(n):
                if paper_rolls[i][j] == 'x':
                    paper_rolls[i][j] = '.'

        return accessible, paper_rolls
    
    total_moved = 0
    accessible, paper_rolls = count_accessible(paper_rolls)
    total_moved += accessible

    while accessible > 0:
        accessible, paper_rolls = count_accessible(paper_rolls)
        total_moved += accessible

    return total_moved
    


if __name__ == "__main__":

    with open('input04.txt', 'r') as f:
        paper_rolls = [ line.strip() for line in f.readlines()]
        paper_rolls = parse_paper_rolls(paper_rolls)

    print ("""--- Part One ---""")
    print ("There are {0} accessible paper rolls".format(part01_count_accessible(paper_rolls)), "\n")

    print ("""--- Part Two ---""")
    print ("There are {0} accessible paper rolls".format(part02_clear_accessible(paper_rolls)), "\n")
