class Solution:

    """
    Given a string s, return true if s is a good string, or false otherwise.
    A string s is good if all the characters that appear in s have the same number of occurrences (i.e., the same frequency).
    """
    def areOccurrencesEqual(self, s: str) -> bool:
        result_dict = dict()
        for i in range(0, len(s)):
            result_dict.setdefault(s[i], 0)
            result_dict[s[i]] = result_dict[s[i]] + 1

        frequency_set = set()
        for i in result_dict.keys():
            frequency_set.add(result_dict[i])

        return len(frequency_set) == 1


cls = Solution
print(cls.areOccurrencesEqual(cls, "aaabbb"))