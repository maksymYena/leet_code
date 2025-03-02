from typing import List


"""
In the town of Digitville, there was a list of numbers called nums containing integers from 0 to n - 1. 
Each number was supposed to appear exactly once in the list, however, two mischievous numbers sneaked in an additional time, making the list longer than usual.

As the town detective, your task is to find these two sneaky numbers. 
Return an array of size two containing the two numbers (in any order), so peace can return to Digitville.
"""
def getSneakyNumbers(nums: List[int]) -> List[int]:
    result_dict = {}
    result_list = []
    for i in nums:
        result_dict[i] = result_dict.get(i, 0) + 1

    for i in result_dict.keys():
        if result_dict[i] == 2 and len(result_list) < 2:
            result_list.append(i)

    return result_list




print(getSneakyNumbers([7,1,5,4,3,4,6,0,9,5,8,2]))