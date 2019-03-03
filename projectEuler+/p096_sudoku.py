# #96: Su Doku

import copy

def print_sudoku(problem):
    for row in problem:
        for elem in row:
            print(elem, end='')
        print('')

def solved(problem):
    def invalid(s, v):
        return not v or v in s
    
    for i in range(9):
        row = set()
        col = set()
        box = set()
        for j in range(9):
            v_row = problem[i][j]
            v_col = problem[j][i]
            
            r0 = i // 3
            c0 = i % 3
            r = 3*r0 + (j // 3)
            c = 3*c0 + (j % 3)
            v_box = problem[r][c]
            
            if invalid(row, v_row) or invalid(col, v_col) or invalid(box, v_box):
                return False
            
            row.add(v_row)
            col.add(v_col)
            box.add(v_box)
            
    return True

def solve(problem):
    if solved(problem):
        return
    
    r = c = None
    for i in range(9):
        for j in range(9):
            if problem[i][j] == 0:
                r = i
                c = j
                break
        if r:
            break
    
    cands = set(range(1,10))
    r0 = 3 * (r // 3)
    c0 = 3 * (c // 3)
    for i in range(9):
        dr = i // 3
        dc = i % 3
        vb = problem[r0+dr][c0+dc]
        cands.discard(problem[r][i])
        cands.discard(problem[i][c])
        cands.discard(vb)
        
    if len(cands) == 0:
        return
    
    for cand in cands:
        problem[r][c] = cand
        
        solve(problem)
        if solved(problem):
            return
        else:
            problem[r][c] = 0
    
problem = []
for _ in range(9):
    problem.append(list(map(int, list(input()))))

solve(problem)
print_sudoku(problem)
