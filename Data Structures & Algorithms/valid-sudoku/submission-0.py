class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        checking the duplicate -> using the hash set
        check the rows if have that value or not
        check the columns if have that value or not
        check the boxes if have that value or not 
        soduko  = 9 * 9 
        rows, col = 0, 0  -> position = rows * 9 + col = 0 (position 0)
        rows, col = 0, 1 -> position = rows * 9 + col = 1 

        [
            0,1,2, 
            9,10,11 -> boxes = 0 (calculate the box 1) -> (18 % 9) // 3 = boxes
            18,19,20
        ]
        [
            3,4,5
            12,13,14 -> boxes = 1 (12 % 9 == 3 // 3 == 1 -> boxes)
            21,22,23
        ]
        formula for the box = ((rows * 9 + cols) % 9) // 3 = id of boxes
        for each cell in rows
            for each cell in cols:
                value = board[i][j]
                if value in rows_0, set() or value in cols_0, or in boxes = 0
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                val = board[r][c]
                b = (r //3) * 3 + (c // 3)
                print(r, c, b)
                if val in rows[r] or val in cols[c] or val in boxes[b]:
                    return False
                rows[r].add(val)
                cols[c].add(val)
                boxes[b].add(val)

        """
        [27, 28, 29] -> 27 // 9
        """
        return True