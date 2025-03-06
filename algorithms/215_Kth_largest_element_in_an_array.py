import heapq
from typing import List

"""
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?
"""


def findKthLargest(nums: List[int], k: int) -> int:
    min_heap = []

    for num in nums:
        heapq.heappush(min_heap, num)
        if len(min_heap) > k:
            heapq.heappop(min_heap)

    return min_heap[0]


print(findKthLargest(nums=[3, 2, 3, 1, 2, 4, 5, 5, 6], k=4))
