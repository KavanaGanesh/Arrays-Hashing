class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dict_pattern ={}
        dict_s ={}
        if len(s.split()) != len(pattern):
            return False
        for char, word in zip(pattern, s.split()):
            if (char in dict_pattern and dict_pattern[char]!=word) or \
            (word in dict_s and dict_s[word] != char):
                return False
            
            dict_pattern[char] = word
            dict_s[word] = char
        return True

pattern = 'abba'
s = 'dog cat cat dog'
# pattern = "abba"
# s = "dog dog dog dog"
# pattern = "abba"
# s = "dog cat cat fish"
# pattern = "aaaa"
# s = "dog cat cat dog"
print(Solution().wordPattern(pattern,s))