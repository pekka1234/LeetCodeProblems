class Solution(object):
    def twoSum(self, nums, target):
        anwser = []
        for x in range(len(nums)):
            for y in range(x + 1, len(nums)):
                if nums[x] + nums[y] == target:
                    if (x not in anwser) and (y not in anwser):
                        anwser.append(x)
                        anwser.append(y)
        return anwser
