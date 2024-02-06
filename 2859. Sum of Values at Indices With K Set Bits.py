"""Approach
To solve the problem of summing elements from a list based on the 
number of set bits in their indices' binary representation, 
we iterate through each index of the input list. 
For every index, we convert it into its binary representation and 
count the number of set bits ('1's) using the bin() function and count() method. 
We compare this count with the given value k to determine if the index satisfies the condition. 
If the count matches k, we add the corresponding element from the list to a running sum. 
Finally, we return the sum as the result. This approach ensures that we accurately identify 
and sum the elements whose indices have exactly k set bits in their binary representation, providing an efficient 
solution to the problem.

Complexity
Time complexity: O(n * log(n))
Space complexity: O(1)"""

class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        sum = 0
        for i in range(len(nums)):
            if int(bin(i).count(str('1'))) == k:
                sum += nums[i]
        return sum