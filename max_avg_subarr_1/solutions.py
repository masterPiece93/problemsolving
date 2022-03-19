from typing import List

# Solution 1 -------------------------------------------------


class Solution:
    @staticmethod
    def solution1(nums: List[int], k: int) -> bool:
        """sliding window solution"""

        # defining a window : |(i) ---- (j)|
        i = 0
        j = i + k
        # sum of elements lying initially withing the window -
        current_window_sum = sum(nums[i:j])
        # global storage to keep track of max sum found till date -
        max_sum = current_window_sum

        # start sliding i and j , till 'j' reaches end of array
        while j < len(nums):
            # sum of new window
            current_window_sum += nums[j] - nums[i]
            if current_window_sum > max_sum:
                max_sum = current_window_sum
            i += 1
            j += 1
        return max_sum / k


# ------------------------------------------------------------
# ------------------------------------------------------------
