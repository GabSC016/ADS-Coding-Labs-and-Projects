def dfs_n_queens(n):
    if n < 1:
        return []

    solution = []
    solutions = []

    def is_safe(line, column):
        if column in solution:
            return False
        
        for previus_line in range(line):
            previus_column = solution[previus_line]

            if line + column == previus_line + previus_column or line - column == previus_line - previus_column:
                return False

        return True
    
    def backtrack(line):
        if line == n:
            solutions.append(solution.copy())
            return
        
        for column in range(n):

            if is_safe(line, column):
                solution.append(column)

                backtrack(line + 1)

                solution.pop()
    
    backtrack(0)
    return solutions