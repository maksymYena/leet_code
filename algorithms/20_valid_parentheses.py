
def isValid(s: str) -> bool:
    pairs = {
        "}": "{",
        "]": "[",
        ")": "("
    }

    stack = []

    for i in range(0, len(s)):
        if s[i] in pairs.values():
            stack.append(s[i])
        elif s[i] in pairs.keys():
            if len(stack) == 0 or pairs.get(s[i]) != stack.pop():
                return False

    return len(stack) == 0


print(isValid("[]["))