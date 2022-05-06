from collections import defaultdict, deque
from itertools import product
from termcolor import colored
import timeit
import math

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
    def isValidBST(self, root):
        
        # def BST_validation(cur_root, min = -math.inf, max = math.inf):
        #     if not cur_root:
        #         return True
            
        #     cur_val = cur_root.val
        #     if (cur_val < min
        #         or cur_val > max):
        #         return False
            
        #     return (BST_validation(cur_root.left, min, cur_val-1)
        #             and BST_validation(cur_root.right, cur_val+1, max))

        # return BST_validation(root)

        stack = deque()
        stack.append((root, -math.inf, math.inf))
        while len(stack) > 0:
            cur_root, min, max = stack.popleft()
            cur_val = cur_root.val

            if (cur_val <= min
                or cur_val >= max):
                return False
            
            if cur_root.left:
                stack.append((cur_root.left, min, cur_val))
            if cur_root.right:
                stack.append((cur_root.right, cur_val, max))
        return True

def main():
    sol = Solution()

    test_cases = [
                    ("[2,1,3]", True),
                    ("[5,1,4,null,null,3,6]", False)
                  ]
    
    sol = Solution()
    all_passed = True

    for input, target in test_cases:
        print()
        print("input : {}".format(input))
        
        start = timeit.default_timer()
        actual = sol.isValidBST(build_Tree(input))
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