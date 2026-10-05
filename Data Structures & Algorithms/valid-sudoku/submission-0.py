class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows={}
        columns={}
        quadrants={}
        for r, row in enumerate(board):
            rows[r]=set()
            for c, val in enumerate(row):
                if c not in columns:
                    columns[c]=set()
                quadrant = c//3 + (r//3)*3
                if quadrant not in quadrants:
                    quadrants[quadrant] = set()
                if val == ".":
                    continue
                if val in rows[r] or val in columns[c] or val in quadrants[quadrant]:
                    # print(f"val={val}, r={r}, c={c}, q={quadrant}")
                    # print("rows:", rows)
                    # print("columns:", columns)
                    # print("quadrants:", quadrants)
                    return False
                rows[r].add(val)
                columns[c].add(val)
                quadrants[quadrant].add(val)
        # print("rows:", rows)
        # print("columns:", columns)
        # print("quadrants:", quadrants)
        return True

