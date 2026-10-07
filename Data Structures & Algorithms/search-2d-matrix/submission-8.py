class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def get_mel(x,m,n):
            return x//n, x%n
        m,n=len(matrix),len(matrix[0])
        
        low,high=0,m*n
        # get_mel = lambda x : (x//m, x%n)
        while low<high:
            mid = (high+low) // 2
            matrix_idx=get_mel(mid,m,n)
            mel = matrix[matrix_idx[0]][matrix_idx[1]]
            if mel == target:
                return True
            elif mel < target:
                low=mid+1
            else:
                high=mid
        return False
        # two possible approaches: 
        # 1. write a single binary search over the numel, then convert index to matrix id (row-major)
        # 2. first, binary search last column, then binary search the row
