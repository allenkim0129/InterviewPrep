"""
@date        : Friday April 8 2022
@author      : Allen Kim (allenkim0129@gmail.com)
@description : This file contains CanConstruct(sequence, sub_sequences) function,
               which checks if sequence can be created by sub_sequences, such as the following:
            (1). CanConstruct([1, 2, 3, 4, 5], [[1, 2], [3, 4], [5]]) == True
            (2). CanConstruct([1, 3, 4, 5, 2], [[2, 3], [1, 3], [4, 2], [2], [4, 5]]) == True
            (3). CanConstruct[1, 2, 3, 4, 5], [[2, 3], [1, 3], [4, 2], [4, 5]]) == False
            (4). CanConstruct[1, 2, 3, 4, 5], [[2, 3], [3], [1, 2], [4, 5]]) == True
            (5). CanConstruct[1, 2, 3, 4, 5], [[2, 3], [1, 2], [4, 5]]) == False

            By running the main() function it tests all pre-determinded test cases against
            CanConstruct() function, and print the results

@assuptions  : There is no duplication in sequence and sub_sequences
"""

from collections import defaultdict
from termcolor import colored
import timeit

"""
Helper functions
"""
def test_output(actual, target):
    """
    Description:
    -----------
        This method checks if 'actual' and 'target' matches

    Parameters:
    -----------
        actual : Actual output from 'CanConstruct()' function
        target : Target output to 'CanConstruct()' function

    Returns:
    --------
        Return True if outputs match, otherwise return False
    """
    print("target: {}".format(target))
    print("actual: {}".format(actual))
    if actual == target:
        print(colored("Passed!", "green"))
        return True
    else:
        print(colored("Failed", "red"))
        return False

def contains(seq: list, seq_idx_dict: dict, sub_seq: list):
    """
    Description:
    -----------
        This method checks if a sub_seq is in seq
        
        Time complexity: big O(L)
            - M: len(sequence)
            - N: len(sub_sequences)
            - L: max(sub_sequences[i])

    Parameters:
    -----------
        seq : The main sequence
        seq_idx_dict : The dictionary of indices of 'seq'
                        (key: values in 'seq', val: index)
        sub_seq : The sub_sequence to be compaired

    Returns:
    --------
        Return True if sub_seq is in seq, otherwise return False
    """
    try:
        # Get start and end index of sequence.
        # If first valuse in sub_seq not found in dict, 
        # raise KeyError
        seq_sid = seq_idx_dict[sub_seq[0]]
        # If seq_eid is out-of-range,
        # raise IndexError
        seq_eid = seq_sid + len(sub_seq)

        # check sub_seq values one by one with seq values
        for seq_val, sub_seq_val in zip(seq[seq_sid:seq_eid], sub_seq):
            if seq_val != sub_seq_val:
                return False

        return True
    except IndexError or KeyError:
        pass
    
    return False

def dfs(graph, num):
    """
    Description:
    -----------
        This method runs Depth First Search of 'graph' from a 'num'
        
        Time complexity: big O(N)
            - M: len(sequence)
            - N: len(sub_sequences)
            - L: max(sub_sequences[i])

    Parameters:
    -----------
        graph : The graph
                - key: The beginning of sub-sequence
                - val: The expected next begining balue of another sub-sequence
        num : The beginning of sub-sequcence
    Returns:
    --------
        Return True if the graph reachs to the end(None), otherwise return False
    """
    # Base cases
    if num is None:
        return True
    
    if num not in graph:
        return False

    # Recurse over to the next sub-sequence
    for next_num in graph[num]:
        if dfs(graph, next_num):
            return True
    return False

def CanConstruct(sequence: list, sub_sequences: list):
    """
    Description:
    -----------
        This method checks if sequence can be constructed by sub-sequences

        Time complexity: big O(M*L + N)
            - M: len(sequence)
            - N: len(sub_sequences)
            - L: max(sub_sequences[i])

    Parameters:
    -----------
        sequence : The sequence
        sub_sequences : The list of sub-sequences
    Returns:
    --------
        Return True if sequence can be constructed by sub-sequences, otherwise return False
    """

    # Base cases
    if len(sequence) < 1:
        return True
    
    if len(sub_sequences) < 1:
        return False

    # Build index dictionary for sequ
    # ence
    seq_index_dict = {num: idx for idx, num in enumerate(sequence)}                 # bigO(M)

    # Build graph of sub_sequence
    sub_seq_graph = defaultdict(list)
    for sub_seq in sub_sequences:                                                   # bigO(M*L)
        if contains(sequence, seq_index_dict, sub_seq):                             # bigO(L)
            if sequence[-1] == sub_seq[-1]:
                next_num = None
            else:
                next_idx = seq_index_dict[sub_seq[-1]]
                next_num = sequence[next_idx]
            sub_seq_graph[sub_seq[0]].append(next_num)
    
    # DFS to check if sequence can be contructed by sub_seq_graph
    return dfs(sub_seq_graph, sequence[0])                                          # bigO(N)

def main():
    test_cases = [
        ([[1, 2, 3, 4, 5], [[1,2],[3,4],[5]]], True),
        ([[1, 3, 4, 5, 2], [[2,3],[1,3],[4,2],[2],[4,5]]], True),
        ([[1, 2, 3, 4, 5], [[2,3],[1,3],[4,2],[4,5]]], False),
        ([[1, 2, 3, 4, 5], [[2,3],[3],[1,2],[4,5]]], True),
        ([[1, 2, 3, 4, 5], [[2,3],[1,2],[4,5]]], False),

        ([[1, 2, 3, 4], [[3,4],[1,2]]], True),
        
        ([[], [[2,3],[1,2],[4,5]]], True),
        ([[1, 2, 3, 4, 5], []], False),
        
        ([[1, 2, 3], [[1,2,3]]], True),
        ([[1, 2, 3], [[1],[1,2],[1,2,3]]], True),
        ([[1, 2, 3], [[1],[2],[3]]], True),
        ([[1, 2, 3], [[1,2,3]]], True),
        ([[1, 2, 3], [[3],[1],[1,2]]], True),
        ([[1, 2, 3], [[2,3],[1,2],[1]]], True),
    ]
    
    all_passed = True    
    for input, target in test_cases:
        print()
        print("input : {}".format(input))
        start = timeit.default_timer()
        actual = CanConstruct(input[0], input[1])
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