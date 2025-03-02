from typing import List


def longestCommonPrefix(strs: List[str]) -> str:
    chars_and_length = dict()

    for i in strs:
        chars_and_length[i] = len(i)

    print(chars_and_length)




print(longestCommonPrefix(["flower","flow","flight"]))