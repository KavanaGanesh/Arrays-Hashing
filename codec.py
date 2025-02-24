# Algorithm for encoding:
# create an empty string
# pick each word from list of string
    # keep adding the length of the word + *(Special symbol) +  the word
#finally using .join method return one whole sentence

#Algorithm for decoding:
# create an empty list. keep 2 pointers i,j
# keep i pointer to iterate over each character untill it exceeds the length of the string
    # make j pointer = i pointer
    # check if each character is a special symbol? "5*hello"
        # if not keep incrementing j pointer to find the special symbol

    # extract the length of integer using string split
    # then extract the length of the string by splitting and appending
    # finally make ipointer to point to the next "number*stringword" ex:"5*world"
# return the list

from typing import List
class Solution:

    def encode(self, strs: List[str]) -> str:
        strs_res = ""
        for s in strs:
            strs_res += str(len(s)) + '*' + s 
        return "".join(strs_res)


    def decode(self, s: str) -> List[str]:
        decoded_strings = []
        i = 0
        n = len(s)

        while i < n:
            j=i

            while s[j] != '*':
                j+=1
            length = int(s[i:j])
            decoded_strings.append(s[j+1:j+1+length])      
            
            i = j+1+length
        return decoded_strings
    

strs = ["hello", "world", "leetcode", "example"]

# Example of how the Codec class is expected to be used:
encode_result = Solution().encode(strs)
decode_result = Solution().decode(encode_result)
print(encode_result)
print(decode_result)

