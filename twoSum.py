""" Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice."""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        modified_nums = [-x + target for x in nums]
        potential_numbers = list(set(nums) & set(modified_nums))
        if len(potential_numbers) == 1:
            result = [i for i, val in enumerate(nums) if val == potential_numbers[0]]
        else:
            result = [nums.index(x) for x in potential_numbers if nums.index(x) != modified_nums.index(x)]
        if len(result) == 2:
            return sorted(result)
            
  """ Comments:
  Time complexity : O(n)
  """
            
