#Q)Given two string arrays words1 and words2, return the number of strings that appear exactly once in each of the two arrays.

class Solution(object):
    def countWords(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: int
        """
        
        list=[]
        c=0
        
        for i in words1:
            for j in words2:
                if(i==j):
                    c=c+1
            if(c==1):
                if i  in list:
                    list.remove(i)
                else:
                    list.append(i)
            
                c=0
                
        return len(list)        