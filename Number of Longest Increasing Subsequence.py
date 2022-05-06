from collections import Counter, defaultdict
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

"""
[DP approach]
create a graph:
from v_i to all v_j on the right, create dictionary of backward edges, if v_i < v_j
 - graph[j]: [i, ...]

loop over graph from 0 to n-1:
 - update graph[j] with (max_length_to_v, num_edges)
 - if max_length_to_v is greater than existing max_length, update max_length and its number

return number of max_length

"""
# class Graph:
#     class Edge:
#         def
#     def __init__(self, nums) -> None:
        
    
class Solution:
    def findNumberOfLIS(self, nums):
        dictDictC = defaultdict(Counter)
        dictDictC[-1][-float('Inf')] = 1

        listN = []
        for n in nums:
            l,r = 0,len(listN)
            while l<r:
                ind = (l+r) // 2
                if listN[ind]<n:        l = ind+1
                else:                   r = ind
            if l<len(listN):            listN[l] = n
            else:                       listN.append(n)
            dictDictC[l][n] += sum( c for k,c in dictDictC[l-1].items() if k<n )

        return sum(dictDictC[max(dictDictC.keys())].values())

    # def findNumberOfLIS(self, nums):
    #     #build graph O(n^2)
    #     graph = defaultdict(list)
    #     for i in range(len(nums)):
    #         for j in range(i + 1, len(nums)):
    #             if nums[i] < nums[j]:
    #                 #key: end vertex id
    #                 #val: start_vertex_id
    #                 graph[j].append(i)
        
    #     #find LIS
    #     dp = [(1, 1)] * len(nums)
    #     max_len = 0
    #     num_max_len = 0
    #     for i in range(len(nums)):
    #         local_max_len, local_num_max_len = (1, 1)
    #         if i in graph:                    
    #             for j in graph[i]:
    #                 if 1 + dp[j][0] > local_max_len: 
    #                     local_max_len = 1 + dp[j][0]
    #                     local_num_max_len = dp[j][1]
    #                 elif 1 + dp[j][0] == local_max_len:
    #                     local_num_max_len += dp[j][1]
                
    #             dp[i] = (local_max_len, local_num_max_len)

    #         if local_max_len > max_len:
    #             max_len = local_max_len
    #             num_max_len = local_num_max_len
    #         elif local_max_len == max_len:
    #             num_max_len += local_num_max_len

    #     return num_max_len

def main():
    sol = Solution()

    test_cases = [
                    ([1,3,5,4,7], 2),
                    ([2,2,2,2,2], 5)
                  ]
    
    sol = Solution()
    
    for input, target in test_cases:
        start = timeit.default_timer()
        actual = sol.findNumberOfLIS(input)

        test_output(actual, target)
        stop = timeit.default_timer()
        print('Time: ', stop - start) 
        


if __name__ == '__main__':
    main()