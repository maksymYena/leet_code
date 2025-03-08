from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        result_array = []
        for i in range(0, n + 1):
            value = int(bin(i).replace("0b", ""))
            result_array.append(self.calculate_sum_of_digit(value))

        return result_array

    def calculate_sum_of_digit(self, value: int) -> int:
        sum = 0
        while value != 0:
            tmp = value % 10
            value //= 10
            sum += tmp
        return sum


clazz = Solution()
print(clazz.countBits(n=5))
