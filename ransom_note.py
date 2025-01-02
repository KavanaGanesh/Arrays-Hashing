from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = Counter(magazine) 
     
        for char in ransomNote:
            count[char]-=1
            if count[char]<0:
                return False
        return True

# ransomNote = "a"
# magazine = "b"
# ransomNote = "aa"
# magazine = "ab"
ransomNote = "aa"
magazine = "aab"
print(Solution().canConstruct(ransomNote,magazine))
        