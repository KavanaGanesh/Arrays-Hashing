"""Isomorphic strings: strings that can be consistently replaced """
'''"egg" and "add" are isomorphic because you can map 'e' to 'a', 'g' to 'd'''

# conditions to check:
# 1. char can be present as a key {p:t} - True ideal this is what i am considering
# 2. the same char can be pointed to another char as a value{p:f} - this is False
# 3. the same char can be present as a value mapped to another char as key {a:p} - this is False too

# 1) check if both the length of strings doesnot match  - return False
# 2) if the length matches: now create another dictionary, to map as the key - value pair using zip(s1,s2) 
# 3) now all char in s1 are keys: with this condition:
    # 4) check if each char is not mapping to y -  return False
# 5) if the same key is also present in values - return False  
# 6) just add the unique key-value to makiing it a proper key-value dictionary
# 7) Finally return True
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        order_dict = dict()
        for i , (x, y) in enumerate(zip(s,t)):
            print(i, x, y)

            if x in order_dict.keys():
                if order_dict[x] != y:
                    return False
            else:
                if x in order_dict.values():
                    return False
            order_dict[x] = y
        return True
 

# s = "egg"
# t = "add"
# s = "foo"
# t = "bar"
# s = "paper"
# t = "title"
s = "aab" 
t = "xxy"
print(Solution().isIsomorphic(s,t))