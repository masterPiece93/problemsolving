# PROBLEM ID : MINDIFFBTWHIGHLOW
import time
from pprint import pprint
from min_diff_btw_high_low.solutions import Solution

# -----------
# solution 1 :
# -----------
print("-" * 10 + "\n" + "SOLUTION 1" + "\n" + "-" * 10)
INPUT1 = dict()
start = time.perf_counter()
sol = Solution.solution(**INPUT1)
end = time.perf_counter()
print(f"\t|on INPUT 1|: ")
pprint({"output": sol, "time_taken": end - start})

print("\n")
