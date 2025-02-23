# Algorithm:
# there will be couple of mapping scenarios [a: dog, a:cat, b:dog]
# 1) if the length doesnot match with both the strings : return False
# 2) Keep 2 dictionaries for each string and try to do the unique mapping for each char and word
# 3) use zip to play with both strings (make sure the other string is split with spaces)
# 4) condition: if char in new_dict_char and new_dict_char[char] is not equal or if word in new_dict_word and new_dict_word[word] is not equal - return FALSE
# 5) otherwise keep adding the unique key and value for both the dictionaries
# 6) finally return True

# complexities SPace = O(N)
# Time = O(n)
from collections import defaultdict

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

# another solution :Kavana: not passing one more scenario

# class Solution(): 
#     def wordPattern(self, pattern , s):
#         new_dict = defaultdict()
#         for x , y in zip(pattern, s.split()):
#             if x not in new_dict.keys() and y not in new_dict.values():
#                 new_dict[x] = y
#         return new_dict

        # result_string = ""
        # for char in pattern:
        #     result_string = result_string + new_dict[char] + " "
        # return True if result_string.split() == s.split() else False
        


# pattern = 'abba'
# s = 'dog cat cat dog'
pattern = "abba"
s = "dog dog dog dog"
# pattern = "abba"
# s = "dog cat cat fish"
# pattern = "aaaa"
# s = "dog cat cat dog"
print(Solution().wordPattern(pattern,s))