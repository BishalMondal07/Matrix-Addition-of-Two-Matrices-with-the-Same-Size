def matrix(m, n):
    o = []
    for i in range(m):
        row = []
        for j in range(n):
            inp = int(input(f"Enter O[{i}][{j}]"))
            row.append(inp)
        o.append(row)
    return o

def sum(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        raise ValueError("Matrices must have the same size")
    output = []
    for i in range(len(A)):
        row = []
        for j in range(len(A[0])):
            row.append(A[i][j] + B[i][j])
        output.append(row)
    return output

m = int(input("Enter the value of m: "))
n = int(input("Enter the value of n: "))

print("Enter Matrix A")
A = matrix(m, n)
print("Enter Matrix B")
B = matrix(m, n)

print(A)

s = sum(A, B)
print(s)
