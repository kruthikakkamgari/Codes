def input_matrix(rows,cols):
    matrix=[]
    print(f"enter the elements for a {rows}x{cols}")
    for i in range(rows):
        row= list(map(int, input(f"")))
        matrix.append(row)
    return matrix

