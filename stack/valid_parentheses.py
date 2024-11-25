'''
You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.

The input string s is valid if and only if:

    1. Every open bracket is closed by the same type of close bracket.
    2. Open brackets are closed in the correct order.
    3. Every close bracket has a corresponding open bracket of the same type.

Return true if s is a valid string, and false otherwise.
'''

# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        char_map = {
            "}" : "{",
            ")" : "(",
            "]" : "["
        }

        for char in s:
            # checks to see if char is one of the keys, if not, its a opening char
            if char not in char_map:
                stack.append(char)
            else:
                if not stack or stack[-1] != char_map[char]:
                    return False
                stack.pop()
        return True

