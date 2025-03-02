

"""
You are given positive integers n and m.

Define two integers as follows:

num1: The sum of all integers in the range [1, n] (both inclusive) that are not divisible by m.
num2: The sum of all integers in the range [1, n] (both inclusive) that are divisible by m.
Return the integer num1 - num2.
"""

def differenceOfSums(n: int, m: int) -> int:
    non_divisible_list = []
    divisible_list = []

    for i in range(1, n + 1):
        print(f"result of division of {i} / {m} == {i % m}")
        if i % m != 0:
            non_divisible_list.append(i)
        else:
            divisible_list.append(i)
    print(f"{non_divisible_list} - {divisible_list}")
    return sum(non_divisible_list) - sum(divisible_list)



print(differenceOfSums(10, 3))