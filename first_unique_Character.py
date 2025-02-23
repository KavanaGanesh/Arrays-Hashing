# Given a string s, find the first non-repeating character in it and return its index.
# If it does not exist, return -1.

# Algorithm:
# 1) pass the string into the counter
# 2) since i need to print the index , will loop through the enumerate()
# 3) check if the count[char] == 1, if yes - then print the index
# 4) if not return -1

from collections import Counter

class Solution:
    def unique_index(self, s):
        count = Counter(s)

        for index, char in enumerate(s):
            if count[char] == 1:
                return index
        return -1


s = "leetcode"
# Output: 0
print(Solution().unique_index(s))