# (default dict - pass a list to the dict, and append works here as i am passing list to default dict)
# chosen default dict: it provides default values with non-existent keys
# Algorithm:
# create an empty dictionary using default dict of class list type
# pick each word with iteration in for loop:
    # sort and join each character
    # add the sorted char as key and word as value using append() method
# print the entire dictionary and extract what is needed
# In this case print only the values and convert into list



from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        order_dict = defaultdict(list)


        for strg in strs:
            sorted_strg = "".join(sorted(strg))
            order_dict[sorted_strg].append(strg)
        return list(order_dict.values())


strs = ["act","pots","tops","cat","stop","hat"]
print(Solution().groupAnagrams(strs))