#Q) Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), 
# ans[i] is the number of 1's in the binary representation of i.

class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        List=[0]
        c=0
        for i in range(1,n+1):
            k=bin(n)
            for j in k:
                if(j!='b' and int(j)==1):
                    c+=1
            List.append(c)
            c=0
        return(List)