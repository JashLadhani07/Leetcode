class Solution():
    def twoSum(self,num,target):
        for i in range(len(num)):
            for j in range(i+1,len(num)):
                if num[i] + num[j] == target:
                    return i,j
Solution().twoSum([2,7,11,15],9) 
        
