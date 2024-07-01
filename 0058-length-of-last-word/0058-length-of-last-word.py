class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        splitted_string = s.split()
        if not splitted_string:
            return 0
        return len(splitted_string[-1])
            