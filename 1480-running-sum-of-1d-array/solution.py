from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running_sum = []
        aggregate = 0
        for number in nums:
            aggregate += number
            running_sum.append(aggregate)
        return running_sum
