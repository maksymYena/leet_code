from typing import List


"""
You are given a 0-indexed array of strings words and a character x.

Return an array of indices representing the words that contain the character x.

Note that the returned array may be in any order.

Example 1:

Input: words = ["leet","code"], x = "e"
Output: [0,1]
Explanation: "e" occurs in both words: "leet", and "code". Hence, we return indices 0 and 1.
"""

def findWordsContaining(words: List[str], x: str) -> List[int]:
    result_array = []
    for i in range(0, len(words)):
        print(f"current word to check = {words[i]}")
        if words[i].__contains__(x):
            result_array.append(i)

    return result_array




print(findWordsContaining(words = ["leet","code"], x = "e"))