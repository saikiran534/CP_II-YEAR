# Write the function matrixMultiply(m1, m2) that takes two 2d lists 
# (that we will consider to be matrices) and returns a new 2d list that 
# is the result of multiplying the two matrices. Return None if the 
# two matrices cannot be multiplied for any reason.


def fun_matrixmultiply(m1, m2):
    result = [[0 for i in range(len(m2[0]))] for j in range(len(m1))]
    print(result)
    if len(m1[0])!=len(m2):
        return None
    else: 
        for  i in range(len(m1)): #p
            for j in range(len(m2[0])):#q 
                for k in range(len(m2)):#n 
                    result[i][j] = result[i][j]+m1[i][k]*m2[k][j]
    
    # for i in range(len(m1)):
    #     for j in range(len(m2[0])):
    #         print(format(result[i][j],"<5"),end="")
    #     print()
    return result

    
#     for i in range(len(m1)):
  
#     # iterating by coloum by B 
#         for j in range(len(m2[0])):
  
#         # iterating by rows of B
#             for k in range(len(m2)):
#                 result[i][j] += m1[i][k] * m2[k][j]
  
#     for r in result:
#         return r
# m1= [[12, 7],
#     [4, 5],
#     [7, 8]]
  
# # take a 3x4 matrix    
# m2= [[5, 8, 1, 2],
#     [6, 7, 3, 0]]
# print(fun_matrixmultiply(m1,m2))




