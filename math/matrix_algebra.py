# Matrix Algebra

import numpy as np

#Constructing matrices and vectors from sheet
A = np.matrix([[1,2,3],[2,7,4]])
B = np.matrix([[1,-1],[0,1]])
C = np.matrix([[5,-1],[9,1],[6,0]])
D = np.matrix([[3,-2,-1],[1,2,3]])
u = np.array([(6,2,-3,5)])
v = np.array([(3,5,-1,4)])
w = np.array([(1, 8, 0, 5)]).T
#added scalar for ease
alpha = 6
#dictionary where each key is the name of the matrix/vector and each value is the matrix/vector itself
array_dict = { 'A':A,
               'B':B,
               'C':C,
               'D':D,
               'u':u,
               'v':v,
               'w':w
               }
#Recreating worksheet for end readability
print('\nLINEAR ALGEBRA WORKSHEET\n')

for key, val in array_dict.items():
    print(str(key) + ' = \n\n' + str(val) + '\n')
#Answers to Part 1, Matrix Dimensions:
print('1. Matrix Dimensions \nWrite the dimensions of each matrix. \n')
for key, val in array_dict.items():
    print('The dimensions of ' + str(key) + ' is ' + str(val.shape) + '.\n')
#A - 2x3, B - 2x2, C - 3x2, D - 2x3, u - 1x4, w - 4x1
    
#Answers to Part 2
print('2. Vector Operations \nPerform the following operatinos. Assume alpha = 6.\n')
print('2.1) u + v = ' + str(u+v) + '\n')
# [9 7 -4 9]
print('2.2) u - v = ' + str(u-v) + '\n')
# [3 -3 -2 1]
print('2.3) (alpha)(u) = ' + str(alpha*u) +'\n')
# [36 12 -18 30]
print('2.4) u * v = ' + str(np.dot(u,v.T)) + '\n')
# 51
print('2.5) ||u|| = ' + str(np.linalg.norm(u)) + '\n')
# 8.602

#Answer to Part 3
#Added extra line breaks for readability
print('3. Matrix Operations \nEvaluate each of the following expressions, if it\
 is defined; else fill in with "not defined". Do your work by hand on scratch paper.\n')

print('3.1) A + C = not defined\n')
# not defined
print('3.2) A - C^T = \n\n' + str(A - C.T) + '\n')
# [-4 -7 -3][3 6 4]
print('3.3) C^T + 3D = \n\n' + str(C.T + 3*D) + '\n')
# [14 3 3][2 7 9]
print('3.4) BA = \n\n' + str(B*A) + '\n')
# [-1 -5 -1][2 7 4]
print('3.5) BA^T = not defined\n')
# not defined
print('3.6) BC = not defined\n')
# not defined
print('3.7) CB = \n\n' + str(C*B) + '\n')
# [5 -6][9 -8][6 -6]
print('3.8) B^4 = \n\n' + str(B**4) + '\n')
# [1 -4][0 1]
print('3.9) AA^T = \n\n' + str(A*A.T) + '\n')
# [14 28][28 69]
print('3.10) (D^T)(D) = \n\n' + str(D.T*D))
# [10 -4 0][-4 8 8][0 8 10]
