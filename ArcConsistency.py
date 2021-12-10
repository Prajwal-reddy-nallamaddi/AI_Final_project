def cross(A, B):
    return [a+b for a in A for b in B]


def parse_grid(grid):
    values = dict((s, digits) for s in squares)
    for s, d in grid_values(grid).items():
        if d in digits and not assign(values, s, d):
            return False 
    return values


def grid_values(grid):
    chars = [c for c in grid if c in digits or c in '0.']
    assert len(chars) == 36
    return dict(zip(squares, chars))


def assign(values, s, d):
    other_values = values[s].replace(d, '')
    if all(eliminate(values, s, d2) for d2 in other_values):
        return values
    else:
        return False


def eliminate(values, s, d):
    if d not in values[s]:
        return values 
    values[s] = values[s].replace(d, '')
    if len(values[s]) == 0:
        return False  
    elif len(values[s]) == 1:
        d2 = values[s]
        if not all(eliminate(values, s2, d2) for s2 in peers[s]):
            return False
    for u in units[s]:
        dplaces = [s for s in u if d in values[s]]
        if len(dplaces) == 0:
            return False  
        elif len(dplaces) == 1:
            if not assign(values, dplaces[0], d):
                return False
    return values


def show(values):
    width = 1+max(len(values[s]) for s in squares)
    line = '+'.join(['-'*(width*3)]*2)
    for r in rows:
        print(''.join(values[r+c].center(width)+('|' if c in '3' else '')
                      for c in cols))
        if r in 'BD':
            print(line)
    print()
    
def evaluate():
    assert len(squares) == 36
    assert len(unitlist) == 18
    assert all(len(units[s]) == 3 for s in squares)
    assert all(len(peers[s]) == 12 for s in squares)
    assert units['C2'] == [['A2', 'B2', 'C2', 'D2', 'E2', 'F2'],
                           ['C1', 'C2', 'C3', 'C4', 'C5', 'C6'],
                           ['C1', 'C2', 'C3', 'D1', 'D2', 'D3']]
    assert peers['C2'] == set(['A2', 'C3', 'B2', 'C4', 'D3', 'C5', 'D1', 'C1', 'C6', 'F2', 'E2', 'D2'])
    print('All constraint tests are passed.', end="\n")

digits = '123456'
letters = 'ABCDEF'
rows = letters
cols = digits

squares = cross(rows, cols)

unitlist = ([cross(rows, c) for c in cols] +
            [cross(r, cols) for r in rows] +
            [cross(rs, cs) for rs in ('AB', 'CD', 'EF') for cs in ('123', '456')])

units = dict((s, [u for u in unitlist if s in u])
             for s in squares)

peers = dict((s, set(sum(units[s], []))-set([s]))
             for s in squares)


grid = str(input("\nInput Rules: \n Enter 36 inputs as we are dealing with 6 X 6 sudoku.\n Enter blank spaces with 0 or .\n \n\n Enter the Sudoku grid : "))

print("\n Solved Sudoku Grid:")

show(parse_grid(grid))
evaluate()
print("\n Hurray!!! sudoku solved in seconds Thanks to Artificial Intelligence.")