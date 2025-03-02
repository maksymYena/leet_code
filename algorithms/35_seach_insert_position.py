from typing import List

"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
"""


def searchInsert(nums: List[int], target: int) -> int:
    lower_index = 0
    top_index = len(nums) - 1

    while lower_index <= top_index:

        middle_index = (lower_index + top_index) //2
        middle_index_value = nums[middle_index]

        if middle_index_value == target:
            return middle_index

        elif middle_index_value > target:
            top_index = middle_index - 1
        else:
            lower_index = middle_index + 1

    return lower_index


print(searchInsert(nums = [1,3,5,6], target = 5))