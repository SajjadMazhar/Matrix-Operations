def addition(a, b):
    result = []
    for i in range(len(a)):
        row = []
        for j in range(len(a[0])):
            c = a[i][j] + b[i][j]
            row.append(c)
        result.append(row)
    return result


def matrix_multi(a, b):
    mul = []
    for i in range(len(a)):
        row = []
        for j in range(len(b[0])):
            sop = 0
            for k in range(len(a[0])):
                sop = sop + a[i][k] * b[k][j]
            row.append(sop)
        mul.append(row)
    return mul

def mkMatrix(m, n): # m, n are the parameters for the index(order) of the matrix
    mat = []
    for i in range(m):
        row = []
        for j in range(n):
            print(f"Enter the element ({i+1}, {j+1}) = ",end="")
            element = int(input())
            row.append(element)
        mat.append(row)
    return mat

        

print("Enter the order of the matrix:")
m, n = int(input()), int(input())
print(mkMatrix(m,n))


