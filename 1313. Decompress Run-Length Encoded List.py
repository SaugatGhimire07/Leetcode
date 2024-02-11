class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        arr = []

        count = 0
        i = 0
        while count < len(nums):
            for j in range(nums[count]):
                arr.append(nums[count+1])
            count += 2
            i += 1
        return arr