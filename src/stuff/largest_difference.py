import random
import time

def largest_differences(lst):
    """
    Largest difference from list elements:
    O(n^2)
    """
    max_so_far = 0
    for i in range(0, len(lst) - 1):
        for j in range(i+1, len(lst)):
            max_so_far = max(max_so_far, lst[j] - lst[i])
    return max_so_far

def largest_differences2(lst):
    """
    Largest difference from list elements:
    O(n)
    """
    cur_max, max_so_far = 0, 0
    for i in range(1, len(lst)):
        cur_max = max(0, cur_max + lst[i] - lst[i -1 ])
        max_so_far = max(max_so_far, cur_max)
    return max_so_far


def generate_list(n):
    res = []
    for i in range(n):
        res.append(random.randint(1,10))
    return res

ex = [7, 1, 4, 5, 6, 8]
lst = generate_list(100)
lst = ex

start_time = time.time()
res = largest_differences(lst)
print(res)
print(f'[+] Execution time for O(n^2): {time.time() - start_time}')
    
start_time2 = time.time()
res2 = largest_differences2(lst)
print(res2)
print(f'[+] Execution time for O(n): {time.time() - start_time2}')
