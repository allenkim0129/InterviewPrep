from collections import defaultdict
from itertools import product
from termcolor import colored
import timeit

def validate(actual, target):
    if isinstance(target, list):
        if len(actual) != len(target):
            return False
        for a, t in zip(actual, target):
            if not validate(a, t):
                return False
        return True
    else:
        return actual == target

def test_output(actual, target):
    print("target: {}".format(target))
    print("actual: {}".format(actual))
    if validate(actual, target):
        print(colored("Passed!", "green"))
        return True
    else:
        print(colored("Failed", "red"))
        return False

class Node:
    def __init__(self, children = dict()):
        self.children = children

class Solution:
    def solveNQueens(self, n):
        seen = set()
        def dfs(x, y):
            #base condition
            for x1, y1 in seen:
                if (x == x1
                    or y == y1
                    or y + x == x1 + y1
                    or y - x == y1 - x1):
                    return None

            children = dict()
            
            if x == n-1:
                return Node()

            seen.add((x,y))
            x1 = x+1
            for y1 in range(n):
                child = dfs(x1,y1)
                
                if child:
                    children[y1] = child
            seen.remove((x,y))
            
            if len(children) > 0:
                return Node(children)
            else:
                return None

        positions = {}
        
        for y_pos in range(n):
            node = dfs(0,y_pos)
            if node:
                positions[y_pos] = node
        
        def getQueenStr(pos, n):
            ret_str = ""
            for i in range(n):
                if i == pos:
                    ret_str += "Q"
                else:
                    ret_str += "."
            return ret_str
        
        def output(node):
            if not node.children:
                return [[]]

            boards = []
            for y, child in node.children.items():
                row = [getQueenStr(y, n)]
                child_boards = output(child)
                for cb in child_boards:
                    boards.append(row + cb)
            
            return boards
                
        
        #build output
        res = []
        for y, pos_node in positions.items():
            row = [getQueenStr(y, n)]
            boards = output(pos_node)
            for board in boards:
                res.append(row + board)

        return res
        

def main():
    sol = Solution()

    test_cases = [
                    (4, [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]),
                    (1, [["Q"]]),
                    (5, [["Q....","..Q..","....Q",".Q...","...Q."],["Q....","...Q.",".Q...","....Q","..Q.."],[".Q...","...Q.","Q....","..Q..","....Q"],[".Q...","....Q","..Q..","Q....","...Q."],["..Q..","Q....","...Q.",".Q...","....Q"],["..Q..","....Q",".Q...","...Q.","Q...."],["...Q.","Q....","..Q..","....Q",".Q..."],["...Q.",".Q...","....Q","..Q..","Q...."],["....Q",".Q...","...Q.","Q....","..Q.."],["....Q","..Q..","Q....","...Q.",".Q..."]]),
                  ]
    
    sol = Solution()
    all_passed = True
    
    for input, target in test_cases:
        print()
        print("input : {}".format(input))
        start = timeit.default_timer()
        actual = sol.solveNQueens(input)
        stop = timeit.default_timer()

        if not test_output(actual, target):
            all_passed = False
        print('Time: ', stop - start) 
    
    print()
    if all_passed:
        print(colored("All tests passed!", "green"))
    else:
        print(colored("Not all tests passed!", "red"))


if __name__ == '__main__':
    main()