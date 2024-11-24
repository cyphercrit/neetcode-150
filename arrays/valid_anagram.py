'''
Given two strings s and t, return true if the two strings 
are anagrams of each other, otherwise return false.
'''

# Time Complexity: O(n)
# Space Complexity: O(1) - max number of characters in a map is 26
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # words can't be an anagram if they aren't the same length
        if len(s) != len(t):
            return False

        sCounter = {}
        tCounter = {}

        # creates two maps that count the number of each char
        for c1, c2 in zip(s, t):
            if c1 in sCounter:
                sCounter[c1] += 1
            else:
                sCounter[c1] = 1
            
            if c2 in tCounter:
                tCounter[c2] += 1
            else:
                tCounter[c2] = 1
        
        # if the two maps are the same, the words must be valid anagrams
        return sCounter == tCounter