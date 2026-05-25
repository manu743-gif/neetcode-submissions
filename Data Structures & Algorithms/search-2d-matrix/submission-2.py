class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def bs(x,t):
            l = 0
            r = len(x)-1
            while l<=r:
                m = l+ ((r-l)//2)
                if x[m]==t:
                    return True
                elif x[m]<t:
                    l = m +1
                else :
                    r = m-1
            return False 
        for i in range(len(matrix)):
            x = bs(matrix[i],target)
            if x:
                return True 
        return False
