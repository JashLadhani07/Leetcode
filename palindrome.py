class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        for i in range(len(x) // 2):
            if x[i] != x[-(i+1)]:
                print("False")
                return False
        print("True")
        return True
Solution().isPalindrome(1221)