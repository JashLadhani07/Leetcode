class Solution:
    def romanToInt(self, s: str) -> int:
        roman_no = {'I':1,'V':5,'X':10,'L':50,'C':100,
                    'D':500,'M':1000}
        prev = 0
        int_val = 0
        for i in reversed(s.upper()):
            curr = roman_no[i]
            if curr < prev:
                int_val = int_val-curr
            else:
                int_val = int_val+curr
                prev = curr
        print(int_val)
        return int_val
Solution().romanToInt('iv')