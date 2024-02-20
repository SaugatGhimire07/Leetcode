class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start_point = 0
        end_point = len(nums)-1
        
        while start_point <= end_point:
            mid_point = start_point + (end_point - start_point) // 2
            mid_value = nums[mid_point]
            
            if mid_value == target:
                return mid_point
            elif mid_value > target:
                end_point = mid_point - 1
            else:
                start_point = mid_point + 1
        return -1

            