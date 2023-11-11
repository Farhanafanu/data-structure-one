class Solution(object):
    def findDisappearedNumbers(self, nums):
        result=[]
        for j in range(1,len(nums)):
            
            if j not in nums:
                result.append(j)
        return result
               
s=Solution()
nums = [4,3,2,7,8,2,3,1]

result =s.findDisappearedNumbers(nums)
print(result)

