from collections import defaultdict, deque
from itertools import product
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

            if i < len(vals) and vals[i] != 'null':
                new_root.right = TreeNode(int(vals[i]))
                roots.append(new_root.right)
            i += 1

    return root

"""
Two Sum IV - Input is a BST
BST
Input: 
- root
- k: target number
Output:
- return true if there exist two elements, which the sum is equals to target

(Preferred)
Approach1:
- Using hash set to keep track of (target - val)
- Keep going in until the value is in the set

(Not valid, since it is possible to have two numbers in left and right children)
Approach2: Use BST condition
- From root, if (target - val) > val, take right child
- else (target - val) < val take left child

"""

class Solution: 
    #non-recursion (Faster)
    def findTarget(self, root, k):
        if not root:
            return True if k == 0 else False
    
        seen = set()
        
        dq = deque()
        dq.append(root)

        while len(dq) > 0:
            cur_root = dq.popleft()

            if (k - cur_root.val) in seen:
                return True
            
            seen.add(cur_root.val)

            if cur_root.left:
                dq.append(cur_root.left)
            if cur_root.right:
                dq.append(cur_root.right)
        return False

    # #recursion
    # def findTarget(self, root, k):
    #     if not root:
    #         return True if k == 0 else False
    
    #     seen = set()
        
    #     def bfs(cur_root):
    #         if (k - cur_root.val) in seen:
    #             return True
            
    #         seen.add(cur_root.val)
    #         if cur_root.left and bfs(cur_root.left):
    #             return True

    #         if cur_root.right and bfs(cur_root.right):
    #             return True

    #         return False

    #     return bfs(root)

def main():
    sol = Solution()

    test_cases = [
                    (("[5,3,6,2,4,null,7]", 9), True),
                    (("[5,3,6,2,4,null,7]", 28), False),
                    (("[2,1,3]", 4), True),
                    (("[2,1,3]", 1), False),
                    (("[2,1,3]", 3), True),
                    (("[5,-7,9]", 2), True),

                  ]
    
    sol = Solution()
    
    num_failed = 0
    for input, target in test_cases:
        start = timeit.default_timer()
        actual = sol.findTarget(build_Tree(input[0]), input[1])

        stop = timeit.default_timer()
        test_output(actual, target)
        if validate(actual, target):
            print("Passed!")
        else:
            print("Failed!")
            num_failed += 1
        print('Time: ', stop - start) 
    
    print("\n{} tests failed".format(num_failed))


if __name__ == '__main__':
    main()