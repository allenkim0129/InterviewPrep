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

"""
Trie tree? 

1. Start with sorting products

2. Build Trie Tree

3. for each char in searchWord, use Node to find the first 3 words

Node(m)
 - start_id: 0
 - end_id: 5
 children{
     Node(o):
        - start_id: 0
        - end_id: 5
        children{
            Node(u):
                - start_id: 3
                - end_id: 5
                children{
                    Node(s):
                        - start_id: 3
                        - end_id: 5

                }
            Node(b):
                - start_id: 0
                - end_id: 1
        }
 }


"""


class TrieNode:
    def __init__(self, start_id, end_id) -> None:
        self.start_id = start_id
        self.end_id = end_id
        self.children = {}        
        
class Solution: 
    def suggestedProducts(self, products, searchWord):
        #sort
        products.sort()

        #build Trie Tree with start and end indices
        root = {}
        for i, product in enumerate(products):
            cur_node = root
            for c in product:
                if c not in cur_node:
                    cur_node[c] = TrieNode(i, i+1)
                else:
                    cur_node[c].end_id += 1
                cur_node = cur_node[c].children
        
        res = []
        cur_node = root
        for i, c in enumerate(searchWord):
            if c in cur_node:
                start = cur_node[c].start_id
                end = cur_node[c].end_id
                if end - start > 3:
                    res.append(products[start:start+3])
                else:
                    res.append(products[start:end])
                cur_node = cur_node[c].children
            else:
                for _ in range(len(searchWord)-i):
                    res.append([])
                break

        return res

def main():
    sol = Solution()

    test_cases = [
                    ((["mobile","mouse","moneypot","monitor","mousepad"], "mouse"),[["mobile","moneypot","monitor"],["mobile","moneypot","monitor"],["mouse","mousepad"],["mouse","mousepad"],["mouse","mousepad"]]),
                    ((["havana"], "havana"), [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]),
                    ((["bags","baggage","banner","box","cloths"], "bags"), [["baggage","bags","banner"],["baggage","bags","banner"],["baggage","bags"],["bags"]]),
                    ((["havana"], "tatiana"), [[],[],[],[],[],[],[]]),
                  ]
    
    sol = Solution()
    all_passed = True
    
    for input, target in test_cases:
        print()
        print("input : {}".format(input))
        start = timeit.default_timer()
        actual = sol.suggestedProducts(*input)
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