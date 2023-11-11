class Solution(object):
    def merge(self, nums1, m, nums2, n):
        res = []
        res.extend(nums1[:m])
        res.extend(nums2[:n])

        # Sort the merged list
        res.sort()
        
        return res


nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
obj = Solution()
result = obj.merge(nums1,m,nums2,n)
print(result)