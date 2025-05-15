def spiral_traversal(matrix,n):
   # matrix=[[0]* n for k in range(n)]
    start_row,end_row = 0, n-1
    start_col,end_col=0,n-1
    result=[]

    while start_row <= end_row and start_col <= end_col:
        for i in range(start_col,end_col+1):
            result.append(matrix[start_row][i])
            #matrix[start_row][i]=counter
            #counter+=1
        start_row+=1
        for i in range(start_row, end_row+1):
            result.append(matrix[i][end_col])
            #matrix[i][end_col]=counter
            #counter +=1
        end_col -=1
        if start_row <=end_row:
            for i in range(end_col,start_col-1,-1):
                result.append(matrix[end_row][i])
                #counter+=1
            end_row -=1
        if start_col <=end_col:
            for i in range(end_row,start_row-1,-1):
                result.append(matrix[i][start_col])
                #counter+=1
            start_col +=1
    return matrix
n=int(input("Enter the size of spiral"))
matrix=[]
print("enter the matrix row wise")
#spiral_matrix=spiral_traversal(matrix,n)
#print("spiral matrix:")
#for row in spiral_matrix:
    #print(row)
for i in range(n):
    row=list(map(int,input().split()))
    matrix.append(row)

    