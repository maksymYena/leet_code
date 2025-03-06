"""
You are given a 0-indexed 2D integer matrix grid of size n * n with values in the range [1, n2]. Each integer appears exactly once except a which appears twice and b which is missing. The task is to find the repeating and missing numbers a and b.

Return a 0-indexed integer array ans of size 2 where ans[0] equals to a and ans[1] equals to b.
"""
from typing import List


class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        return list([self.find_repated_value(grid), self.find_missing_value(grid)])

    def find_missing_value(self, grid: List[List[int]]) -> int:
        all_value = list()
        missed_value = list()
        for i in grid:
            for j in i:
                all_value.append(j)

        for i in range(1, len(all_value) + 1):
            if not all_value.__contains__(i):
                missed_value.append(i)

        return missed_value[0]

    def find_repated_value(self, grid: List[List[int]]) -> int:
        all_values = list()
        repeated = list()
        for i in grid:
            for j in i:
                if all_values.__contains__(j):
                    repeated.append(j)
                else:
                    all_values.append(j)

        return repeated[0]


clz = Solution()

print(clz.findMissingAndRepeatedValues(grid=[[1, 3], [2, 2]]))
