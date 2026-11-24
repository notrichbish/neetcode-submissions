class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        for i in range(0, len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            first = i
            second = i + 1 
            last = len(nums) - 1
            while second < last:
                target = nums[first] + nums[second] + nums [last] 
                if target == 0:
                    res.append([nums[first], nums[second], nums[last]])
                    second += 1
                    last -= 1
                    while second < last and nums[second] == nums[second-1]:
                        second +=1
                elif target < 0:
                    second += 1
                else:
                    last -= 1
        return res