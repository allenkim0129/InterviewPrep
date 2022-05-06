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

class Solution: 
    def combinationSum2(self, candidates, target):
        candidates.sort()
        
        
        prev = candidates[0]

        cand = [(prev, 1)]

        for cur in candidates[1:]:
            if cur == prev:
                cand[-1] = (cand[-1][0], cand[-1][1]+1)
            else:
                cand.append((cur, 1))
        
        

        def rec(cid, t):
            ans = []
            
            for i in range(cid, len(cand)):
                if cand[i][0] == t:
                    ans.append([cand[i][0]])
                    break
                if cand[i][0] > t:
                    break
                if i == len(cand)-1:
                    break
                
                for j in range(1, cand[i][1]):
                    new_t = t - cand[i][0] * j

                    if cand[i+1][0] <= new_t:
                        ret = rec(i+1, new_t)
                        
                        if len(ret) > 0:
                            for r in ret:
                                temp = [cand[i][0] for _ in range(j)]
                                ans.append(temp + r)
                
            return ans
        
        ans = rec(0, target)
        ans = [tuple(a) for a in ans]
        
        set_ans = set(ans)
        
        return list(set_ans)

def main():
    sol = Solution()

    test_cases = [
                    ([[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], 4], []),
                    # ([[10,1,2,7,6,1,5], 8], [[1,1,6],[1,2,5],[1,7],[2,6]]),
                  ]
    
    sol = Solution()
    all_passed = True
    
    for input, target in test_cases:
        print()
        print("input : {}".format(input))
        start = timeit.default_timer()
        actual = sol.combinationSum2(input[0], input[1])
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