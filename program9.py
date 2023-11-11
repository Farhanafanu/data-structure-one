class Solution(object):
    def numberOfMatches(self, n):
        m=0
        if n%2 !=0:
            m=(n-1)/2
            s=m
            while m>0:
                m= n- m
                n=m
                m = m / 2
                s += m
            return s
        else:
            m=n/2
            s=m
            while m>0:
                m= n- m
                n=m
                m = m / 2
                s += m
            return s
            
                


# Usage
sol = Solution()
s = sol.numberOfMatches(7)
print(s)


