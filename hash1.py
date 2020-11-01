# Given a string s, find the length of the longest substring without repeating characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        biggest_substring = 0
        #caracter_dict = {}
        if (len(s) >= 0) and (len(s) <= 5 * (10**4)):
            if len(s) > 0:
                for i in range(0, len(s)):
                    counter = 0
                    for j in range(i, len(s)):
                        if s[j] not in s[i:j]:
                            counter += 1
                        else:
                            if counter > biggest_substring:
                                biggest_substring = counter
                            break
                        if counter > biggest_substring:
                            biggest_substring = counter
                return biggest_substring
            else:
                return 0
            
        
        
        
     #   s = 'abcda'
     #   s = 'p'
     #   s = "abcabcbb"
    