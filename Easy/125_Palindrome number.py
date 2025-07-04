class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Filter only alphanumeric characters and convert to lowercase
        filtered = [c.lower() for c in s if c.isalnum()]
        # Check if the filtered list is the same forwards and backwards
        return filtered == filtered[::-1]
