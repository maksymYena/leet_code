
"""
You are given a string date representing a Gregorian calendar date in the yyyy-mm-dd format.

date can be written in its binary representation obtained by converting year, month, and day to their binary representations without any leading zeroes and writing them down in year-month-day format.

Return the binary representation of date.
"""


class Solution:
    def convertDateToBinary(self, date: str) -> str:
        result_array = []
        for i in date.split("-"):
            result_array.append(bin(int(i)).replace("0b", ""))

        return f"{result_array[0]}-{result_array[1]}-{result_array[2]}"