"""
Welcome to Meta!

This is just a simple shared plaintext pad, with no execution capabilities.

When you know what language you would like to use during your interview,
simply choose it from the dropdown in the top bar.

Enjoy your interview!
"""

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
  actual = answerQueries(queries, N)
  check(expected, actual)
  

if __name__ == "__main__":
  main()
  