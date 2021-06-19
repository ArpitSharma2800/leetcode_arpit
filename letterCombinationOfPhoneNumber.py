# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

# A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

# Brute Force technique amd backtracking solution

# worst case scenrio O(n.4^n)
from typing import List


def letterCombinations(digits: str) -> List[str]:
    result = []
    digitChar = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "qprs",
        "8": "tuv",
        "9": "wxyz",
    }

    def tracking(i, curr):
        if len(curr) == len(digits):
            result.append(curr)
            return
        for l in digitChar[digits[i]]:
            tracking(i+1, curr + l)

    if digits:
        tracking(0, "")

    return result


print(letterCombinations("9928926428"))
