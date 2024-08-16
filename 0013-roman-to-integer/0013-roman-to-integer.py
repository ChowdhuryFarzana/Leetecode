class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
        total_value = 0
        i = 0
    
        while i < len(s):
        # Check if this character and the next character form a subtraction case
            if i + 1 < len(s) and roman_to_int_map[s[i]] < roman_to_int_map[s[i + 1]]:
            # Subtraction case, add the difference
                total_value += roman_to_int_map[s[i + 1]] - roman_to_int_map[s[i]]
            # Move to the next pair of characters
                i += 2
            else:
            # Normal case, add the value of the current character
                total_value += roman_to_int_map[s[i]]
            # Move to the next character
                i += 1
        return total_value


        