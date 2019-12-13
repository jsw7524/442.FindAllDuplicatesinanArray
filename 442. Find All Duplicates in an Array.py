class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result=[]
        for n in nums:
            nums[abs(n)-1]=-1*nums[abs(n)-1]
        for i,n in zip(range(len(nums)),nums):
            if nums[abs(n)-1] > 0:
                result.append(abs(nums[i]))
        return list(set(result))


sln=Solution()
assert [2,3]==sln.findDuplicates([4,3,2,7,8,2,3,1])