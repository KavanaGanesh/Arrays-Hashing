# 1) magazine has more number of characters and from magazine check if ransomenote can be made
# 2) so pass the magazine into counter from collections module
# 3) now pick each character and keep decrementing the count correpsonding to character
# 4) when the count of the char becomes less than 0  - that shows ransomenote cannnot be made from magazine return False
# 5) Finally return True

# complexity: Time = O(n)
# space = O(n)

from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = Counter(magazine) 
     
        for char in ransomNote:
            count[char]-=1
            if count[char]<0:
                return False
        return True

ransomNote = "a"
magazine = "b"
# ransomNote = "aa"
# magazine = "ab"
# ransomNote = "aa"
# magazine = "aab"
print(Solution().canConstruct(ransomNote,magazine))
        