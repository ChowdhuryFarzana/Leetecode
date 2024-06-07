class Solution:
    def isPalindrome(self, s: str) -> bool:
         s_cleaned = ''.join(char.lower() for char in s if char.isalnum())

         s_flipped = s_cleaned[::-1]

         return s_flipped == s_cleaned
        