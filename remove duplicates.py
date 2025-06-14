class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i = 0
        while i < len(nums):
            j = i+1
            while j <len(nums):
                if nums[i] == nums[j]:
                    nums.pop(j)
                else:
                    j+=1
            i+=1
        print(nums)
        return len(nums)
Solution().removeDuplicates([9, 8, 8, 7, 5, 2, 1, 1])

