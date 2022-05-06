from collections import defaultdict, deque
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

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_Tree(input_str):
    input_str = input_str.strip(']').strip('[')

    vals = input_str.split(',')
    root = None

    if len(vals) > 0:
        root = TreeNode(int(vals[0]))
        roots = deque([root])
        i = 1
        while i < len(vals):
            new_root = roots.popleft()
            
            if vals[i] != 'null':
                new_root.left = TreeNode(int(vals[i]))
                roots.append(new_root.left)
            i += 1
            
            if vals[i] != 'null':
                new_root.right = TreeNode(int(vals[i]))
                roots.append(new_root.right)
            i += 1

    return root

class Solution: 
    def isBalanced(self, root):
        if not root:
            return True
        
        def check_balance(cur_root):
            if not cur_root:
                return 0
            
            left = check_balance(cur_root.left)
            if left < 0:
                return -1
            right = check_balance(cur_root.right)
            if right < 0:
                return -1
            
            if abs(left - right) > 1:
                return -1
            else:
                return 1 + max(left, right)
        
        return check_balance(root) >= 0

def main():
    sol = Solution()

    test_cases = [
                    ("[1,2,2,3,3,null,null,4,4]", False),
                  ]
    
    sol = Solution()
    all_passed = True

    for input, target in test_cases:
        print()
        print("input : {}".format(input))
        
        start = timeit.default_timer()
        actual = sol.isBalanced(build_Tree(input))
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