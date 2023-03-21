class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        matches = []
        match = ''
        for index,word in enumerate(strs):
            my_index_word = strs[0]
            for index,letter in enumerate(word):
                try:
                    if letter == my_index_word[index]:
                        match += letter
                    else:
                        break
                except:
                    continue
            matches.append(match)
            match = ''
        winning_match = min(matches, key=len)
        return winning_match


answer = Solution()
answer.longestCommonPrefix(['flower','flow','flannel','flask','flennery'])
answer.longestCommonPrefix(['canon','can','canonball','canadian','canada'])
answer.longestCommonPrefix(["cir","car"])
