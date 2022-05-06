from collections import defaultdict
from itertools import product
from termcolor import colored
import timeit

def validate(actual, target):
    if isinstance(target, list):
        if len(actual) != len(target):
            return False
        actual.sort()
        target.sort()
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
    def __init__(self) -> None:
        self.children = {}

class Solution: 
    def findWords(self, board, words):
        #O(len(words) * max(len(words[i])))
        #build trie tree
        trie = {}
        for i, word in enumerate(words):
            node = trie
            for c in word:
                if c not in node:
                    node[c] = Node()
                node = node[c].children
            node['id'] = i

        m = len(board)
        n = len(board[0])
        res = []
        seen = set()
        #O(mn^2) * O(logN)
        # go over each cell and search words
        # (need to remove nodes?) Yes when we find the word and if the node has no other child
        def dfs(i, j, tree):
            # #check if we found a word from trie tree
            if 'id' in tree:
                res.append(words[tree['id']])
                del tree['id']
                
                if len(tree) == 0:
                    return

            #boundary check
            if i < 0 or j < 0 or i >= m or j >= n:
                return
            
            c = board[i][j]
            if c in tree:
                child_tree = tree[c].children
                for ni, nj in [(i+1, j), (i, j+1), (i-1, j), (i, j-1)]:
                    have_child = len(child_tree) > 0
                    if not have_child:
                        break
                
                    if (ni, nj) not in seen:
                        seen.add((ni, nj))
                        dfs(ni, nj, child_tree)
                        seen.remove((ni, nj))
                if not have_child:
                    del tree[c]
                
            return

        for r in range(m):
            for c in range(n):
                if board[r][c] not in trie:
                    continue
                seen.add((r, c))
                dfs(r, c, trie)
                seen.remove((r, c))

        return res

def main():
    sol = Solution()

    test_cases = [
                    (([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], ["oath","pea","eat","rain"]), ["eat","oath"]),
                    # (([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], ["oath","pea","eat", "eath","rain","oatt"]), ["eat","oath"]),
                  ]
    
    sol = Solution()
    all_passed = True
    
    for input, target in test_cases:
        print()
        print("input : {}".format(input))
        start = timeit.default_timer()
        actual = sol.findWords(*input)
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