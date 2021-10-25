#!/usr/bin/env python
# coding: utf-8

# In[28]:


#Question 1
import numpy as np


# In[29]:


def transpose1(matrix):
    mat_m = matrix.shape[0]   # num row in matrix. will be num cols in transpose
    mat_n = matrix.shape[1]   # num col in matrix. will be num rows in transpose
    matrix_trans = np.empty([mat_n,mat_m])
    for i in range(mat_n):       #iterate thru rows
        for j in range(mat_m):   #iterate thru cols
            matrix_trans[i][j] = matrix[j][i]  #assign elements
    return(matrix_trans)
    


# In[30]:


A = np.array([[1,2], [3,4], [5,6], [7,8]])
print(A)
print(transpose1(A))


# In[ ]:




