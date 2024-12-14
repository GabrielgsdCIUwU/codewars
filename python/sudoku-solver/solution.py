def sudoku(puzzle):
    def checkRow(rowNumber, puzzle):
        seen = set()
        for num in puzzle[rowNumber]:
            if num != 0:
                if num in seen:
                    return False
                seen.add(num)
        return True

    def checkColumn(colNumber, puzzle):
        seen = set()
        for i in range(9):
            num = puzzle[i][colNumber]
            if num != 0:
                if num in seen:
                    return False
                seen.add(num)
        return True

    def checkBlock(coordX, coordY, puzzle):
        seen = set()
        for row in range(coordY, coordY + 3):
            for col in range(coordX, coordX + 3):
                num = puzzle[row][col]
                if num != 0:
                    if num in seen:
                        return False
                    seen.add(num)
        return True

    def findEmpty(puzzle):
        for i in range(9):
            for j in range(9):
                if puzzle[i][j] == 0:
                    return (i, j)
        return None

    def guessNumber(puzzle):
        empty_pos = findEmpty(puzzle)
        if not empty_pos:
            return True
    
        row, col = empty_pos
        for num in range(1, 10):
            puzzle[row][col] = num
            if checkRow(row, puzzle) and checkColumn(col, puzzle) and checkBlock(col // 3 * 3, row // 3 * 3, puzzle):
                if guessNumber(puzzle):
                    return True
            puzzle[row][col] = 0

        return False

    if guessNumber(puzzle):
        return puzzle