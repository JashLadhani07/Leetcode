class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        
        # 1. Skip trailing spaces at the end
        while i >= 0 and s[i] == ' ':
            i -= 1
        
        # Mark end of the last word
        end = i
        
        # 2. Move backwards until beginning of word or string
        while i >= 0 and s[i] != ' ':
            i -= 1
        
        # Length = end - i
        return end - i
