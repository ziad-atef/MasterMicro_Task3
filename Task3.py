import numpy as np

n = np.random.randint(0, 100)
m = np.random.randint(0, 100)
p = np.random.randint(0, 100)

matrix3D = np.random.randint(0, 100, size=(n, m, p))

vector = np.zeros(n*m*p)

for i in range(n):
    for j in range(m):
        for k in range(p):
            vector[i*m*p+j*p+k] = matrix3D[i][j][k]

print(matrix3D)
print(vector)
