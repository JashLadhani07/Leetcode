#class Solution:
#    def containsDuplicate(self, nums: list[int]) -> bool:
#        duplicate = False
#        for i in range(len(nums)):
#           for j in range(i+1,len(nums)):
#              if nums[i] == nums[j]:
#                    print(f"Duplicate of {nums[i]} at location {j}")
#                    duplicate = True
#        return duplicate
#Solution().containsDuplicate([1,2,3,1,1,2])
#time complexity for this is too much therefore not used O(n^2)
#instead
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        dup = False
        for i in range(len(nums)):
            if nums[i] in seen:
                print(f"Duplicate of {nums[i]} at location {i}")
                dup = True
            else:
                seen.add(nums[i])
        return dup
Solution().containsDuplicate([1,2,3,1,1,2])
