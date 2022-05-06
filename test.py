import timeit

num_runs = 10000000

a = 1
b = 2
c = 2
cnt = 0

start = timeit.default_timer()
for _ in range(num_runs):
    if a < b:
        a = 1

stop = timeit.default_timer()
print('Time: ', stop - start) 

start = timeit.default_timer()
for _ in range(num_runs):
    if a <= b:
        a = 1

stop = timeit.default_timer()
print('Time: ', stop - start) 



