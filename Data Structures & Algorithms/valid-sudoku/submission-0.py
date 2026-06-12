from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()

        for r in range(9):
            for c in range(9):
                num = board[r][c]

                if num == ".":
                    continue

                if ((num, r) in seen or
                    (c, num) in seen or
                    (r // 3, c // 3, num) in seen):
                    return False

                seen.add((num, r))              
                seen.add((c, num))               
                seen.add((r // 3, c // 3, num)) 

        return True