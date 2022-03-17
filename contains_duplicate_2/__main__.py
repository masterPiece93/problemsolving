# PROBLEM ID : CONDUP2
import time
from pprint import pprint
from contains_duplicate_2.solutions import Solution

# -----------
# solution 1 :
# -----------
print("-" * 10 + "\n" + "SOLUTION 1" + "\n" + "-" * 10)
INPUT1 = dict(nums=[1, 0, 1, 1], k=1)
start = time.perf_counter()
sol = Solution.solution1(**INPUT1)
end = time.perf_counter()
print(f"\t|on INPUT 1|: ")
pprint({"output": sol, "time_taken": end - start})

INPUT2 = dict(nums=[1, 2, 3, 1, 2, 3], k=2)
start = time.perf_counter()
sol = Solution.solution1(**INPUT2)
end = time.perf_counter()
print(f"\t|on INPUT 2|: ")
pprint({"output": sol, "time_taken": end - start})

print("\n")
# -----------
# solution 2 :
# -----------
print("-" * 10 + "\n" + "SOLUTION 2" + "\n" + "-" * 10)
INPUT1 = dict(nums=[1, 0, 1, 1], k=1)
start = time.perf_counter()
sol = Solution.solution2(**INPUT1)
end = time.perf_counter()
print(f"\t|on INPUT 1|: ")
pprint({"output": sol, "time_taken": end - start})

INPUT2 = dict(nums=[1, 2, 3, 1, 2, 3], k=2)
start = time.perf_counter()
sol = Solution.solution2(**INPUT2)
end = time.perf_counter()
print(f"\t|on INPUT 2|: ")
pprint({"output": sol, "time_taken": end - start})

INPUT3 = dict(nums=[1, 2, 3, 1], k=3)
start = time.perf_counter()
sol = Solution.solution2(**INPUT3)
end = time.perf_counter()
print(f"\t|on INPUT 3|: ")
pprint({"output": sol, "time_taken": end - start})

print("\n")
# -----------
# solution 3 :
# -----------
print("-" * 10 + "\n" + "SOLUTION 3" + "\n" + "-" * 10)
INPUT1 = dict(nums=[1, 0, 1, 1], k=1)
start = time.perf_counter()
sol = Solution.solution3(**INPUT1)
end = time.perf_counter()
print(f"\t|on INPUT 1|: ")
pprint({"output": sol, "time_taken": end - start})

INPUT2 = dict(nums=[1, 2, 3, 1, 2, 3], k=2)
start = time.perf_counter()
sol = Solution.solution3(**INPUT2)
end = time.perf_counter()
print(f"\t|on INPUT 2|: ")
pprint({"output": sol, "time_taken": end - start})

INPUT3 = dict(nums=[1, 2, 3, 1], k=3)
start = time.perf_counter()
sol = Solution.solution3(**INPUT3)
end = time.perf_counter()
print(f"\t|on INPUT 3|: ")
pprint({"output": sol, "time_taken": end - start})
