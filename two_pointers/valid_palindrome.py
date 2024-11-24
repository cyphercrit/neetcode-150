'''
Given a string s, return true if it is a palindrome, otherwise return false.

A palindrome is a string that reads the same forward and backward. It is
also case-insensitive and ignores all non-alphanumeric characters.
'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            # skips non-alphanum characters
            if not s[left].isalnum():
                left += 1
                continue

            if not s[right].isalnum():
                right -= 1
                continue
            
            # returrns false if characters do not match, without regard to case
            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1
        
        return True
