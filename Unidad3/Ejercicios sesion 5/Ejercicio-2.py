A = [[1, 0, -3], [2, 0, 1], [-1, -1, 0]]
B = [[-1, -2, 0], [-2, 3, 0], [0, 0, -3]]

m = len(A)       
n = len(A[0])     
p = len(B[0])     

C = [[0 for _ in range(p)] for _ in range(m)]


for i in range(m):          
    for j in range(p):      
        for k in range(n):  
            C[i][j] += A[i][k] * B[k][j]

print(C)
