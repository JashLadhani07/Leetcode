from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        
        # Traverse the list from the end
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            # If digit is 9, set it to 0 and continue to carry
            digits[i] = 0
        
        # If all digits were 9, we need an extra digit at the beginning
        return [1] + [0] * n
