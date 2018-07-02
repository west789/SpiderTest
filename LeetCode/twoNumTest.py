class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j]==target:
                    return [nums[i], nums[j]]


solution = Solution()
content = input("请输入内容:")
res = solution.twoSum([2, 8, 2, 6], int(content))
print(res)
