from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        unique_elems = set()
        for num in nums:
            if num not in unique_elems:
                unique_elems.add(num)
                nums[k] = num
                k += 1

        return k


class SolutionTwoPointer:
    # Since nums is sorted, duplicates are always adjacent, so we don't need
    # a set to remember every value we've seen — comparing each element to
    # the last one written is enough. This drops space from O(n) to O(1),
    # which matters at the array's upper bound of 3 * 10^4 elements.
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[k - 1]:
                nums[k] = nums[i]
                k += 1

        return k
