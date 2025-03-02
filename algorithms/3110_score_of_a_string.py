"""
You are given a string s.
The score of a string is defined as the sum of the absolute difference between the ASCII values of adjacent characters.
Return the score of s.
"""


# Ord function is used for getting ASCII code of char

def scoreOfString(s: str) -> int:
    sum = 0
    for i in range(0, len(s) - 1):
        sum += abs(ord(s[i]) - ord(s[i + 1]))
        print(sum)
    return sum


print(scoreOfString("hello"))
