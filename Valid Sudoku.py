from collections import defaultdict
from itertools import product
import timeit

def test_output(actual, target):
    print()
    # start = timeit.default_timer()
    print("target: {}".format(target))
    print("actual: {}".format(actual))
    # stop = timeit.default_timer()
    # print('Time: ', stop - start) 

class Solution: 
    def isValidSudoku(self, board):
        sub_board_set = [set() for _ in range(len(board))]
        col_val_set = [set() for _ in range(len(board[0]))]
        row_val_set = set()
            
        for i, row in enumerate(board):
            if i % 3 == 0:
                for sub_board_set_id in range(len(sub_board_set)):
                    sub_board_set[sub_board_set_id].clear()
            
            row_val_set.clear()
            for j, val in enumerate(row):
                if val == '.':
                    continue
                
                if val in row_val_set:
                    return False

                sub_board_set_id = int(j / 3)
                if val in sub_board_set[sub_board_set_id]:
                    return False
                
                if val in col_val_set[j]:
                    return False
                
                row_val_set.add(val)
                sub_board_set[sub_board_set_id].add(val)
                col_val_set[j].add(val)
        
        return True

def main():
    sol = Solution()

    test_cases = [
                    ([["7",".",".",".","4",".",".",".","."],[".",".",".","8","6","5",".",".","."],[".","1",".","2",".",".",".",".","."],[".",".",".",".",".","9",".",".","."],[".",".",".",".","5",".","5",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".","2",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."]], False),
                    # ([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]], True),
                    # ([["8","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]], False),
                  ]
    
    sol = Solution()
    
    for input, target in test_cases:
        start = timeit.default_timer()
        actual = sol.isValidSudoku(input)

        test_output(actual, target)
        stop = timeit.default_timer()
        print('Time: ', stop - start) 
        


if __name__ == '__main__':
    main()