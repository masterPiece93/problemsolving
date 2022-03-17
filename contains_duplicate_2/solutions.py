from typing import List

# Solution 1 -------------------------------------------------


class Solution:
    @staticmethod
    def solution1(nums: List[int], k: int) -> bool:
        """brute force solution"""

        for i, num in enumerate(nums):
            for j, _num in enumerate(nums):
                if num == _num and i != j and abs(j - i) <= k:
                    return True

        return False

    @staticmethod
    def solution2(nums: List[int], k: int) -> bool:
        """with extra memory using dict"""

        reference_dict: dict = {}
        results = []
        for i, num in enumerate(nums):
            if num not in results:
                try:
                    index = reference_dict[num]
                    if abs(index - i) <= k:
                        results.append(num)
                    reference_dict[num] = i
                except KeyError:
                    reference_dict[num] = i

        return results != []

    @staticmethod
    def solution3(nums: List[int], k: int) -> bool:
        """advancement on solution2"""

        reference_dict: dict = {}
        for i in range(len(nums)):
            num = nums[i]

            if num in reference_dict:
                if abs(reference_dict[num] - i) <= k:
                    return True
            reference_dict[num] = i
        return False


# ------------------------------------------------------------
# ------------------------------------------------------------
