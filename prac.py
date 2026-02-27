"""
this file to be sent to main dir 
"""

assortment = ["flower","flow","flight"]

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        shortest_word_len = min([len(word) for word in strs])
        shortest_word = ''
        for word in strs:
            if len(word) == shortest_word_len:
                shortest_word = word

        longest_common_prefix = ''

        for i in range(shortest_word_len):
            char = shortest_word[i]

            for word in strs:
                if word[i] != char:
                    return longest_common_prefix
                
            longest_common_prefix += char


        # longest_common_prefix = ''

        # for i in range(shortest_word_len):
        #     char = shortest_word[i]

        #     for word in strs:
        #         if word[i] != char:
        #             return longest_common_prefix
                
        #     longest_common_prefix += char

        # return longest_common_prefix
        

sol = Solution()
print(f'Longest common prefix: {sol.longestCommonPrefix(assortment)}')