class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = i+1
        while(i!=len(nums)):
            if i==j:
                j+=1
            elif j == len(nums):
                i +=1
                j = 0
            elif nums[i]+nums[j] == target:
                return[i,j]
            
            else:
                j+=1
