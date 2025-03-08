from typing import List
import math


"""
Given two positive integers left and right, find the two integers num1 and num2 such that:

left <= num1 < num2 <= right .
Both num1 and num2 are prime numbers.
num2 - num1 is the minimum amongst all other pairs satisfying the above conditions.
Return the positive integer array ans = [num1, num2]. If there are multiple pairs satisfying these conditions, return the one with the smallest num1 value. If no such numbers exist, return [-1, -1].

 

Example 1:

Input: left = 10, right = 19
Output: [11,13]
Explanation: The prime numbers between 10 and 19 are 11, 13, 17, and 19.
The closest gap between any pair is 2, which can be achieved by [11,13] or [17,19].
Since 11 is smaller than 17, we return the first pair.
"""

class Solution:
    def is_prime(self, n: int) -> bool:
        if n < 2:
            return False
        if n in (2, 3):
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        for i in range(5, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True

    def closestPrimes(self, left: int, right: int) -> List[int]:
        primes = [i for i in range(left, right + 1) if self.is_prime(i)]

        if len(primes) < 2:
            return [-1, -1]

        min_diff = float('inf')
        best_pair = [-1, -1]

        for i in range(len(primes) - 1):
            diff = primes[i + 1] - primes[i]
            if diff < min_diff:
                min_diff = diff
                best_pair = [primes[i], primes[i + 1]]

        return best_pair
