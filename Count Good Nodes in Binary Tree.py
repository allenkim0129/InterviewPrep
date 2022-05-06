from collections import defaultdict, deque
from itertools import product
import timeit

def test_output(actual, target):
    print()
    # start = timeit.default_timer()
    print("target: {}".format(target))
    print("actual: {}".format(actual))
    # stop = timeit.default_timer()
    # print('Time: ', stop - start) 

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
    def goodNodes(self, root, max = -10001):
        if not root:
            return 0

        if root.val < max:
            count = 0
        else:
            count = 1
            max = root.val

        if root.left:
            count += self.goodNodes(root.left, max)
        if root.right:
            count += self.goodNodes(root.right, max)
        
        return count

def main():
    sol = Solution()

    test_cases = [
                    ("[3,3,null,4,2]", 3),
                    ("[3,1,4,3,null,1,5]", 4),
                  ]
    
    sol = Solution()
    
    for input, target in test_cases:
        input = build_Tree(input)
        
        start = timeit.default_timer()
        actual = sol.goodNodes(input)

        test_output(actual, target)
        stop = timeit.default_timer()
        print('Time: ', stop - start) 
        


if __name__ == '__main__':
    main()