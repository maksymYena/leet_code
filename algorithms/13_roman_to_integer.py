class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {
            "I": 1, "V": 5, "X": 10, "L": 50,
            "C": 100, "D": 500, "M": 1000
        }

        sum = 0
        prev_value = 0

        for char in reversed(s):
            cur_value = roman_dict.get(char)
            print(f"cur_value => {cur_value}")
            print(f"prev_value => {prev_value}")
            if cur_value < prev_value:
                sum -= cur_value
                print(f"sum value = {sum} in case if cur_value < prev_value")
            else:
                sum += cur_value
                print(f"sum value = {sum} in case if cur_value >= prev_value")

            prev_value = cur_value
            print(f"updating prev_value to cur_value and the result is {prev_value}")
        return sum
