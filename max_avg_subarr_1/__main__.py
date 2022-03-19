# PROBLEM ID : CONDUP2
import time
from pprint import pprint
from max_avg_subarr_1.solutions import Solution

# -----------
# solution 1 :
# -----------
print("-" * 10 + "\n" + "SOLUTION 1" + "\n" + "-" * 10)
INPUT1 = dict(nums=[1, 12, -5, -6, 50, 3], k=4)
start = time.perf_counter()
sol = Solution.solution1(**INPUT1)
end = time.perf_counter()
print(f"\t|on INPUT 1|: ")
pprint({"output": sol, "time_taken": end - start})

INPUT2 = dict(nums=[5], k=1)
start = time.perf_counter()
sol = Solution.solution1(**INPUT2)
end = time.perf_counter()
print(f"\t|on INPUT 2|: ")
pprint({"output": sol, "time_taken": end - start})

INPUT2 = dict(nums=[-1], k=1)
start = time.perf_counter()
sol = Solution.solution1(**INPUT2)
end = time.perf_counter()
print(f"\t|on INPUT 3|: ")
pprint({"output": sol, "time_taken": end - start})

print("\n")
