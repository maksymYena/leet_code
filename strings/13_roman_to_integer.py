class Solution:
    def romanToInt(self, s: str) -> int:
        result_dict = self.roman_dict()
        sum = 0
        i = 0

        while i < len(s):
            cur_int = result_dict.get(s[i], 0)

            if i < len(s) - 1:
                if s[i] == 'I' and s[i + 1] == "V":
                    cur_int = 4
                    i += 1
                elif s[i] == 'I' and s[i + 1] == "X":
                    cur_int = 9
                    i += 1
                elif s[i] == 'X' and s[i + 1] == "L":
                    cur_int = 40
                    i += 1
                elif s[i] == 'X' and s[i + 1] == "C":
                    cur_int = 90
                    i += 1
                elif s[i] == 'C' and s[i + 1] == "D":
                    cur_int = 400
                    i += 1
                elif s[i] == 'C' and s[i + 1] == "M":
                    cur_int = 900
                    i += 1

            sum += cur_int
            i += 1

        return sum

    def roman_dict(self) -> dict:
        return {
            "I": 1, "V": 5, "X": 10, "L": 50,
            "C": 100, "D": 500, "M": 1000
        }


sol = Solution()
print(sol.romanToInt("MCMXCIV"))  # 1994
print(sol.romanToInt("III"))      # 3
print(sol.romanToInt("LVIII"))    # 58
