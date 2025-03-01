from typing import List


class Solution:
    """
    You are given a 0-indexed array nums of size n consisting of non-negative integers.

You need to apply n - 1 operations to this array where, in the ith operation (0-indexed),
you will apply the following on the ith element of nums:

If nums[i] == nums[i + 1], then multiply nums[i] by 2 and set nums[i + 1] to 0. Otherwise, you skip this operation.
After performing all the operations, shift all the 0's to the end of the array.

For example, the array [1,0,2,0,0,1] after shifting all its 0's to the end, is [1,2,1,0,0,0].
Return the resulting array.

Note that the operations are applied sequentially, not all at once.
    """

    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(0, len(nums) - 1):
            if nums.__getitem__(i) == nums.__getitem__(i + 1):
                nums.__setitem__(i, nums.__getitem__(i) * 2)
                nums.__setitem__(i + 1, 0)

        tmp_arr = list(filter(lambda cur_value: cur_value > 0, nums))
        tmp_arr.extend(list(filter(lambda cur_value: cur_value == 0, nums)))
        return tmp_arr
