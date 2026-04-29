def determinan_2x2(m):
    return m[0][0]*m[1][1] - m[0][1]*m[1][0]
def inverse_2x2(matriks):
    det = determinan_2x2(matriks)
    if det == 0:
        print('Matriks singular: inverse tidak ada (det = 0)')
        return None
    a, b = matriks[0][0], matriks[0][1]
    c, d = matriks[1][0], matriks[1][1]
    return [[ d/det, -b/det],
            [-c/det, a/det]]

A = [[4, 7],
[2, 6]]
inv = inverse_2x2(A)
print('Inverse A:')
for baris in inv:
    print([round(x, 4) for x in baris])
# Output:
# Inverse A:
# [0.6, -0.7]
# [-0.2, 0.4]
# Verifikasi: A x A_inv harus menghasilkan matriks identitas

import numpy as np
A_np = np.array(A, dtype=float)
print('A x A_inv:')
print(np.round(A_np @ np.linalg.inv(A_np), 4))
# Output:
# [[1. 0.]
# [0. 1.]]