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

            if i < len(vals) and vals[i] != 'null':
                new_root.right = TreeNode(int(vals[i]))
                roots.append(new_root.right)
            i += 1

    return root

class Solution: 
    def maxProduct(self, root):
        #1. build a new tree with sums
        def build_sum_tree(cur_root):         
            if cur_root.left:
                cur_root.val += build_sum_tree(cur_root.left)
                
            if cur_root.right:
                cur_root.val += build_sum_tree(cur_root.right)
                
            return cur_root.val

        total_sum = build_sum_tree(root)
        #2. iterate new tree and get the max product
        global min_diff
        min_diff = float('inf')
        def get_max_products(cur_root):
            global min_diff
            #get products of cutting left/right edges
            max_product = 0
            for node in [cur_root.left, cur_root.right]:
                if node:
                    diff = abs(total_sum - 2 * node.val)
                    if diff >= min_diff:
                        continue
                    
                    min_diff = diff
                    local_product = node.val * (total_sum - node.val)
                    if local_product > max_product:
                        max_product = local_product

                    #recurse edge
                    child_product = get_max_products(node)
                    if child_product > max_product:
                        max_product = child_product
            
            return max_product
        max_product = get_max_products(root)

        #3 post processing (mod)
        max_product %= 1e9 + 7

        return int(max_product)

def main():
    sol = Solution()

    test_cases = [
                    # ("[1,2,3,4,5,6]",110),
                    # ("[1,null,2,3,4,null,null,5,6]", 90),
                    # ("[1,1]", 1),
                    # ("[2,3,9,10,7,8,6,5,4,11,1]", 1025),
                    ("[43,71,611,287,90,319,null,766,533,null,565,191,844,405,912,1,546,334,780,109,232,997,336,962,null,162,148,562,463,399,238,null,534,156,null,494,null,834,18,null,null,null,null,256,910,null,552,null,null,956,545,859,163,589,454,null,119,null,null,null,null,null,null,null,null,803,188,776,null,407,429,null,850,287,967,299,51,157,903,null,797,616,776,null,null,83,null,null,487,null,null,null,965,null,509,null,null,null,null,null,null,461,795,null,null,null,null,987,503,691,772,399,738,944,822,null,874,null,null,null,null,858,null,null,null,null,null,null,null,null,null,null,917,null,null,621,370,null,null,836,null,null,null,null,null,null,411,null,null,null,null,463,411,149,null,417,69,null,null,null,614,942,283,30,675,null,44,null,null,null,null,139,173,823,null,381,null,null,851,null,null,null,586,null,null,null,null,826,338,null,null,null,247,null,null,null,null,null,846]", 649079758)
                    
                  ]
    
    sol = Solution()
    
    for input, target in test_cases:
        print()
        print("##################################")
        start = timeit.default_timer()
        actual = sol.maxProduct(build_Tree(input))

        test_output(actual, target)
        stop = timeit.default_timer()
        print('Total Time: ', stop - start) 
        print("##################################")
        

if __name__ == '__main__':
    main()