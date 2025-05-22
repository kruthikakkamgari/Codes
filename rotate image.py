class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        m=len(matrix[0])
        dupMat=[]
        for i in range(n):
            temp=[0]*n
            dupMat.append(temp)
        for i in range(0,n):
            for j in range(0,n):
                dupMat[j][n-i-1]=matrix[i][j]
        for i in range(0,n):
            for j in range(0,n):
                matrix[i][j]=dupMat[i][j]

        