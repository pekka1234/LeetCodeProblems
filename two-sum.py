class Solution(object):
    def twoSum(self, nums, target):
        # the loops take a number from list and then checks the rest of the list's numbers for their sum like this:
        # if list is [3,5,5,1], the loop will check the sums like this:
        # 3+5, 3+5, 3+1
        # 5+5, 5+1
        # 5+1
        # so every combination gets cheked
        for x in range(len(nums)):
            for y in range(x + 1, len(nums)):
                if nums[x] + nums[y] == target:
                    return [x, y] 
