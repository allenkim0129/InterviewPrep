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
    def build_graph(self, start, nums):
        if self.graph[start] is not None:
            return self.graph[start][1]
        
        first = nums[start]
        max_slen = 0
        max_sid = -1
        for i in range(start+1, len(nums)):
            if nums[i] % first == 0:
                slen = self.build_graph(i, nums)
                if slen > max_slen:
                    max_slen = slen
                    max_sid = i
        
        self.graph[start] = (max_sid, max_slen+1)
        
        return max_slen+1
    
    
    def largestDivisibleSubset(self, nums):
        nums.sort()

        self.graph = [None] * len(nums)
        
        max_slen = 0
        max_sid = 0

        for i in range(len(nums)):
            if self.graph[i] is None:
                slen = self.build_graph(i, nums)
                if slen > max_slen:
                    max_slen = slen
                    max_sid = i
        
        subset = []

        id = max_sid
        while id >= 0:
            subset.append(nums[id])

            id = self.graph[id][0]

        return subset
            
        
        
def main():
    sol = Solution()

    test_cases = [
                    ([1,2,3], [1,2]),
                    ([2,3,4,9,27], [3,9,27]),
                    ([1,2,4,8], [1,2,4,8])
                  ]
    
    sol = Solution()
    all_passed = True
    
    for input, target in test_cases:
        print()
        print("input : {}".format(input))
        start = timeit.default_timer()
        actual = sol.largestDivisibleSubset(input)
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


    Welcome to Meta!

This is just a simple shared plaintext pad, with no execution capabilities.

When you know what language you would like to use during your interview,
simply choose it from the dropdown in the top bar.

Enjoy your interview!

class QueryProcessor:
  def __init__(self, n):
    self.arr = [False] * n
  
  def get(self, i):
    for j in range(i, len(self.arr)):
      if self.arr[j]:
        return j
    
    return -1
  
  def set(self, i):
    self.arr[i] = True
  
  
def answerQueries(queries, N):
  qp = QueryProcessor(N)
  
  ans = []
  for q in queries:
    if q[0] == 1:
      qp.set(q[1])
    else:
      ans.append(qp.get(q[1]))
  
  
  return ans




def check(expected, actual):
  msg = "Passed!"
  if len(expected) != len(actual):
    msg = "Faliled!"
  
  for i, j in zip(expected, actual):
    if i != j:
      msg = "Failed!"
      break
  
  print(msg)
  return

def main():
  #test cases
  N = 5
  queries = [[2, 3], [1, 2], [2, 1], [2, 3], [2, 2]]
  expected = [-1, 2, -1, 2]
  actual = answerQueries(queires, N)
  check(expected, actual)
  

if __name__ == "__main__":
  main()