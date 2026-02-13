"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""

assortment = ["flower","flow","flight"]

class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        
        shortest_word_len = min(len(word) for word in strs)
        longest_common_prefix = ""
        
        for i in range(shortest_word_len):
            current_char = strs[0][i]            

            for word in strs:
                if word[i] != current_char:
                    return longest_common_prefix
            
            longest_common_prefix += current_char
            # print(f'current largest prefix: \t{longest_common_prefix}')
        
        return longest_common_prefix



sol = Solution()
print(f'largest common prefix: \t{sol.longestCommonPrefix(assortment)}')