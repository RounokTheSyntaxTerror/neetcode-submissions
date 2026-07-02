class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        bucket = set()
        for i in range(len(nums)):
            if nums[i] in bucket:
                return True
            bucket.add(nums[i])
        return False
        